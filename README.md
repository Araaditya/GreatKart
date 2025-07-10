# 🛒 QuickBasket

QuickBasket is a fully functional e-commerce web application built with Django. It provides core features found in modern online shopping platforms including user authentication, product browsing, cart management, and checkout workflow.

## 🔧 Features

- 🧍‍♂️ User registration, login, logout
- 🛍️ Product listing and categorization
- 🛒 Cart management with quantity handling
- ✅ Checkout system
- 🔐 Secure user authentication and session management
- 📦 Order history (if implemented)
- 📧 Email verification and password reset support (if SMTP integrated)

## 🗂️ Project Structure

```
QuickBasket/
│
├── accounts/              # User registration and authentication
├── cart/                  # Cart and session-based order handling
├── store/                 # Product and category management
├── orders/                # Order placement and tracking (if present)
├── templates/             # HTML templates for the UI
├── static/                # CSS, JS, images
├── media/                 # Uploaded media files
├── manage.py              # Django project management script
├── requirements.txt       # List of dependencies
└── .env-sample            # Sample environment variables
```

## 🚀 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/your-username/QuickBasket.git
cd QuickBasket
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Rename `.env-sample` to `.env` and fill in the necessary keys like database config, email, secret key, etc.

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Start the development server**
```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap (or similar)
- **Database**: SQLite (default) or PostgreSQL
- **Deployment Ready**: Can be deployed to Heroku, Railway, or any VPS

## 📄 License

This project is licensed under the MIT License.
