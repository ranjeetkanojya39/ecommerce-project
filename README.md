# 🛍️ E-Commerce Project

A full-featured e-commerce platform built with Python and Django, providing a seamless online shopping experience with modern frontend technologies.

**Live Demo:** [https://ecommerce-project-5-86b1.onrender.com](https://ecommerce-project-5-86b1.onrender.com)

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- 🏪 **Product Catalog** - Browse and search products with advanced filtering
- 🛒 **Shopping Cart** - Add/remove items and manage quantities
- 💳 **Secure Checkout** - Payment processing and order management
- 👤 **User Authentication** - Registration, login, and profile management
- 📦 **Order Tracking** - View order history and track shipments
- ⭐ **Product Reviews** - Rate and review purchased items
- 🔍 **Search & Filter** - Find products by category, price, rating, and more
- 📱 **Responsive Design** - Optimized for desktop, tablet, and mobile devices
- 🛡️ **Admin Dashboard** - Manage products, orders, and users
- 💰 **Inventory Management** - Stock tracking and low-inventory alerts

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Django - Web framework
- Django REST Framework - API development
- SQLite/PostgreSQL - Database

**Frontend:**
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap/Tailwind CSS (for styling)

**DevOps & Deployment:**
- Git & GitHub - Version control
- Render - Hosting platform
- Gunicorn - WSGI server

---

## 📁 Project Structure

```
ecommerce-project/
├── manage.py
├── requirements.txt
├── static/
│   ├── admin/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── accounts/
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── cart/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── orders/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── accounts/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── .env.example
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment tool (venv or virtualenv)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ranjeetkanojya39/ecommerce-project.git
   cd ecommerce-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create a `.env` file** (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```

2. **Update environment variables in `.env`:**
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Frontend: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

---

## 💻 Usage

### For Customers

1. **Browse Products** - Navigate to the home page or use the search bar
2. **Filter & Sort** - Use filters by category, price range, and ratings
3. **Add to Cart** - Click "Add to Cart" on any product
4. **Checkout** - Review cart and proceed to payment
5. **Track Orders** - View order status in your account dashboard

### For Administrators

1. **Login to Admin Panel** - http://localhost:8000/admin
2. **Manage Products** - Add, edit, or delete products
3. **View Orders** - Track all customer orders and update statuses
4. **Manage Users** - Monitor user accounts and permissions
5. **View Analytics** - Check sales reports and statistics

---

## 🔌 API Endpoints

### Products
- `GET /api/products/` - Get all products
- `GET /api/products/<id>/` - Get product details
- `POST /api/products/` - Create a new product (Admin only)
- `PUT /api/products/<id>/` - Update product (Admin only)
- `DELETE /api/products/<id>/` - Delete product (Admin only)

### Cart
- `GET /api/cart/` - View cart items
- `POST /api/cart/add/` - Add item to cart
- `POST /api/cart/remove/` - Remove item from cart
- `PUT /api/cart/update/` - Update cart item quantity

### Orders
- `GET /api/orders/` - Get user's orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/<id>/` - Get order details

### Accounts
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/user/profile/` - Get user profile
- `PUT /api/user/profile/` - Update user profile

---

## 🗄️ Database

The project uses Django's ORM with the following main models:

- **User** - User accounts and authentication
- **Product** - Product catalog and details
- **Category** - Product categories
- **Cart** - Shopping cart items
- **Order** - Customer orders
- **OrderItem** - Items in orders
- **Review** - Product reviews and ratings

---

## 🌐 Deployment

### Deploying to Render

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. **Connect to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Select the ecommerce-project repository

3. **Configure Environment:**
   - Set environment variables in Render dashboard:
     - `PYTHON_VERSION=3.9.16`
     - `DEBUG=False`
     - `SECRET_KEY=your_secret_key`
     - Database URL (if using PostgreSQL)

4. **Deploy:**
   - Set build command: `pip install -r requirements.txt && python manage.py migrate`
   - Set start command: `gunicorn ecommerce.wsgi`
   - Click "Create Web Service"

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guide for Python
- Use descriptive variable and function names
- Add comments for complex logic
- Write unit tests for new features

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📧 Contact & Support

For questions, issues, or suggestions:
- **GitHub Issues:** [Create an issue](https://github.com/ranjeetkanojya39/ecommerce-project/issues)
- **GitHub Discussions:** [Start a discussion](https://github.com/ranjeetkanojya39/ecommerce-project/discussions)

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Font Awesome](https://fontawesome.com) - Icons
- The open-source community for invaluable libraries and tools

---

**Happy Coding! 🚀**
