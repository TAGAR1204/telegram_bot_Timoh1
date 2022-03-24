@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5125306171:AAEUwK4OJErKFHMhgPgLAnvNyVbtcGnNPDg

python bot_telegram.py

pause