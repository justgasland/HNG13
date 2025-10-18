

### 🐱 Django Cat Facts API

A simple Django REST API that returns profile information with dynamic timestamps and random cat facts from an external API.

### Installation

Use the package manager pip to install virtualenv (if you don't already have it).

```bash
pip install virtualenv
```

Create a new Python environment.

```bash
virtualenv venv
```

Activate your environment.

```bash
source venv/bin/activate     # For Mac/Linux
venv\Scripts\activate        # For Windows users
```

Install the project dependencies.

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root and add your details:

```
EMAIL=youremail@example.com
NAME=Your Full Name
```

### Usage

Run the Django development server.

```bash
python manage.py runserver
```

Visit the endpoint in your browser or Postman:

```
http://127.0.0.1:8000/me
```

You should get a JSON response like this:

```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```
## Live API

**Base URL:**
[https://djangocatapp.up.railway.app/](https://djangocatapp.up.railway.app/)

**Endpoint:**
`GET /me`

**Full URL:**
[https://djangocatapp.up.railway.app/me](https://djangocatapp.up.railway.app/me)

---

### Dependencies

* Django
* Django REST Framework
* python-decouple
* requests
* django_ratelimit

Install them all with:

```bash
pip install -r requirements.txt
```

### Notes

* The timestamp updates with each request.
* A new cat fact is fetched every time you hit `/me`.
* If the Cat Facts API fails, a fallback message is returned.
* Rate limiting is enabled to prevent abuse.

<<<<<<< HEAD
=======

>>>>>>> origin/main
