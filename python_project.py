import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
import numpy as np

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Load and set background image
        self.bg_image = tk.PhotoImage(file='.vscode/python/P_project_folder/money.png')
        self.background_label = tk.Label(root, image=self.bg_image,bg="dark sea green")
        self.background_label.place(relwidth=1, relheight=1)

        # Add a title
        self.title = Label(root, text="Expense Tracker", font=("Helvetica", 45, "bold"),bg="dark sea green")
        self.title.pack(pady=20)

        # Data storage
        self.expenses = {}

        # Frame for input fields
        self.input_frame = Frame(root, bg='white', padx=10, pady=10)
        self.input_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Input fields
        self.label_name = Label(self.input_frame, text="Expense Name:", bg='light blue')
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = Entry(self.input_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_amount = Label(self.input_frame, text="Amount (in ₹):", bg='light blue')
        self.label_amount.grid(row=1, column=0, padx=5, pady=5)

        self.entry_amount = Entry(self.input_frame)
        self.entry_amount.grid(row=1, column=1, padx=5, pady=5)

        # Date Entry
        self.label_date = Label(self.input_frame, text="Date:", bg='light blue')
        self.label_date.grid(row=2, column=0, padx=5, pady=5)

        self.date_entry = DateEntry(self.input_frame, width=12, foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button frame
        self.button_frame = Frame(root, bg='white', padx=10, pady=10)
        self.button_frame.place(relx=0.5, rely=0.7, anchor="center")

        # Buttons
        self.button_add = Button(self.button_frame, text="Add Expense", command=self.add_expense, bg='light blue')
        self.button_add.grid(row=0, column=0, padx=10, pady=10)

        self.button_visualize = Button(self.button_frame, text="Visualize Expenses", command=self.visualize_expenses, bg='light blue')
        self.button_visualize.grid(row=0, column=1, padx=10, pady=10)

        self.button_view_all = Button(self.button_frame, text="View All Expenses", command=self.view_all_expenses, bg='light blue')
        self.button_view_all.grid(row=0, column=2, padx=10, pady=10)

        self.button_clear = Button(self.button_frame, text="Clear All Expenses", command=self.clear_all_expenses, bg='red')
        self.button_clear.grid(row=0, column=3, padx=10, pady=10)

    def add_expense(self):
        name = self.entry_name.get()
        amount = self.entry_amount.get()
        date = self.date_entry.get()

        if name and amount:
            try:
                amount = float(amount)
                if amount < 0:
                    raise ValueError("Negative value")

                key = f"{name} on {date}"
                if key in self.expenses:
                    self.expenses[key] += amount
                else:
                    self.expenses[key] = amount

                self.entry_name.delete(0, END)
                self.entry_amount.delete(0, END)
                messagebox.showinfo("Success", "Expense added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def visualize_expenses(self):
        if not self.expenses:
            messagebox.showwarning("Warning", "No expenses to visualize.")
            return

        names = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        # Create explode array to highlight the largest slice
        explode = [0.1] * len(names)
        max_index = amounts.index(max(amounts))
        explode[max_index] = 0.2

        plt.figure(figsize=(8, 6))
        wedges, texts, autotexts = plt.pie(
            amounts,
            labels=names,
            autopct='%1.1f%%',
            startangle=140,
            explode=explode,
            shadow=True,
            colors=plt.cm.Paired(np.arange(len(names)))
        )

        # Add legend
        plt.legend(wedges, names, title="Expenses")

        # Improve appearance
        plt.setp(autotexts, size=10, weight="bold", color="white")
        plt.title("Expense Distribution")
        plt.axis('equal')
        plt.show()

    def view_all_expenses(self):
        if not self.expenses:
            messagebox.showinfo("No Expenses", "No expenses recorded yet.")
            return

        expenses_list = "\n".join(f"{name}: ₹{amount:.2f}" for name, amount in self.expenses.items())
        messagebox.showinfo("All Expenses", expenses_list)

    def clear_all_expenses(self):
        self.expenses.clear()
        messagebox.showinfo("Cleared", "All expenses have been cleared.")

class LoginPage:
    def __init__(self, a):
        self.a = a
        self.a.title("Login Page")
        self.a.geometry("1000x800")  # Set the login window size

        # Load and set background image
        self.bg_image = PhotoImage(file='.vscode/python/P_project_folder/expense_project.png')
        self.background_label = tk.Label(a, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Create the login frame
        self.login_frame = tk.Frame(a, bg='light blue', padx=10, pady=10)
        self.login_frame.grid(row=0, column=0, padx=20, pady=50)

        # Configure grid weights for centering
        a.grid_rowconfigure(0, weight=1)
        a.grid_columnconfigure(0, weight=1)

        # Add widgets to the frame as needed
        self.label_username = Label(self.login_frame, text="Username:", bg='light blue')
        self.label_username.grid(row=0, column=0, padx=5, pady=5)

        self.entry_username = Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        # Password label and entry
        self.label_password = Label(self.login_frame, text="Password:", bg='light blue')
        self.label_password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_password = Entry(self.login_frame, show='*')
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Login button
        self.button_login = Button(self.login_frame, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "lavisha" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome to the Expense Tracker!")
            self.a.destroy()  # Close the login window
            self.open_expense_tracker()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_expense_tracker(self):
        root = Tk()
        app = ExpenseTracker(root)
        root.geometry("600x500")  # width x height
        root.minsize(400, 300)
        root.config(bg="dark sea green")
        root.mainloop()

if __name__ == "__main__":
    login_root = Tk()
    login_app = LoginPage(login_root)
    login_root.geometry("500x300")  # width x height
    login_root.mainloop()
