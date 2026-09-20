@echo off
setlocal
py -3.11 -m venv venv 2>nul || py -3 -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --noconsole --onedir --name HtStudioV3 --add-data "web;web" main.py
echo.
echo Cikti: dist\HtStudioV3\HtStudioV3.exe
echo web\ klasoru exe ile birlikte gelir. htpack YOK.
pause
