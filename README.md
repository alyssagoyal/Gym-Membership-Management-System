# **Gym Membership Management System**

*A simple Python + MySQL project for managing gym member records.*

## 🚀 **Project Overview**

This is a console-based Gym Membership Management System developed using **Python** with **MySQL connectivity**.
It allows users to perform basic CRUD operations (Create, Read, Update, Delete) on gym member records.

This project is perfect for beginners exploring Python, MySQL, and database handling.

---

## 📌 **Features**

✔ Add new gym members
✔ View all member records in table format
✔ Search members by ID
✔ Update member details
✔ Delete member records
✔ Auto-creates the table if it does not exist
✔ Clean grid-style output using `tabulate`

---

## 🛠️ **Tech Stack**

* **Python**
* **MySQL**
* **mysql-connector-python** library
* **tabulate** library

---

## 📂 **Project Structure**

```
├── gym_management.py     # Main Python script (your code)
├── README.md             # Project documentation
```

---

## 💾 **Database Setup**

Before running the project, create a database in MySQL:

```sql
CREATE DATABASE gym_management;
```

The table will be auto-created when the program runs:

```sql
members(
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    membership_type VARCHAR(30),
    contact_no VARCHAR(15)
)
```

---

## ⚙️ **Installation Instructions**

### **1. Install Python Libraries**

Run the following commands:

```bash
pip install mysql-connector-python
pip install tabulate
```

### **2. Configure MySQL Connection**

In the script, replace this line with your MySQL password:

```python
password="your_password_here"
```

---

## ▶️ **How to Run the Program**

Open terminal or command prompt and run:

```bash
python gym_management.py
```

You will see the main menu:

```
1. Add New Member
2. View All Members
3. Search Member
4. Update Member Details
5. Delete Member
6. Exit
```

Just enter the corresponding number to perform any action.

---

## 📘 **Example Outputs**

### Viewing members:

```
+----+--------+-------+--------+------------------+-------------+
| ID | Name   | Age   | Gender | Membership Type  | Contact No  |
+----+--------+-------+--------+------------------+-------------+
| 1  | John   | 25    | Male   | Monthly          | 9876543210  |
+----+--------+-------+--------+------------------+-------------+
```

---

## 🎯 **Purpose of the Project**

This project demonstrates:

* Basic Python programming
* Database connectivity
* CRUD operations
* Menu-driven applications
* User input handling

It is suitable for school projects, beginners in Python, and students planning for CS portfolios.

---

## 📜 **Future Enhancements (Optional Ideas)**

* Add login system (Admin/User)
* Add payment tracking
* Add membership expiration reminders
* Create a GUI using Tkinter / PyQt
* Export data to CSV or Excel

---

## 🙌 **Author**

**Alyssa Goyal**
12th Grade (Graduating 2026)
Aspiring Computer Science Student

---

