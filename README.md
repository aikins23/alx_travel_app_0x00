

# 🐍 ALX Backend Python  

Welcome to **ALX Backend Python** — a collection of hands-on projects designed to strengthen your backend development skills using **Python**.  
This repository focuses on **generators**, **database querying**, **memory-efficient programming**, and **API integration** — all essential for building high-performance backend systems.  

---

## 📂 Project Structure  

### `python-generators-0x00`  
> Learn to build **memory-efficient Python programs** using **generators**.

Key concepts covered:  
- **Batch Processing** → Stream database rows in chunks using generator functions.  
- **Lazy Pagination** → Fetch paginated results **only when needed**.  
- **Memory-Efficient Aggregation** → Calculate aggregates (e.g., average age) without loading entire datasets into memory.  

---

## 🚀 Learning Objectives  

By the end of this repository, you will be able to:  
- Write **Python generator functions** using `yield`.  
- Apply **lazy evaluation** techniques to handle large datasets.  
- Implement **batch processing** for database queries.  
- Design **paginated data loaders** that fetch on-demand.  
- Perform **efficient aggregations** without using heavy SQL functions like `AVG()`.

---

## 🛠️ Tech Stack  

- **Language:** Python `3.8+`  
- **Database:** MySQL (with `user_data` table)  
- **Environment:** Ubuntu 20.04 LTS / macOS / Windows  
- **Tools:** Virtualenv, Pip, MySQL Client  

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your-username>/alx-backend-python.git
cd alx-backend-python
```

### 2️⃣ Create a Virtual Environment  
```bash
python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install Dependencies  
=======
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

>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
```bash
pip install -r requirements.txt
```


### 4️⃣ Setup the MySQL Database  

#### Create Database  
```sql
CREATE DATABASE alx_backend;
USE alx_backend;
```

#### Create `user_data` Table  
```sql
CREATE TABLE user_data (
    user_id CHAR(36) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
```

#### Insert Sample Data  
```sql
INSERT INTO user_data (user_id, name, email, age) VALUES
(UUID(), 'John Doe', 'john@example.com', 25),
(UUID(), 'Jane Smith', 'jane@example.com', 32),
(UUID(), 'Sam Wilson', 'sam@example.com', 41);
```

---

## 📖 Usage  

Navigate to the project directory and run tasks:  

```bash
cd python-generators-0x00
python3 3-main.py
=======
### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Seeder

```bash
python manage.py seed
>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
```

---


## ✅ Example Outputs  

### **Batch Processing**  
```text
{'user_id': '00af05c9...', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 22}
```

### **Average Age Calculation**  
```text
Average age of users: 54.78
=======
## 📊 Example Usage

Start the development server:

```bash
python manage.py runserver
```

Check available listings (example API endpoint if DRF views are added):

```
GET /api/listings/
>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
```

---


## 🧩 Folder Structure  

```
alx-backend-python/
│── python-generators-0x00/
│   ├── 0-main.py
│   ├── 1-main.py
│   ├── 2-main.py
│   ├── 3-main.py
│   └── README.md
│── README.md
=======
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
>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
```

---


=======


>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
## 👨🏽‍💻 Author  

This repository is maintained as part of the **ALX Software Engineering Program**.  


- **GitHub:** [aikins](https://github.com/aikins)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

---

💡 *Keep learning, keep building — one generator at a time!*  
=======
- **GitHub:** [aikins](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

```

---
```
>>>>>>> fa0792f2e0588974308d84ed9c14784553a88fdf
