import csv
import os

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_students()  # Load data when program starts

    def save_student_to_csv(self, student):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student.roll_no, student.name, student.marks])

    def load_students(self):
        if not os.path.exists(self.filename):
            # Create file with headers if not exists
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Roll No", "Name", "Marks"])
        else:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row:  # Avoid empty rows
                        student = Student(row[0], row[1], row[2])
                        self.students.append(student)

    def save_all_students(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Marks"])
            for student in self.students:
                writer.writerow([student.roll_no, student.name, student.marks])

    def add_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        student = Student(roll_no, name, marks)
        self.students.append(student)
        self.save_student_to_csv(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found!")
        else:
            for student in self.students:
                print(student)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Student Found:", student)
                return
        print("Student not found.")

    def update_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter new name: ")
                student.marks = input("Enter new marks: ")
                self.save_all_students()  # Save updates
                print("Student updated successfully!")
                return
        print("Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.save_all_students()  # Save updates
                print("Student deleted successfully!")
                return
        print("Student not found.")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            roll_no = input("Enter Roll No to search: ")
            sms.search_student(roll_no)
        elif choice == '4':
            roll_no = input("Enter Roll No to update: ")
            sms.update_student(roll_no)
        elif choice == '5':
            roll_no = input("Enter Roll No to delete: ")
            sms.delete_student(roll_no)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
