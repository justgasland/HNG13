# 🐱 Django Cat Facts API

A professional RESTful API built with Django REST Framework that returns profile information with dynamic timestamps and random cat facts from an external API.

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🌟 Features

- ✅ RESTful API endpoint (`/me`)
- ✅ Dynamic UTC timestamp generation
- ✅ External API integration (Cat Facts API)
- ✅ Environment variable configuration
- ✅ CORS support for cross-origin requests
- ✅ Comprehensive logging for debugging
- ✅ Rate limiting protection
- ✅ Error handling and graceful fallbacks
- ✅ Production-ready deployment configuration

---

## 📂 GitHub Repository

**Live Repo:** [https://github.com/abdulgaffarsonola/django-cat-facts-api](https://github.com/abdulgaffarsonola/django-cat-facts-api)

---

## 🚀 Live Demo

**API Endpoint:** [Add your deployed URL here]

**Example Request:**
```bash
curl https://your-deployed-url.com/me
```

**Example Response:**
```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Name",
    "stack": "Python/Django REST Framework"
  },
  "timestamp": "2025-10-17T14:30:45.123Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.11** | Core programming language |
| **Django 4.2** | Web framework |
| **Django REST Framework** | RESTful API toolkit |
| **python-decouple** | Environment variable management |
| **django-cors-headers** | CORS handling |
| **django-ratelimit** | API rate limiting |
| **Gunicorn** | WSGI HTTP server for production |
| **Requests** | HTTP library for external API calls |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download here](https://git-scm.com/downloads)
- **Virtual environment** (recommended)

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abdulgaffarsonola/django-cat-facts-api.git
cd django-cat-facts-api
```

### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory (same level as `manage.py`):

```env
# .env file
MY_EMAIL=youremail@example.com
MY_NAME=Your Full Name
DEBUG=True
SECRET_KEY=your-secret-key-here
```

**Note:** A `.env.example` file is provided as a template. Copy it and fill in your details:

```bash
cp .env.example .env
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

### 6️⃣ Test the Endpoint

Open your browser or use `curl`:

```
http://127.0.0.1:8000/me
```

You should see a JSON response with your profile info and a cat fact! 🎉

---

## 📁 Project Structure

```
django-cat-facts-api/
│
├── backend_wizards/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings & configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI config for deployment
│   └── asgi.py
│
├── api/                      # Main API application
│   ├── __init__.py
│   ├── views.py             # API endpoint logic
│   ├── apps.py
│   └── tests.py
│
├── venv/                     # Virtual environment (not in repo)
├── .env                      # Environment variables (not in repo)
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
├── runtime.txt               # Python version specification
├── manage.py                 # Django management script
└── README.md                 # This file
```

---

## 🔧 Configuration

### Environment Variables

The following environment variables can be configured in your `.env` file:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `MY_EMAIL` | Your email address | ✅ Yes | - |
| `MY_NAME` | Your full name | ✅ Yes | - |
| `DEBUG` | Debug mode (True/False) | No | False |
| `SECRET_KEY` | Django secret key | ✅ Yes | - |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | No | * |

### Generate a Secret Key

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📡 API Documentation

### Endpoint: `GET /me`

Returns profile information with a dynamic timestamp and random cat fact.

#### Request

```http
GET /me HTTP/1.1
Host: your-api-domain.com
```

#### Response

**Status Code:** `200 OK`

**Headers:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django REST Framework"
  },
  "timestamp": "2025-10-17T14:30:45.123Z",
  "fact": "A cat's hearing is better than a dog's."
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Always returns "success" |
| `user.email` | string | Your email from environment variable |
| `user.name` | string | Your name from environment variable |
| `user.stack` | string | Technology stack used |
| `timestamp` | string | Current UTC time in ISO 8601 format |
| `fact` | string | Random cat fact from Cat Facts API |

#### Error Responses

**405 Method Not Allowed**
```json
{
  "error": "Method not allowed"
}
```

**429 Too Many Requests** (Rate limit exceeded)
```json
{
  "error": "Rate limit exceeded. Try again later."
}
```

---

## 🧪 Testing

### Manual Testing

```bash
# Test with curl
curl http://127.0.0.1:8000/me

# Test with httpie (if installed)
http GET http://127.0.0.1:8000/me

# Test in browser
open http://127.0.0.1:8000/me
```

### Automated Testing

Run Django tests:
```bash
python manage.py test
```

---

## 🚢 Deployment

### Deployment Platforms

This project is configured for deployment on:
- ✅ Railway
- ✅ Heroku
- ✅ AWS Elastic Beanstalk
- ✅ PythonAnywhere
- ✅ DigitalOcean App Platform

### Railway Deployment (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Add environment variables in Railway dashboard:
     - `MY_EMAIL`
     - `MY_NAME`
     - `SECRET_KEY`

3. **Railway auto-detects Django** and uses `Procfile`

4. **Get your URL** and test!

### Heroku Deployment

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set MY_EMAIL=youremail@example.com
heroku config:set MY_NAME="Your Name"
heroku config:set SECRET_KEY=your-secret-key

# Deploy
git push heroku main

# Open app
heroku open
```

### Environment Variables for Production

Set these in your deployment platform:

```
MY_EMAIL=youremail@example.com
MY_NAME=Your Full Name
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
Django==4.2.7
djangorestframework==3.14.0
requests==2.31.0
gunicorn==21.2.0
python-decouple==3.8
django-cors-headers==4.3.1
django-ratelimit==4.1.0
```

---

## 🔒 Security Features

- ✅ **Environment variables** for sensitive data
- ✅ **CORS configuration** for controlled access
- ✅ **Rate limiting** (100 requests/hour per IP)
- ✅ **Secret key** protection
- ✅ **Debug mode** disabled in production
- ✅ **Allowed hosts** configuration

---

## 🐛 Troubleshooting

### Common Issues

**1. Cat Facts API returns fallback message**
- The external API might be temporarily down
- Check your internet connection
- The app gracefully handles this with a fallback message

**2. "Module not found" errors**
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

**3. Port already in use**
```bash
# Use a different port
python manage.py runserver 8080
```

**4. Environment variables not loading**
- Ensure `.env` file is in the same directory as `manage.py`
- Check for typos in variable names
- Verify `python-decouple` is installed

---

## 📝 Development Notes

### Logging

The application includes comprehensive logging:

```python
# View logs during development
python manage.py runserver

# Logs show:
# - Endpoint access
# - External API calls
# - Errors and warnings
# - Timestamp generation
```

### Rate Limiting

- **Limit:** 100 requests per hour per IP address
- **Modify in:** `api/views.py` - `@ratelimit` decorator
- **Disable for testing:** Comment out the decorator

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---




---



<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ and ☕ by Abdul Gaffar Sonola

</div>
