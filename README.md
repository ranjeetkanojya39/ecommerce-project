# 🛒 GreatKart — Django E-Commerce Platform

A full-stack e-commerce web application built with **Django**, featuring a complete shopping experience including product browsing, cart management, checkout, order processing, user authentication, and an admin dashboard.

🌐 **Live Demo:** https://ecommerce-project-5-86b1.onrender.com

---

# 📖 Project Overview

GreatKart is a modular Django-based e-commerce platform developed to demonstrate a complete online shopping workflow. The project follows Django's app-based architecture, making it easy to maintain, extend, and scale.

> 📸 **Home Page Screenshot**
>
> ![Home Page](docs/screenshots/home.png)

---

# ✨ Features

* 🛍️ Product Catalog with Categories
* 🔍 Product Search
* 📄 Product Detail Page
* 🛒 Shopping Cart Management
* 💳 Checkout & Order Placement
* 👤 User Authentication (Register/Login)
* 📦 Order Management
* 🛠️ Django Admin Dashboard

## Feature Details

| Feature             | Description                                |
| ------------------- | ------------------------------------------ |
| 🛍️ Product Catalog | Browse products organized by categories    |
| 🔍 Search           | Search products using keywords             |
| 📄 Product Details  | Dedicated product detail page              |
| 🛒 Cart Management  | Add, update, and remove products from cart |
| 💳 Checkout         | Complete order placement process           |
| 👤 Authentication   | User registration and login                |
| 🛠️ Admin Panel     | Manage products, categories, and orders    |

### 📸 Product Listing

![Product Listing](docs/screenshots/product-list.png)

### 📸 Product Details

![Product Detail](docs/screenshots/product-detail.png)

### 📸 Shopping Cart

![Cart](docs/screenshots/cart.png)

### 📸 Checkout

![Checkout](docs/screenshots/checkout.png)

### 📸 Admin Dashboard *(Optional)*

![Admin Dashboard](docs/screenshots/admin.png)

---

# 🛠️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* SQLite (Development)
* Easily configurable for PostgreSQL or MySQL

### Tools

* Git
* GitHub
* Django Admin
* Render (Deployment)

---

# 📂 Project Structure

```text
greatkart/
│
├── accounts/                # User Authentication
├── cart/                    # Shopping Cart
├── category/                # Product Categories
├── store/                   # Product Management
├── orders/                  # Order Processing
├── search/                  # Search Functionality
├── greatkart_template/      # Templates
├── static/                  # Static Files
├── staticfiles/             # Collected Static Files
├── media/                   # Uploaded Images
├── docs/
│   └── screenshots/         # README Images
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Requirements

* Python 3.x
* pip
* Virtual Environment (Recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd greatkart
```

### 2. Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=your_database_url
```

Configure `settings.py` to load environment variables.

---

# 🗄️ Database & Migrations

Run migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

Create Superuser:

```bash
python manage.py createsuperuser
```

---

# 🎨 Static Files

Collect static files before deployment.

```bash
python manage.py collectstatic
```

Configure:

* STATIC_ROOT
* STATICFILES_DIRS
* MEDIA_ROOT
* MEDIA_URL

for production deployment.

---

# ▶️ Run the Project

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

# 🧪 Running Tests

```bash
python manage.py test
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

Please include tests and update the documentation when applicable.

---

# ⚠️ Notes

* This project includes `db.sqlite3` for development purposes.
* Do not use the development database in production.
* Set `DEBUG=False` before deployment.
* Update `ALLOWED_HOSTS` for your production domain.

---

# 📄 License

This project is intended for educational and portfolio purposes.

You may add the **MIT License** if you plan to make it open source.

---

# 👨‍💻 Author

**Ranjeet Kanojiya**

🎓 BCA Graduate

💻 Aspiring Python & Django Backend Developer

### Connect With Me

* 🌐 Portfolio: *Add Portfolio Link*
* 💼 LinkedIn: *Add LinkedIn Profile*
* 💻 GitHub: https://github.com/ranjeetkanojya39
