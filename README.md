
🛒 GreatKart — Django E-Commerce Platform

A full-stack e-commerce web application built with Django, featuring product catalog, cart, checkout, order management, and a clean, responsive UI.

🔗 Live Demo: ecommerce-project-5-86b1.onrender.com

Show Image
Show Image
Show Image
Show Image

</div>

📋 Table of Contents


📖 Project Overview
✨ Features
🛠️ Tech Stack
📂 Project Structure
⚙️ Requirements
🚀 Setup & Installation
🔑 Environment Variables
🗄️ Database & Migrations
🎨 Static Files & Media
▶️ Running the Project
📸 Screenshots
🧪 Tests
🤝 Contributing
⚠️ Notes
📄 License



📖 Project Overview

GreatKart is a Django-based e-commerce project built to demonstrate a complete full-stack e-commerce flow — from browsing products to placing an order. It's structured as multiple modular Django apps, making the codebase clean and easy to extend.


✨ Features

FeatureDescription🛍️ Product CatalogBrowse products organized by categories🔍 SearchSearch products by keyword📄 Product DetailsDedicated detail page for every product🛒 Cart ManagementAdd, update, and remove items from cart💳 Checkout & OrdersComplete checkout flow with order creation👤 User AuthenticationSign up, login, and account management🛠️ Admin PanelManage products, categories, and orders via Django Admin


🛠️ Tech Stack


Backend: Python, Django
Database: SQLite (development) — easily swappable with PostgreSQL/MySQL
Frontend: HTML, CSS, JavaScript, Bootstrap
Admin: Django's built-in admin interface



📂 Project Structure

greatkart/
├── accounts/              # 👤 User authentication & profiles
├── cart/                  # 🛒 Shopping cart logic
├── category/              # 🗂️ Product categories
├── store/                 # 🏬 Main product store app
├── orders/                # 📦 Order processing
├── search/                 # 🔍 Search implementation
├── greatkart_template/     # 🎨 Templates & example pages
├── static/, staticfiles/   # 🎨 CSS, JS, images
├── media/                  # 🖼️ Uploaded product images
├── docs/screenshots/       # 📸 README screenshots (see below)
├── db.sqlite3              # 🗄️ Development database
├── manage.py                # ⚙️ Django management script
└── requirements.txt          # 📜 Python dependencies


⚙️ Requirements

Make sure you have Python 3.x and pip installed. It's recommended to use a virtual environment.

bashpip install -r requirements.txt


🚀 Setup & Installation

bash# 1️⃣ Clone the repository
git clone <your-repo-url>
cd greatkart

# 2️⃣ Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt


🔑 Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your_database_url   # optional, if not using default SQLite


Make sure settings.py is configured to read these values from the environment.




🗄️ Database & Migrations

The repo ships with a ready-to-use db.sqlite3. To start fresh:

bashpython manage.py makemigrations
python manage.py migrate

Create an admin/superuser account:

bashpython manage.py createsuperuser


🎨 Static Files & Media

Before deploying, collect static files:

bashpython manage.py collectstatic


Ensure MEDIA_ROOT and STATIC_ROOT are correctly set in settings.py for production.




▶️ Running the Project

bashpython manage.py runserver

Then open 👉 http://127.0.0.1:8000/ in your browser.


📸 Screenshots


📌 Yaha screenshots add karni hain. Ek docs/screenshots/ folder banao repo me, images upload karo, aur neeche diye gaye markdown ko unke sahi jagah par README me use karo.



PageScreenshot PathPreview🏠 Home / Landing Pagedocs/screenshots/home.png![Home](docs/screenshots/home.png)🗂️ Product Listing / Category Pagedocs/screenshots/product-list.png![Product Listing](docs/screenshots/product-list.png)📄 Product Detail Pagedocs/screenshots/product-detail.png![Product Detail](docs/screenshots/product-detail.png)🛒 Cart Pagedocs/screenshots/cart.png![Cart](docs/screenshots/cart.png)💳 Checkout / Order Confirmationdocs/screenshots/checkout.png![Checkout](docs/screenshots/checkout.png)🛠️ Admin Dashboard (optional)docs/screenshots/admin.png![Admin Dashboard](docs/screenshots/admin.png)

📍 Kaha insert karni hai (guide):


Home page screenshot → Project Overview ke turant baad
Product listing / detail screenshots → Features section ke niche
Cart screenshot → Cart Management feature ke paas
Checkout screenshot → Orders/Checkout section ke paas
Admin dashboard screenshot → optional, ek alag "Admin Panel" subsection bana ke


✅ Tip: Sab screenshots same resolution (jaise 1280x720) me rakho — README zyada professional aur clean dikhega.


🧪 Tests

Run tests (if available) with:

bashpython manage.py test

(Agar abhi tests nahi likhe hain, to yeh section future me update kar sakte ho.)


🤝 Contributing

Contributions welcome! 🎉


🍴 Fork the repository
🌿 Create a feature branch: git checkout -b feat/my-feature
💾 Commit your changes and push
🔁 Open a Pull Request describing your changes



Please include tests and update the README if you add or change features.




⚠️ Notes


This repo includes db.sqlite3 for development convenience. Remove or replace it before deploying to production or publishing sensitive data.
Update ALLOWED_HOSTS and DEBUG=False before going live.



📄 License

This project is for educational / portfolio purposes. Add an MIT or other license file if you plan to open-source it.



👤 Author

Ranjeet — BCA Graduate | Aspiring Python/Django Backend Developer

🔗 Portfolio: add link  |  💼 LinkedIn: add link  |  💻 GitHub: add link

