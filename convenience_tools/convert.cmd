@echo off
setlocal enabledelayedexpansion

:: Switch to script directory
cd /D "%~dp0"

:: Check if convert.py exists
if not exist "convert.py" (
    echo convert.py is missing.
    pause
    exit /B 1
)

:: Try every possible Python command until one works
for %%A in (python3 python py) do @(
    echo Checking if Python is installed as %%A
    where %%A
    if !ERRORLEVEL! equ 0 (
        echo Found Python at %%A
        echo Python version:
        %%A --version
        %%A convert.py %*
        goto :Found
    )
)

echo Python not found. Please install Python 3.9 or newer.
pause
exit /B 1

:Found
pause
