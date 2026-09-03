# 🛒 E-Commerce Dashboard

A modern and user-friendly **E-Commerce Dashboard** built with Django for managing products, monitoring inventory, and viewing important business statistics from a centralized dashboard.

## ✨ Features

* 📊 Dashboard with business statistics
* 📦 Product management
* ➕ Add new products
* ✏️ Edit product details
* 🗑️ Delete products
* 🔍 Product search
* 🎯 Product filtering
* 📋 Stock status tracking
* 💰 Revenue analytics
* 🗂️ Category-wise revenue insights
* 🔐 CSRF protection
* ⚙️ Django Admin Panel
* 🗄️ SQLite database
* 🚀 Django ORM for database management

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **Django ORM**
* **HTML / CSS**
* **JavaScript**

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sumit-vish0/E-commerce-Dashboard-.git
cd E-commerce-Dashboard-
```

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database

This project uses **SQLite** as its database.

To use the existing product data, run:

```bash
python import_legacy_data.py
```

If you want to start with a fresh database, remove the existing database file and run:

```bash
python manage.py migrate
```

## ⚙️ Django Admin

Create an admin account using:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## 📊 Dashboard

The dashboard provides a quick overview of important e-commerce information such as:

* Total products
* Product stock
* Revenue
* Categories
* Stock availability
* Product performance

## 📌 Project Purpose

This project is designed to provide a simple and efficient platform for managing an e-commerce product inventory and monitoring essential business data through a clean dashboard interface.

## 👨‍💻 Author

**Sumit Vishwakarma**
