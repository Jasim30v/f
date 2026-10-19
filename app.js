let settings = { geminiKey: '', geminiModel: 'gemini-2.5-flash-image' };
let currentImageUrl = null;
let currentStyle = 'realistic';
let gallery = [];

const STYLE_PROMPTS = {
    realistic: 'photorealistic, ultra-detailed, 8k, natural lighting',
    anime: 'anime style, vibrant colors, Studio Ghibli inspired, detailed illustration',
    cinematic: 'cinematic composition, dramatic lighting, film grain, 35mm lens, moody',
    '3d': '3D render, octane, ray tracing, Pixar style, volumetric lighting'
};

function init() {
    settings = loadSettings();
    gallery = loadGallery();
    document.getElementById('geminiKey').value = settings.geminiKey || '';
    document.getElementById('geminiModel').value = settings.geminiModel || 'gemini-2.5-flash-image';
    renderGallery();
}

function toggleSettings() {
    const p = document.getElementById('settingsPanel');
    p.style.display = p.style.display === 'none' ? 'block' : 'none';
}

function saveSettings() {
    settings.geminiKey = document.getElementById('geminiKey').value.trim();
    settings.geminiModel = document.getElementById('geminiModel').value.trim() || 'gemini-2.5-flash-image';
    saveSettingsToStorage(settings);
    showToast('✅ تم الحفظ');
    document.getElementById('settingsPanel').style.display = 'none';
}

function saveSettingsToStorage(s) { saveSettings(s); }

function selectStyle(el) {
    document.querySelectorAll('.style-pill').forEach(p => p.classList.remove('active'));
    el.classList.add('active');
    currentStyle = el.dataset.style;
}

function showToast(m) {
    const t = document.getElementById('toast');
    t.innerText = m;
    t.classList.add('show');
    clearTimeout(window._t);
    window._t = setTimeout(() => t.classList.remove('show'), 3000);
}

async function generateImage() {
    const prompt = document.getElementById('promptInput').value.trim();
    if (!prompt) { showToast('⚠️ اكتب وصفاً أولاً'); return; }
    if (!settings.geminiKey) { showToast('⚠️ أدخل مفتاح Gemini في الإعدادات'); toggleSettings(); return; }

    const btn = document.getElementById('generateBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التوليد...';
    
    document.getElementById('loadingOverlay').style.display = 'flex';
    document.getElementById('previewArea').classList.remove('has-image');
    document.getElementById('imgOverlay').style.display = 'none';

    try {
        const fullPrompt = `${prompt}, ${STYLE_PROMPTS[currentStyle]}`;
        const model = settings.geminiModel;
        const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${settings.geminiKey}`;
        
        const body = {
            contents: [{ parts: [{ text: fullPrompt }] }],
            generationConfig: { responseModalities: ["TEXT", "IMAGE"] }
        };

        const res = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error?.message || 'HTTP ' + res.status);

        const parts = data.candidates?.[0]?.content?.parts || [];
        let imagePart = null;
        for (const part of parts) {
            if (part.inlineData && part.inlineData.mimeType && part.inlineData.mimeType.startsWith('image/')) {
                imagePart = part.inlineData;
                break;
            }
        }

        if (!imagePart) {
            const textPart = parts.find(p => p.text);
            throw new Error(textPart ? 'لم يتم توليد صورة: ' + textPart.text.substring(0, 80) : 'لم يتم استلام صورة');
        }

        currentImageUrl = `data:${imagePart.mimeType};base64,${imagePart.data}`;
        document.getElementById('generatedImg').src = currentImageUrl;
        document.getElementById('previewArea').classList.add('has-image');
        document.getElementById('imgOverlay').style.display = 'flex';
        document.getElementById('loadingOverlay').style.display = 'none';
        
        // إضافة للمعرض
        gallery.unshift({ url: currentImageUrl, prompt: prompt, style: currentStyle, at: Date.now() });
        if (gallery.length > 30) gallery = gallery.slice(0, 30);
        saveGallery(gallery);
        renderGallery();
        
        showToast('🎨 تم توليد الصورة!');

    } catch(e) {
        console.error(e);
        document.getElementById('loadingOverlay').style.display = 'none';
        showToast('❌ ' + e.message);
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-bolt"></i> توليد';
    }
}

function renderGallery() {
    const section = document.getElementById('gallerySection');
    const container = document.getElementById('imageGallery');
    const count = document.getElementById('galleryCount');
    
    if (gallery.length === 0) {
        section.style.display = 'none';
        return;
    }
    
    section.style.display = 'block';
    count.innerText = gallery.length + ' صورة';
    container.innerHTML = gallery.map((g, i) => `
        <div class="gallery-item" onclick="loadFromGallery(${i})">
            <img src="${g.url}" alt="${g.prompt}">
        </div>
    `).join('');
}

function loadFromGallery(i) {
    const g = gallery[i];
    currentImageUrl = g.url;
    document.getElementById('generatedImg').src = g.url;
    document.getElementById('previewArea').classList.add('has-image');
    document.getElementById('imgOverlay').style.display = 'flex';
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function downloadImage() {
    if (!currentImageUrl) return;
    const a = document.createElement('a');
    a.href = currentImageUrl;
    a.download = 'pixelforge-' + Date.now() + '.png';
    a.click();
    showToast('📥 جاري التحميل');
}

function shareImage() {
    if (!currentImageUrl) return;
    fetch(currentImageUrl).then(r => r.blob()).then(blob => {
        const file = new File([blob], 'pixelforge.png', { type: blob.type });
        if (navigator.canShare && navigator.canShare({ files: [file] })) {
            navigator.share({ files: [file], title: 'Pixel Forge' });
        } else {
            showToast('⚠️ جهازك لا يدعم المشاركة');
        }
    });
}

function clearAll() {
    if (!confirm('مسح كل الصور من المعرض؟')) return;
    gallery = [];
    saveGallery(gallery);
    renderGallery();
    document.getElementById('previewArea').classList.remove('has-image');
    document.getElementById('imgOverlay').style.display = 'none';
    showToast('🗑️ تم مسح المعرض');
}

window.addEventListener('DOMContentLoaded', init);