const KEYS = { settings: 'pixelforge_settings', gallery: 'pixelforge_gallery' };
function saveData(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return 1; } catch(e) { return 0; } }
function loadData(k, d = null) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch(e) { return d; } }

function saveSettings(s) { return saveData(KEYS.settings, s); }
function loadSettings() { return loadData(KEYS.settings, { geminiKey: '', geminiModel: 'gemini-2.5-flash-image' }); }

function saveGallery(g) { return saveData(KEYS.gallery, g); }
function loadGallery() { return loadData(KEYS.gallery, []); }