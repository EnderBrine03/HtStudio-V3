"""
HtStudio V3 — Düz WebView HTML uygulaması
htpack / payload / launcher YOK. web/ klasöründeki index.html açılır.
"""
import os
import sys
from pathlib import Path


def resource_path(*parts: str) -> Path:
    if getattr(sys, "frozen", False):
        # onedir: exe yanı; onefile: _MEIPASS
        base = Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path(sys.executable).resolve().parent
        # PyInstaller onedir: data files next to exe in _internal or beside
        candidates = [
            Path(sys.executable).resolve().parent,
            Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else None,
        ]
        for c in candidates:
            if c and (c / "web" / "index.html").is_file():
                return c.joinpath(*parts) if parts else c
        return Path(sys.executable).resolve().parent.joinpath(*parts)
    return Path(__file__).resolve().parent.joinpath(*parts)


def main():
    from PyQt5.QtCore import Qt, QUrl
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEnginePage

    app = QApplication(sys.argv)
    app.setApplicationName("HtStudio V3")
    app.setOrganizationName("HtStudio")

    web_dir = resource_path("web")
    index = web_dir / "index.html"
    if not index.is_file():
        # fallback: next to exe
        alt = Path(sys.executable).resolve().parent / "web" / "index.html"
        if alt.is_file():
            index = alt
            web_dir = alt.parent
        else:
            print("HATA: web/index.html bulunamadı:", index)
            sys.exit(1)

    win = QMainWindow()
    win.setWindowTitle("HtStudio V3")
    win.resize(1100, 720)

    view = QWebEngineView()
    settings = view.settings()
    settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
    settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
    settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
    settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

    view.setUrl(QUrl.fromLocalFile(str(index.resolve())))
    win.setCentralWidget(view)
    win.show()
    return app.exec_()


if __name__ == "__main__":
    # Optional: allow opening a custom html path: HtStudioV3.exe path\to\file.html
    sys.exit(main())
