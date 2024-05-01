import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

# Abstract class representing an Item in the library
class LibraryItem:
    def __init__(self, title, author):
        self.title = title  # Attribute: Title
        self.author = author  # Attribute: Author

    # Abstract method for checking availability
    def check_availability(self):
        pass

# Concrete class representing a Book
class Book(LibraryItem):  # Inheritance: Book inherits from LibraryItem
    def __init__(self, title, author, isbn, copies, book_type):
        super().__init__(title, author)  # Calling parent class constructor
        self.isbn = isbn  # Attribute: ISBN
        self.copies = copies  # Attribute: Copies
        self.book_type = book_type  # Attribute: Book Type

    # Method to check availability of the book
    def check_availability(self):
        return self.copies, self.copies > 0

# Class representing the GUI for the library management system
class LibraryManagementSystem:
    # Static list of books (Composition: LibraryManagementSystem has a list of books)
    books = [
        Book("The Night Circus", "Erin Morgenstern", "0000000001", 3, "Fiction"),
        Book("B", "A", "0000000001", 3, "Fiction"),
        Book("To Kill a Mockingbird", "Harper Lee", "0000000002", 5, "Novel"),
        Book("Dune", "Frank Herbert", "0000000003", 2, "Science Fiction"),
        Book("Steve Jobs", " Walter Isaacson", "0000000004", 0, "Biography"),
        Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "0000000001", 3, "Fiction"),
        Book("1984", "George Orwell", "0000000002", 5, "Novel"),
        Book("Neuromancer", " William Gibson", "0000000003", 2, "Science Fiction"),
        Book("The Diary of a Young Girl", "Anne Frank", "0000000004", 0, "Biography")
    ]

    # Static method to create and return a library item instance based on user input (Polymorphism)
    @staticmethod
    def create_library_item(title, author, book_type):
        title = title.lower()
        author = author.lower()
        book_type = book_type.lower()
        book = next((b for b in LibraryManagementSystem.books if b.title.lower() == title and b.author.lower() == author and b.book_type.lower() == book_type), None)
        return book

    # Static method to check and display the availability of the selected item
    @staticmethod
    def check_availability(title, author, book_type):
        item = LibraryManagementSystem.create_library_item(title, author, book_type)
        if item:
            copies, is_available = item.check_availability()
            if is_available:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                messagebox.showinfo("Availability", f"The book '{item.title}' by {item.author} is available.\nTotal copies available: {copies}\nCurrent time: {current_time}")
            else:
                messagebox.showwarning("Availability", f"The book '{item.title}' by {item.author} is not available.")
        else:
            messagebox.showerror("Error", "Book not found.")

    # Constructor for the GUI
    def __init__(self, root):
        self.root = root  # Attribute: Root window
        self.root.title("Login")
        self.root.geometry("300x300")
        self.root.resizable(True, True)

        self.root.config(bg='#93B1A6')  # Background color

        self.login_frame = tk.Frame(self.root, bg='#93B1A6')
        self.login_frame.pack(pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:", bg='#93B1A6', fg='black', font=('Arial', 12, 'bold'))
        self.username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", bg='#93B1A6', fg='black', font=('Arial', 12, 'bold'))
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.regex_label = tk.Label(self.login_frame, text="Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character.", wraplength=280, justify='left', bg='#93B1A6', fg='black', font=('Arial', 10))
        self.regex_label.grid(row=2, columnspan=2, padx=5, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.authenticate, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.login_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Library management system window
        self.library_system_window = None

    # Method to authenticate the user
    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Example of password validation using regular expression
        if username == "admin" and re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()\-_=+{};:,<.>])(?!.*\s).{8,}$', password):
            messagebox.showinfo("Login", "Login Successful!")
            self.root.destroy()  # Close the login window
            self.create_main_window()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    # Method to create the main library management window
    def create_main_window(self):
        self.library_system_window = tk.Tk()
        self.library_system_window.title("Library Management System")
        self.library_system_window.state('zoomed')

        self.library_system_window.config(bg='#93B1A6')  # Background color

        self.item_frame = tk.Frame(self.library_system_window, bg='#93B1A6')
        self.item_frame.pack(pady=20)

        # Labels and Entry widgets for user input
        self.title_label = tk.Label(self.item_frame, text="Title:", bg='#93B1A6', fg='black', font=('Arial', 12, 'bold'))
        self.title_label.grid(row=0, column=0, padx=5, pady=5)

        self.title_entry = tk.Entry(self.item_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.author_label = tk.Label(self.item_frame, text="Author:", bg='#93B1A6', fg='black', font=('Arial', 12, 'bold'))
        self.author_label.grid(row=1, column=0, padx=5, pady=5)

        self.author_entry = tk.Entry(self.item_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        self.book_type_label = tk.Label(self.item_frame, text="Book Type:", bg='#93B1A6', fg='black', font=('Arial', 12, 'bold'))
        self.book_type_label.grid(row=2, column=0, padx=5, pady=5)

        self.book_type_var = tk.StringVar()
        self.book_type_var.set("Fiction")

        self.book_type_dropdown = tk.OptionMenu(self.item_frame, self.book_type_var, "Fiction", "Novel", "Science Fiction", "Biography")
        self.book_type_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Button to check availability
        self.check_availability_button = tk.Button(self.library_system_window, text="Check Availability", command=self.check_availability, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.check_availability_button.pack(pady=10)

    # Method to create a library item instance based on user input
    def create_library_item(self):
        title = self.title_entry.get().lower()  # Convert input title to lowercase
        author = self.author_entry.get().lower()  # Convert input author to lowercase
        book_type = self.book_type_var.get().lower()  # Convert input book type to lowercase
        book = next((b for b in self.books if b.title.lower() == title and b.author.lower() == author and b.book_type.lower() == book_type), None)
        return book

    # Method to check and display the availability of the selected item
    def check_availability(self):
        item = self.create_library_item()
        if item:
            copies, is_available = item.check_availability()
            if is_available:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                messagebox.showinfo("Availability", f"The book '{item.title}' by {item.author} is available.\nTotal copies available: {copies}\nCurrent time: {current_time}")
            else:
                messagebox.showwarning("Availability", f"The book '{item.title}' by {item.author} is not available.")
        else:
            messagebox.showerror("Error", "Book not found.")


if __name__ == "__main__":
    root = tk.Tk()
    library_management_system = LibraryManagementSystem(root)
    root.mainloop()
