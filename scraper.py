#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  🎨  PIXEL FORGE 2044 - ULTIMATE AI IMAGE GENERATOR  🎨   ║
║                                                            ║
║  🔑 Gemini API (Nano Banana)                               ║
║  ✨ توليد صور + معرض داخلي + أنماط فنية                     ║
║  💎 تصميم فخم + خلفية Aurora متحركة                         ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os

TOTAL_LINES = 0

DEFAULT_MODEL = "gemini-2.5-flash-image"

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  🎨 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🖼️ 1. index.html
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🎨 Pixel Forge</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- خلفية Aurora المتحركة -->
    <div class="aurora">
        <div class="aurora-blob aurora-1"></div>
        <div class="aurora-blob aurora-2"></div>
        <div class="aurora-blob aurora-3"></div>
    </div>
    <div class="noise-overlay"></div>

    <div class="app">
        <!-- الهيدر -->
        <header class="glass-header">
            <div class="brand">
                <div class="brand-icon">🎨</div>
                <div class="brand-text">
                    <h1>FORGE</h1>
                    <span>AI IMAGE GEN</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="icon-btn" onclick="toggleSettings()" id="btnSettings"><i class="fas fa-sliders"></i></button>
                <button class="icon-btn" onclick="clearAll()" title="مسح المعرض"><i class="fas fa-trash"></i></button>
            </div>
        </header>

        <!-- معاينة الصورة -->
        <section class="hero-preview glass-card" id="previewArea">
            <div class="empty-forge" id="emptyState">
                <i class="fas fa-wand-magic-sparkles"></i>
                <p>اكتب وصفاً في الأسفل لتبدأ</p>
            </div>
            <div class="loading-overlay" id="loadingOverlay" style="display:none;">
                <div class="spinner"></div>
                <p>جاري التوليد...</p>
            </div>
            <img class="generated-img" id="generatedImg" alt="">
            <div class="img-overlay" id="imgOverlay" style="display:none;">
                <button class="action-circle" onclick="downloadImage()"><i class="fas fa-download"></i></button>
                <button class="action-circle" onclick="shareImage()"><i class="fas fa-share"></i></button>
            </div>
        </section>

        <!-- حقل الإدخال -->
        <section class="prompt-section glass-card">
            <textarea id="promptInput" class="luxury-textarea" placeholder="اكتب وصف الصورة هنا... (مثال: قطة تشرب قهوة في الفضاء)" rows="3"></textarea>
            
            <div class="style-pills">
                <button class="style-pill active" data-style="realistic" onclick="selectStyle(this)">📷 واقعي</button>
                <button class="style-pill" data-style="anime" onclick="selectStyle(this)">🌸 أنمي</button>
                <button class="style-pill" data-style="cinematic" onclick="selectStyle(this)">🎬 سينمائي</button>
                <button class="style-pill" data-style="3d" onclick="selectStyle(this)">🧊 3D</button>
            </div>

            <div class="prompt-actions">
                <select id="aspectRatio" class="luxury-select">
                    <option value="1:1">مربع 1:1</option>
                    <option value="16:9">عريض 16:9</option>
                    <option value="9:16">طولي 9:16</option>
                </select>
                <button class="generate-btn" id="generateBtn" onclick="generateImage()">
                    <i class="fas fa-bolt"></i> توليد
                </button>
            </div>
        </section>

        <!-- معرض الصور المولدة -->
        <section class="gallery-section" id="gallerySection" style="display:none;">
            <div class="section-title">
                <h3><i class="fas fa-images"></i> معرضك</h3>
                <span id="galleryCount">0 صورة</span>
            </div>
            <div class="image-gallery" id="imageGallery"></div>
        </section>

        <!-- لوحة الإعدادات -->
        <div class="glass-modal" id="settingsPanel" style="display:none">
            <div class="modal-header">
                <h3><i class="fas fa-sliders"></i> الإعدادات</h3>
                <button class="close-btn" onclick="toggleSettings()"><i class="fas fa-times"></i></button>
            </div>
            <div class="modal-body">
                <label>مفتاح Gemini API</label>
                <input type="password" class="luxury-input" id="geminiKey" placeholder="AIza...">
                
                <label>الموديل (Model)</label>
                <input type="text" class="luxury-input" id="geminiModel" placeholder="gemini-2.5-flash-image">
                
                <button class="luxury-btn primary full-width" onclick="saveSettings()">حفظ</button>
            </div>
        </div>
    </div>

    <div class="luxury-toast" id="toast"></div>

    <script src="storage.js"></script>
    <script src="app.js"></script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🎨 2. style.css
# ═══════════════════════════════════════════════════════════

def build_style():
    return """@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&family=Syne:wght@600;700;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
    --bg: #020204;
    --surface: rgba(255, 255, 255, 0.04);
    --border: rgba(255, 255, 255, 0.1);
    --text: #ffffff;
    --text-dim: #8b8b9e;
    --gold: #ffd700;
    --gold-glow: rgba(255, 215, 0, 0.3);
    --cyan: #00f0ff;
    --cyan-glow: rgba(0, 240, 255, 0.4);
    --purple: #a855f7;
    --purple-glow: rgba(168, 85, 247, 0.4);
    --danger: #ff3366;
    --radius-xl: 32px;
    --radius-lg: 24px;
    --radius-md: 16px;
}

body {
    font-family: 'Cairo', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}

/* خلفية Aurora المتحركة */
.aurora {
    position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
}
.aurora-blob {
    position: absolute; border-radius: 50%; filter: blur(100px); opacity: 0.35;
    animation: float 20s ease-in-out infinite;
}
.aurora-1 { width: 400px; height: 400px; background: var(--purple); top: -150px; right: -100px; }
.aurora-2 { width: 350px; height: 350px; background: var(--cyan); bottom: -100px; left: -100px; animation-delay: -7s; }
.aurora-3 { width: 250px; height: 250px; background: var(--gold); top: 40%; left: 30%; animation-delay: -14s; opacity: 0.15; }
@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(30px, -30px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.95); }
}

.noise-overlay {
    position: fixed; inset: 0; z-index: 0; pointer-events: none; opacity: 0.03;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

.app { width: 100%; max-width: 480px; margin: 0 auto; padding: 20px 16px 40px; position: relative; z-index: 1; }

.glass-card, .glass-header, .glass-modal {
    background: var(--surface);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.05);
}

/* الهيدر */
.glass-header { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; margin-bottom: 20px; }
.brand { display: flex; align-items: center; gap: 12px; }
.brand-icon { font-size: 28px; filter: drop-shadow(0 0 10px var(--gold)); }
.brand-text h1 { font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 800; letter-spacing: 2px; background: linear-gradient(135deg, #fff, #aaa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.brand-text span { font-size: 9px; letter-spacing: 3px; color: var(--gold); font-weight: 700; }
.header-actions { display: flex; gap: 8px; }
.icon-btn { width: 42px; height: 42px; border-radius: var(--radius-md); background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--text); font-size: 16px; cursor: pointer; transition: all 0.3s; }
.icon-btn:hover { background: rgba(255,255,255,0.1); color: var(--gold); transform: translateY(-2px); }

/* المعاينة */
.hero-preview { position: relative; width: 100%; aspect-ratio: 1; overflow: hidden; margin-bottom: 16px; border-radius: var(--radius-xl); display: flex; align-items: center; justify-content: center; }
.empty-forge { text-align: center; color: var(--text-dim); }
.empty-forge i { font-size: 48px; margin-bottom: 12px; opacity: 0.3; }
.empty-forge p { font-size: 14px; }
.generated-img { width: 100%; height: 100%; object-fit: cover; display: none; position: absolute; inset: 0; }
.hero-preview.has-image .generated-img { display: block; }
.hero-preview.has-image .empty-forge { display: none; }
.img-overlay { position: absolute; bottom: 16px; left: 16px; right: 16px; display: flex; gap: 10px; justify-content: center; opacity: 0; transition: 0.3s; z-index: 2; }
.hero-preview:hover .img-overlay { opacity: 1; }
.action-circle { width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.6); backdrop-filter: blur(10px); border: 1px solid var(--border); color: #fff; font-size: 16px; cursor: pointer; transition: 0.3s; }
.action-circle:hover { background: var(--gold); color: #000; }

/* مؤشر التحميل */
.loading-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 3; gap: 16px; }
.spinner { width: 60px; height: 60px; border: 4px solid rgba(255,255,255,0.1); border-top-color: var(--gold); border-radius: 50%; animation: spin 1s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.loading-overlay p { font-size: 14px; color: var(--text-dim); font-weight: 700; }

/* حقل الإدخال */
.prompt-section { padding: 16px; margin-bottom: 20px; }
.luxury-textarea { width: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 12px; color: var(--text); font-family: 'Cairo', sans-serif; font-size: 14px; resize: none; outline: none; transition: 0.3s; margin-bottom: 12px; }
.luxury-textarea:focus { border-color: var(--cyan); box-shadow: 0 0 15px var(--cyan-glow); }

/* أنماط الصور */
.style-pills { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
.style-pill { padding: 8px 14px; border-radius: 20px; background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--text-dim); font-family: 'Cairo', sans-serif; font-size: 11px; font-weight: 700; cursor: pointer; transition: 0.3s; }
.style-pill:hover { color: var(--text); border-color: var(--text); }
.style-pill.active { background: var(--gold); color: #000; border-color: var(--gold); box-shadow: 0 0 15px var(--gold-glow); }

.prompt-actions { display: flex; gap: 10px; }
.luxury-select { flex: 1; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 10px; color: var(--text); font-family: 'Cairo', sans-serif; font-size: 12px; outline: none; cursor: pointer; }
.generate-btn { flex: 1.5; padding: 12px; border-radius: var(--radius-md); border: none; background: linear-gradient(135deg, var(--gold), #ffaa00); color: #000; font-family: 'Cairo', sans-serif; font-size: 14px; font-weight: 800; cursor: pointer; transition: 0.3s; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 0 20px var(--gold-glow); }
.generate-btn:hover { transform: translateY(-2px); box-shadow: 0 0 30px var(--gold-glow); }
.generate-btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }

/* المعرض */
.gallery-section { margin-top: 20px; }
.section-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.section-title h3 { font-size: 14px; font-weight: 800; display: flex; align-items: center; gap: 8px; }
.section-title span { font-size: 11px; color: var(--text-dim); }
.image-gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.gallery-item { position: relative; aspect-ratio: 1; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border); cursor: pointer; transition: 0.3s; }
.gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: 0.3s; }
.gallery-item:hover img { transform: scale(1.1); }
.gallery-item:hover { border-color: var(--gold); box-shadow: 0 0 15px var(--gold-glow); }

/* النوافذ */
.glass-modal { padding: 20px; margin-top: 20px; animation: modalIn 0.4s ease; }
@keyframes modalIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.modal-header h3 { font-size: 16px; font-weight: 800; display: flex; align-items: center; gap: 8px; }
.close-btn { width: 32px; height: 32px; border-radius: 50%; background: rgba(255,255,255,0.05); border: none; color: var(--text-dim); cursor: pointer; transition: 0.3s; }
.close-btn:hover { background: var(--danger); color: #fff; }
.modal-body { display: flex; flex-direction: column; gap: 12px; }
.modal-body label { font-size: 11px; font-weight: 700; color: var(--text-dim); letter-spacing: 1px; margin-bottom: -6px; }
.luxury-input { width: 100%; padding: 14px; border-radius: var(--radius-md); background: rgba(0,0,0,0.4); border: 1px solid var(--border); color: var(--text); font-family: 'Cairo', sans-serif; font-size: 14px; outline: none; transition: 0.3s; }
.luxury-input:focus { border-color: var(--cyan); box-shadow: 0 0 15px var(--cyan-glow); }
.luxury-btn { padding: 14px; border-radius: var(--radius-md); border: none; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer; transition: 0.3s; }
.luxury-btn.primary { background: var(--gold); color: #000; }
.luxury-btn.primary:hover { background: #fff; }
.full-width { width: 100%; }

.luxury-toast { position: fixed; bottom: -100px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.9); backdrop-filter: blur(20px); padding: 14px 28px; border-radius: 30px; border: 1px solid var(--gold); font-size: 13px; font-weight: 700; transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1); z-index: 1000; box-shadow: 0 0 30px var(--gold-glow); white-space: nowrap; }
.luxury-toast.show { bottom: 40px; }
"""

# ═══════════════════════════════════════════════════════════
# 💾 3. storage.js
# ═══════════════════════════════════════════════════════════

def build_storage_js():
    return """const KEYS = { settings: 'pixelforge_settings', gallery: 'pixelforge_gallery' };
function saveData(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return 1; } catch(e) { return 0; } }
function loadData(k, d = null) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch(e) { return d; } }

function saveSettings(s) { return saveData(KEYS.settings, s); }
function loadSettings() { return loadData(KEYS.settings, { geminiKey: '', geminiModel: '""" + DEFAULT_MODEL + """' }); }

function saveGallery(g) { return saveData(KEYS.gallery, g); }
function loadGallery() { return loadData(KEYS.gallery, []); }"""

# ═══════════════════════════════════════════════════════════
# ⚙️ 4. app.js
# ═══════════════════════════════════════════════════════════

def build_app_js():
    return """let settings = { geminiKey: '', geminiModel: '""" + DEFAULT_MODEL + """' };
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
    document.getElementById('geminiModel').value = settings.geminiModel || '""" + DEFAULT_MODEL + """';
    renderGallery();
}

function toggleSettings() {
    const p = document.getElementById('settingsPanel');
    p.style.display = p.style.display === 'none' ? 'block' : 'none';
}

function saveSettings() {
    settings.geminiKey = document.getElementById('geminiKey').value.trim();
    settings.geminiModel = document.getElementById('geminiModel').value.trim() || '""" + DEFAULT_MODEL + """';
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

window.addEventListener('DOMContentLoaded', init);"""

# ═══════════════════════════════════════════════════════════
# 🚀 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print(f"""
╔══════════════════════════════════════════════════════════╗
║  🎨  PIXEL FORGE 2044 - ULTIMATE  🎨                   ║
║     Model: {DEFAULT_MODEL:<46}║
╚══════════════════════════════════════════════════════════╝
    """)
    section("BUILDING PIXEL FORGE ULTIMATE")

    write("index.html", build_index())
    write("style.css", build_style())
    write("storage.js", build_storage_js())
    write("app.js", build_app_js())

    print(f"""
{'='*60}
  ✅ BUILD COMPLETE! - {TOTAL_LINES} سطر
  📁 4 ملفات فقط

  ✨ الميزات الجديدة:
     ✅ خلفية Aurora متحركة (فخمة جداً)
     ✅ 4 أنماط فنية (واقعي/أنمي/سينمائي/3D)
     ✅ معرض صور مدمج (يحفظ آخر 30 صورة)
     ✅ مؤشر تحميل احترافي
     ✅ زر تحميل ومشاركة
     ✅ زر مسح المعرض
     ✅ لا يوجد رفع سحابي (كما طلبت)

  🚀 الخطوات:
     1. شغّل السكربت
     2. ارفع الـ 4 ملفات إلى GitHub
     3. افتح التطبيق → ⚙️ → ضع مفتاح Gemini
     4. اكتب وصفاً → اختر نمط → اضغط "توليد"

  🎨 READY!
{'='*60}
    """)

if __name__ == "__main__":
    main()
