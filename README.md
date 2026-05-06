Django REST API Project

A scalable and modular Django REST API built with Django and Django REST Framework (DRF).

 Features
User authentication & management
RESTful API structure
Modular app architecture
Swagger API documentation
SQLite/PostgreSQL support
Environment-based configuration

 Tech Stack
Python 3.x
Django
Django REST Framework
SQLite / PostgreSQL
drf-yasg (Swagger UI)

Project Structure
project_root/
│
├── backend/          # Main project config
├── api/              # Main app (users, endpoints, logic)
├── manage.py
├── db.sqlite3
└── requirements.txt
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/9Moses/pthon_bankend.git
cd your-repo
2. Create Virtual Environment
python -m venv env

Activate it:

Windows

env\Scripts\activate

Mac/Linux

source env/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Run the Server
python manage.py runserver

App will run on:

http://127.0.0.1:8000/
📘 API Documentation (Swagger)

After setup, access Swagger UI:

http://127.0.0.1:8000/swagger/

ReDoc:

http://127.0.0.1:8000/redoc/
🔑 Example API Endpoints
Method	Endpoint	Description
POST	/api/users/create	Create user
GET	/api/users	Get all users
🧪 Running Tests
python manage.py test
⚠️ Common Issues
❌ no such table: api_user

Run:

python manage.py makemigrations
python manage.py migrate
❌ psycopg2 not found

Install:

pip install psycopg2-binary
🔐 Environment Variables (Optional)

Create .env file:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_db_url
📦 Deployment
Use Gunicorn or uWSGI
Configure Nginx
Set DEBUG = False
Add allowed hosts
👨‍💻 Author

Moses Kwesi Essel