@echo off

call %~dp0Bugget_Bot\venv\Scripts\activate

cd %~dp0Bugget_Bot\Budget_Bot

SET TOKEN=you TOKEN

python main.py

pause