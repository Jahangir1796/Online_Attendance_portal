Student Attendance Portal
This project is a simple yet effective Student Attendance Portal developed using Python and MySQL. It provides a graphical user interface (GUI) for marking student attendance based on their roll numbers. The application includes error handling for database connectivity issues and input validation to ensure smooth operation.

Features:
Graphical User Interface (GUI): Built with Tkinter, offering an intuitive interface for users to input roll numbers.
Database Integration: Utilizes MySQL to store student information and attendance records.
Roll Number Validation: Validates roll numbers within a specified range to ensure accuracy.
Attendance Marking: Marks attendance in the database with timestamps upon successful validation.
Error Handling: Provides error messages for invalid roll numbers and database connectivity issues.
Sample Data: Includes sample data for populating the "student" table in the database.
Usage:
Ensure Python and MySQL are installed on your system.
Execute the provided SQL script to set up the database tables and insert sample data.
Run the StudentAttendancePortal.py script to launch the application.
Enter the student's roll number and click "Mark Attendance" to record attendance.
Database Schema:
student Table:
roll_number (Primary Key): Integer representing the student's roll number.
name: VARCHAR field storing the student's name.
attendance Table:
id (Primary Key): Auto-incremented integer serving as the unique identifier for each attendance record.
roll_number: VARCHAR field storing the student's roll number.
timestamp: TIMESTAMP field recording the date and time of attendance.
Dependencies:
Python 3.x
MySQL Connector Python (mysql-connector-python)
Contributing:
Contributions are welcome! Feel free to submit issues or pull requests for any enhancements or bug fixes.
