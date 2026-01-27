import json
import os

File_Name = "students.json"

def load_date():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(File_Name, "w") as f:
        json.dump(data, f, indent=4)

def add_student(data):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    data[roll] = {"name": name, "marks": marks}
    save_data(data)
    print("✅ Student added successfully!")

def view_students(data):
    if not data:
        print("No student found.")
        return
    
    for roll, info in data.items():
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

def search_student(data):
    roll = input("Enter Roll No to search: ")
    if roll in data:
        print(data[roll])
    else:
        print("❌ Student not found.")

def delete_student(data):
    roll = input("Enter Roll No to delete: ")
    if roll in data:
        del data[roll]
        save_data(data)
        print("🗑 Student deleted.")
    else:
        print("❌ Student not found.")

def menu():
    data = load_date()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

menu()








