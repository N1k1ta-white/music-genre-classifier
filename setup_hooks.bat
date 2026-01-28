@echo off
:: Check if we are in the root of the repo
if not exist ".git" (
    echo Error: .git folder not found. Please run this script from the project root.
    pause
    exit /b
)

:: Copy the pre-commit file to the hooks folder
echo Installing pre-commit hook...
copy /Y "pre-commit" ".git\hooks\pre-commit"

if %errorlevel% equ 0 (
    echo.
    echo Success! The hook is installed.
) else (
    echo.
    echo Error: Failed to copy the file.
)

pause