
import mysql.connector
import tkinter as tk
from tkinter import messagebox

class StudentAttendancePortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Portal")
        self.root.geometry("400x200")  # Set window size

        self.connection = self.connect_to_database()

        self.create_widgets()

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mysql123@#$",
                database="fitness_tracker"
            )
            return connection
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to connect to database: {error}")
            return None

    def get_student_name(self, roll_number):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT name FROM student WHERE roll_number = %s"
            cursor.execute(sql, (roll_number,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to retrieve student name: {error}")
            return None

    def create_widgets(self):
        # Add project heading
        project_heading = tk.Label(self.root, text="Student Attendance Portal", font=("Helvetica", 16, "bold"), pady=10)
        project_heading.pack()

        # Entry for roll number
        self.roll_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.roll_entry.pack(pady=10)

        # Button to mark attendance
        self.attendance_button = tk.Button(self.root, text="Mark Attendance", command=self.mark_attendance,
                                           font=("Helvetica", 12), bg="green", fg="white", padx=20)
        self.attendance_button.pack()

    def mark_attendance(self):
        roll_number = self.roll_entry.get()     
        if not roll_number:
            messagebox.showwarning("Warning", "Please enter your roll number!")
            return

        try:
            roll_number = int(roll_number)
            if roll_number < 1 or roll_number > 54:
                messagebox.showwarning("Warning", "Roll number should be between 1 and 54!")
                return

            student_name = self.get_student_name(roll_number)
            if student_name:
                cursor = self.connection.cursor()
                sql = "INSERT INTO attendance (roll_number, name) VALUES (%s, %s)"
                values = (roll_number, student_name)
                cursor.execute(sql, values)
                self.connection.commit()
                messagebox.showinfo("Success", f"Attendance marked successfully for {student_name}!")
            else:
                messagebox.showwarning("Warning", "No student found with this roll number!")
        except ValueError:
            messagebox.showwarning("Warning", "Invalid roll number format!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to mark attendance: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentAttendancePortal(root)
    root.mainloop()
