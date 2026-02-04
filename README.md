# Zuriwave - Building Technology to Power African Ambition

A modern Django web application showcasing Zuriwave's vision for African fintech.

## Features

- **Modern Design**: Clean, responsive design with custom Zuriwave branding
- **Django Framework**: Built with Django 5.2 for scalability and security
- **Custom Styling**: Beautiful gradients and animations
- **Mobile Responsive**: Works perfectly on all devices

## Quick Start

### Prerequisites

- Python 3.13+
- Django 5.2

### Installation

1. Navigate to the project directory:
```bash
cd d:\Documents\CODE\Zuriwave
```

2. Run migrations (already done):
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

4. Open your browser and visit:
```
http://127.0.0.1:8000/
```

## Project Structure

```
Zuriwave/
├── core/                    # Main Django app
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/           # Stylesheets
│   │   ├── fonts/         # Font files
│   │   ├── images/        # Image assets
│   │   └── videos/        # Video assets
│   ├── templates/         # HTML templates
│   └── views.py           # View functions
├── zuriwave_project/       # Django project settings
│   ├── settings.py        # Project settings
│   └── urls.py            # URL configuration
└── manage.py              # Django management script
```

## Customization

### Changing Colors

Edit the CSS variables in `core/templates/index.html`:

```css
:root {
    --color-primary: #1a237e;
    --color-primary-light: #3949ab;
    --color-accent: #00bcd4;
    --color-background: #f4f2f0;
    --color-foreground: #0f0802;
}
```

### Adding New Pages

1. Create a new template in `core/templates/`
2. Add a view function in `core/views.py`
3. Add a URL pattern in `zuriwave_project/urls.py`

## Services

- **Modern Payments**: Seamless payment solutions
- **Digital Banking**: Next-generation banking services
- **Mobile Solutions**: Mobile-first financial applications
- **Innovation Labs**: Frontier technology exploration
- **Business Tools**: Enterprise-grade financial tools
- **Security First**: Bank-level security and compliance

## Contact

Email: hello@zuriwave.com

## License

© 2026 Zuriwave. All rights reserved.
