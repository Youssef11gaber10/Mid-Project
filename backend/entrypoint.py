from app import app, db
import subprocess
import sys

# إنشاء الجداول لو مش موجودة (بديل سريع عن migrations)
with app.app_context():
    db.create_all()
    print("✅ Tables are ready!")

# لو عندك Flask-Migrate وتريد run migrations:
# subprocess.run(["flask", "db", "upgrade"], check=True)

# تشغيل Gunicorn بعد التأكد من الجداول
subprocess.run([
    "/youssef/venv/bin/gunicorn",
    "app:app",
    "--bind", "0.0.0.0:5000",
    "--workers", "3"
])