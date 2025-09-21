# 🏝 ALX Travel App — Milestone 2

## 📌 Project Overview
This project is part of the **ALX Backend Python track**.  
In this milestone, we extend the `alx_travel_app` project by defining **database models**, creating **serializers** for API responses, and implementing a **database seeder** with Django management commands.

## 🎯 Learning Objectives
By the end of this milestone, you should be able to:
- Model relational data with **Django ORM**.
- Create **serializers** using Django REST Framework (DRF).
- Implement a custom **management command** to seed the database with sample data.
- Populate and test the database programmatically.

---

## 🏗 Features Implemented
### ✅ Models (`listings/models.py`)
- **Listing**: Represents a property available for booking.  
- **Booking**: Links a user to a listing with start/end dates.  
- **Review**: Allows users to leave ratings & comments for a listing.  

### ✅ Serializers (`listings/serializers.py`)
- **ListingSerializer**: Serializes listing data for APIs.  
- **BookingSerializer**: Serializes booking data for APIs.  

### ✅ Seeder Command (`listings/management/commands/seed.py`)
- Populates the database with sample listings.  
- Creates a demo user (`demo / password123`).  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/alx_travel_app_0x00.git
cd alx_travel_app_0x00/alx_travel_app
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Seeder

```bash
python manage.py seed
```

---

## 📊 Example Usage

Start the development server:

```bash
python manage.py runserver
```

Check available listings (example API endpoint if DRF views are added):

```
GET /api/listings/
```

---

## 📦 Requirements

* Python 3.10+
* Django 4.2+
* Django REST Framework 3.14+

---

## 🧪 Testing

Run Django shell to confirm seeded data:

```bash
python manage.py shell
>>> from listings.models import Listing
>>> Listing.objects.all()
```

---



## 👨🏽‍💻 Author  

This repository is maintained as part of the **ALX Software Engineering Program**.  

- **GitHub:** [aikins](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

```

---
```
