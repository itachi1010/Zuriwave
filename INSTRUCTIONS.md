# Zuriwave Django Project - Complete Setup Instructions

## What Was Done

1. ✅ Created a Django 5.2 project named `zuriwave_project`
2. ✅ Created a `core` app to handle the website
3. ✅ Converted the HTTrack-downloaded TSG website to Django template
4. ✅ **Rebranded everything from "The Stack Group" to "Zuriwave"**
5. ✅ Set up static files (CSS, fonts, images, videos)
6. ✅ Configured Django to run on **port 8001** (avoiding port conflicts)

## Project Structure

```
Zuriwave/
├── core/                          # Main Django app
│   ├── static/                    # Static assets
│   │   ├── css/                  # CSS files from _nuxt
│   │   │   ├── entry.PUmZFD-c.css
│   │   │   ├── index.CcfutiKt.css
│   │   │   └── *.js files
│   │   ├── fonts/                # PPMori font files
│   │   ├── images/               # Image assets
│   │   └── videos/               # Video assets
│   ├── templates/                # HTML templates
│   │   └── index.html           # Main page (Zuriwave branded)
│   └── views.py                  # View functions
├── zuriwave_project/             # Django project settings
│   ├── settings.py              # Configured for static files
│   └── urls.py                   # URL routing
├── manage.py                     # Django management script
├── RUN_SERVER.bat               # Quick start script
└── db.sqlite3                    # Database (auto-created)
```

## How to Run the Server

### Option 1: Double-click the batch file
Simply double-click `RUN_SERVER.bat` in Windows Explorer

### Option 2: Command line
```bash
cd d:\Documents\CODE\Zuriwave
python manage.py runserver 8001
```

### Option 3: Using a different port
If port 8001 is also occupied, use any free port:
```bash
python manage.py runserver 8888
# or
python manage.py runserver 9000
```

## Access the Website

Once the server is running, open your browser and visit:
**http://127.0.0.1:8001**

## Currently Occupied Ports (To Avoid)

- Port 80, 443 - HTTP/HTTPS
- Port 5432, 5433 - PostgreSQL
- Port 6379 - Redis
- Port 8000 - Another service
- Port 8080, 8090 - Other web services

**Port 8001 is FREE and recommended!**

## What Changed from TSG to Zuriwave

All references have been replaced:
- "The Stack Group" → "Zuriwave"
- "TSG" → "Zuriwave"
- "tsg.xyz" → "zuriwave.com"
- "hello@tsg.xyz" → "hello@zuriwave.com"
- Page title and meta information updated
- All branding text updated throughout the site

## Template Details

The template uses:
- Original HTTrack design and layout
- All CSS and styling from the original TSG site
- PPMori font family
- Responsive design
- Django template tags for static files ({% static %})

## Troubleshooting

### Server won't start
1. Make sure you're in the correct directory:
   ```bash
   cd d:\Documents\CODE\Zuriwave
   ```

2. Check if Python is installed:
   ```bash
   python --version
   ```

3. Check if Django is installed:
   ```bash
   pip list | findstr Django
   ```

### Port is already in use
If you get an error like "That port is already in use", try a different port:
```bash
python manage.py runserver 8002
```

### Static files not loading
Run:
```bash
python manage.py collectstatic
```

### CSS/Images not showing
1. Check that files exist in `core/static/`
2. Verify `STATICFILES_DIRS` in settings.py
3. Restart the server

## Development Tips

### Creating New Pages
1. Create HTML template in `core/templates/`
2. Add view function in `core/views.py`
3. Add URL pattern in `zuriwave_project/urls.py`

### Modifying the Homepage
Edit `core/templates/index.html`

### Changing Styling
CSS files are in `core/static/css/`

### Admin Panel
Access at: http://127.0.0.1:8001/admin
(You'll need to create a superuser first)

## Next Steps

1. **Run the server**: `python manage.py runserver 8001`
2. **View the site**: http://127.0.0.1:8001
3. **Customize content**: Edit `core/templates/index.html`
4. **Add features**: Create new apps and templates

## Contact

For questions about this Django implementation:
- Check Django documentation: https://docs.djangoproject.com
- Review the code in `core/views.py` and `zuriwave_project/urls.py`

---

**Your Zuriwave website is ready to run! 🚀**

Just run: `python manage.py runserver 8001`
