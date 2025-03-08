@echo off
cd /d "%~dp0"
echo Activating virtual environment...
call venv\Scripts\activate

:: Run only home_validation.py, excluding test_login.py
echo Running tests...

python -m pytest tests/test_home_validation.py --html=reports\report.html --maxfail=1 --disable-warnings --tb=short

echo Tests completed. Report saved in reports folder.
pause
