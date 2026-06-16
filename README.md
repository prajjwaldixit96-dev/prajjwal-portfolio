# Prajjwal Portfolio — Django Backend

## Setup

```bash
# 1. Virtual environment banao
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 2. Dependencies install karo
pip install django

# 3. Migrations run karo
python manage.py migrate

# 4. Superuser banao
python manage.py createsuperuser

# 5. Server start karo
python manage.py runserver
```

## URLs
| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/` | Portfolio homepage |
| `http://127.0.0.1:8000/admin/` | Admin panel |
| `http://127.0.0.1:8000/contact/submit/` | Contact form endpoint (POST) |

## Admin Panel
- **Username:** admin
- **Password:** admin123 *(production mein change karo!)*

## Features
- ✅ Contact form — messages SQLite mein save hoti hain
- ✅ Admin panel — messages read/replied status ke saath manage kar sako
- ✅ CSRF protection
- ✅ Field-level validation with error messages
- ✅ Toast notifications (success/error)
- ✅ IP address logging

## Project Structure
```
portfolio_django/
├── core/               # Django project config
│   ├── settings.py
│   └── urls.py
├── portfolio/          # Main app
│   ├── models.py       # ContactMessage model
│   ├── views.py        # index + contact_submit views
│   ├── admin.py        # Admin config
│   └── urls.py
├── templates/
│   └── index.html      # Tera UI (Django template)
├── static/
│   └── assets/         # SVG files
├── db.sqlite3          # Database (auto-create hoti hai)
└── manage.py
```
