# HtStudio V3

Düz **WebView HTML** uygulaması. **htpack yok**, payload yok, ayrı paket yok.

- Motor: PyQt5 + QtWebEngine (gömülü Chromium)
- İçerik: `web/index.html` (+ css/js)
- Çift tıkla çalışır

## Geliştirme
```bat
pip install -r requirements.txt
python main.py
```

## Derleme (Windows)
```bat
build.bat
```
Çıktı: `dist\HtStudioV3\HtStudioV3.exe` (yanında `_internal` ve `web`)

## Kendi HTML’in
`web/` içini değiştir → yeniden `build.bat`.
