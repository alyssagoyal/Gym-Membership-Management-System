# Gym Membership Management System
# Developed in Python with MySQL Connectivity

# Importing required modules
import mysql.connector
from tabulate import tabulate

# Establish connection to MySQL database
# Make sure you have created a database named 'gym_management' in MySQL before running
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password_here",   # replace with your MySQL password
    database="gym_management"
)

# Create cursor object to execute queries
cursor = conn.cursor()

# Function to create table if not exists
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members(
            member_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            gender VARCHAR(10),
            membership_type VARCHAR(30),
            contact_no VARCHAR(15)
        )
    """)
    conn.commit()

# Function to add a new member
def add_member():
    print("\n--- Add New Member ---")
    name = input("Enter Member Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female): ")
    membership_type = input("Enter Membership Type (Monthly/Quarterly/Yearly): ")
    contact_no = input("Enter Contact Number: ")
    query = "INSERT INTO members (name, age, gender, membership_type, contact_no) VALUES (%s, %s, %s, %s, %s)"
    data = (name, age, gender, membership_type, contact_no)
    cursor.execute(query, data)
    conn.commit()
    print("✅ Member added successfully!")

# Function to view all members
def view_members():
    print("\n--- Member Details ---")
    cursor.execute("SELECT * FROM members")
    records = cursor.fetchall()
    if records:
        print(tabulate(records, headers=["ID", "Name", "Age", "Gender", "Membership Type", "Contact No"], tablefmt="grid"))
    else:
        print("No records found.")

# Function to search member by ID
def search_member():
    print("\n--- Search Member ---")
    member_id = int(input("Enter Member ID: "))
    cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
    record = cursor.fetchone()
    if record:
        print(tabulate([record], headers=["ID", "Name", "Age", "Gender", "Membership Type", "Contact No"], tablefmt="grid"))
    else:
        print("No member found with that ID.")

# Function to update member details
def update_member():
    print("\n--- Update Member ---")
    member_id = int(input("Enter Member ID to update: "))
    print("1. Update Name\n2. Update Age\n3. Update Gender\n4. Update Membership Type\n5. Update Contact Number")
    choice = int(input("Enter choice: "))
    
    fields = ["name", "age", "gender", "membership_type", "contact_no"]
    if 1 <= choice <= 5:
        new_value = input("Enter new value: ")
        query = f"UPDATE members SET {fields[choice-1]} = %s WHERE member_id = %s"
        cursor.execute(query, (new_value, member_id))
        conn.commit()
        print("✅ Member details updated successfully!")
    else:
        print("❌ Invalid choice!")

# Function to delete member
def delete_member():
    print("\n--- Delete Member ---")
    member_id = int(input("Enter Member ID to delete: "))
    cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
    conn.commit()
    print("✅ Member deleted successfully!")

# Function to display main menu
def main_menu():
    create_table()
    while True:
        print("\n==============================")
        print("  GYM MEMBERSHIP MANAGEMENT  ")
        print("==============================")
        print("1. Add New Member")
        print("2. View All Members")
        print("3. Search Member")
        print("4. Update Member Details")
        print("5. Delete Member")
        print("6. Exit")
        print("==============================")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_member()
        elif choice == '2':
            view_members()
        elif choice == '3':
            search_member()
        elif choice == '4':
            update_member()
        elif choice == '5':
            delete_member()
        elif choice == '6':
            print("Exiting program... Thank you!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
    conn.close()
