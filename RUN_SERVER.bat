@echo off
echo ============================================
echo   ZURIWAVE - Django Development Server
echo ============================================
echo.
echo Starting server on port 8001...
echo.
echo Once running, open your browser and visit:
echo http://127.0.0.1:8001
echo.
echo Press CTRL+C to stop the server
echo ============================================
echo.
set DJANGO_DEBUG=1
python manage.py runserver 8001
