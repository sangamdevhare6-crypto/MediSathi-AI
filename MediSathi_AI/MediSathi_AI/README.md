# MediSathi AI — Healthcare Hackathon Starter

A Django-powered healthcare web app starter with an animated responsive dashboard, authentication, patient/doctor/admin roles, appointment booking, medicine reminders, medical-record metadata, and admin management.

> This is a hackathon starter, not a certified medical product. Demo data is fictional. The AI assistant is a safe informational placeholder until you configure a trusted provider. Do not enter real patient information before completing a security/privacy review.

## Requirements
- Python 3.11+
- pip
- Optional: PostgreSQL. SQLite works out of the box.

## Windows setup (PowerShell)
```powershell
cd MediSathi_AI
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
py manage.py makemigrations core
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
Open http://127.0.0.1:8000/ for the app and http://127.0.0.1:8000/admin/ for Django admin.

## First admin
Run `py manage.py createsuperuser`. There is intentionally no public admin registration. In Django admin, users can be assigned Patient, Doctor, or Admin roles. Django staff/superuser status controls access to `/admin/`.

## Main routes
- `/` dashboard
- `/accounts/login/` login
- `/accounts/signup/` patient registration
- `/appointments/` appointments
- `/reminders/` medicine reminders
- `/assistant/` general health information demo
- `/records/` medical record metadata
- `/admin/` Django admin

## Environment
Copy `.env.example` to `.env`, set a strong `DJANGO_SECRET_KEY`, and set `DJANGO_DEBUG=False` plus valid `DJANGO_ALLOWED_HOSTS` for deployment. Configure PostgreSQL using `DATABASE_URL` if desired. Never commit `.env`.

## Security and medical safety notes
- The sample assistant does not diagnose, prescribe, or replace a clinician.
- Appointment and record views are scoped to the signed-in user.
- Before production: configure HTTPS, secure cookies, backups, logging, rate limiting, malware scanning for uploads, consent and retention policies, access auditing, and a professional privacy/security review.
- Do not use the sample metrics as real health measurements.
