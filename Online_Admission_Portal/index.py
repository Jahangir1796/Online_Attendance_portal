
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("800x600")  # Set window size

        # Connect to MySQL server
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mysql123@#$",
                database="fitness_tracker"
            )
            messagebox.showinfo("Info", "Connected to MySQL server successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to connect to MySQL server: {error}")
            self.root.destroy()
            return

        # Apply styles
        self.set_styles()

        # Create widgets
        self.create_widgets()

        # Bind close event to close_connection method
        self.root.protocol("WM_DELETE_WINDOW", self.close_connection)

    def set_styles(self):
        # Define custom styles
        self.root.tk_setPalette(background="#f0f0f0")  # Set background color
        self.root.option_add("*Font", "Helvetica 12")  # Set default font
        self.root.option_add("*Button.Background", "#4CAF50")  # Set button background color
        self.root.option_add("*Button.Foreground", "#ffffff")  # Set button text color
        self.root.option_add("*Button.ActiveBackground", "#45a049")  # Set button background color when active
        self.root.option_add("*Button.ActiveForeground", "#ffffff")  # Set button text color when active
        self.root.option_add("*Label.Background", "#f0f0f0")  # Set label background color
        self.root.option_add("*Label.Foreground", "#333333")  # Set label text color
        self.root.option_add("*Entry.Background", "#ffffff")  # Set entry background color
        self.root.option_add("*Entry.Foreground", "#333333")  # Set entry text color
        self.root.option_add("*Text.Background", "#ffffff")  # Set text widget background color
        self.root.option_add("*Text.Foreground", "#333333")  # Set text widget text color
        self.root.option_add("*Text.Font", "Helvetica 11")  # Set text widget font

    def create_widgets(self):
        # Load background image
        bg_image = Image.open("gym.jpg")  # Path to your image
        bg_image = bg_image.resize((800, 600))  # Resize image to fit window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Create background label to display image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="white", bd=5)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

        # Label for title
        self.label = tk.Label(self.main_frame, text="Welcome to Fitness Tracker", bg="white")
        self.label.pack(pady=10)

        # Entry for exercise name
        self.exercise_name_label = tk.Label(self.main_frame, text="Exercise Name:", bg="white")
        self.exercise_name_label.pack()
        self.exercise_name_entry = tk.Entry(self.main_frame)
        self.exercise_name_entry.pack()

        # Entry for exercise duration
        self.exercise_duration_label = tk.Label(self.main_frame, text="Duration (minutes):", bg="white")
        self.exercise_duration_label.pack()
        self.exercise_duration_entry = tk.Entry(self.main_frame)
        self.exercise_duration_entry.pack()

        # Entry for exercise description
        self.exercise_description_label = tk.Label(self.main_frame, text="Description:", bg="white")
        self.exercise_description_label.pack()
        self.exercise_description_entry = tk.Entry(self.main_frame)
        self.exercise_description_entry.pack()

        # Entry for exercise category
        self.exercise_category_label = tk.Label(self.main_frame, text="Category:", bg="white")
        self.exercise_category_label.pack()
        self.exercise_category_entry = tk.Entry(self.main_frame)
        self.exercise_category_entry.pack()

        # Entry for calories burned
        self.calories_burned_label = tk.Label(self.main_frame, text="Calories Burned:", bg="white")
        self.calories_burned_label.pack()
        self.calories_burned_entry = tk.Entry(self.main_frame)
        self.calories_burned_entry.pack()

        # Add Exercise button
        self.add_button = tk.Button(self.main_frame, text="Add Exercise", command=self.add_exercise)
        self.add_button.pack(pady=10)

        # Text widget to display exercises
        self.exercises_text = tk.Text(self.main_frame, height=10, width=80, bg="white")
        self.exercises_text.pack()

        # Display placeholder text
        self.placeholder_text = "No exercises added yet."
        self.exercises_text.insert(tk.END, self.placeholder_text)

    def add_exercise(self):
        exercise_name = self.exercise_name_entry.get()
        exercise_duration = self.exercise_duration_entry.get()
        exercise_description = self.exercise_description_entry.get()
        exercise_category = self.exercise_category_entry.get()
        calories_burned = self.calories_burned_entry.get()

        if exercise_name and exercise_duration and exercise_description and exercise_category and calories_burned:
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO exercises(name, description, category, calories_burned, duration) VALUES (%s, %s, %s, %s, %s)"
                values = (exercise_name, exercise_description, exercise_category, calories_burned, exercise_duration)
                cursor.execute(sql, values)
                self.connection.commit()

                # Clear placeholder text if it's still there
                if self.exercises_text.get('1.0', 'end-1c') == self.placeholder_text:
                    self.exercises_text.delete('1.0', tk.END)

                # Add exercise details to the display
                exercise_info = f"Exercise Name: {exercise_name}\nDescription: {exercise_description}\nCategory: {exercise_category}\nCalories Burned: {calories_burned}\nDuration: {exercise_duration} minutes\n\n"
                self.exercises_text.insert(tk.END, exercise_info)

                # Clear entry fields
                self.clear_entry_fields()

                messagebox.showinfo("Info", "Exercise added successfully!")
            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Failed to add exercise: {error}")
        else:
            messagebox.showerror("Error", "Please enter values in all fields.")

    def clear_entry_fields(self):
        self.exercise_name_entry.delete(0, tk.END)
        self.exercise_duration_entry.delete(0, tk.END)
        self.exercise_description_entry.delete(0, tk.END)
        self.exercise_category_entry.delete(0, tk.END)
        self.calories_burned_entry.delete(0, tk.END)

    def close_connection(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
