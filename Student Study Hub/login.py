import tkinter as tk
from tkinter import messagebox
import json

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login System")
        self.geometry("300x150")

        # Path for the credentials file
        self.credentials_file = "credentials.json"
        self.load_credentials()

        self.create_widgets()

    def load_credentials(self):
        try:
            with open(self.credentials_file, 'r') as f:
                self.credentials = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty/corrupt, start with default
            self.credentials = {"admin": "123"}
            self.save_credentials()

    def save_credentials(self):
        with open(self.credentials_file, 'w') as f:
            json.dump(self.credentials, f, indent=4)

    def create_widgets(self):
        # Username
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        self.login_button = tk.Button(self, text="Login", command=self.attempt_login)
        self.login_button.grid(row=2, column=1, padx=5, pady=10, sticky="w")

        # Sign Up Button
        self.signup_button = tk.Button(self, text="Sign Up", command=self.open_signup_window)
        self.signup_button.grid(row=2, column=0, padx=5, pady=10, sticky="e")

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.credentials.get(username) == password:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.destroy()  # Close the login window on success
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_signup_window(self):
        self.signup_window = tk.Toplevel(self)
        self.signup_window.title("Create New Account")
        self.signup_window.geometry("300x180")

        # New Username
        tk.Label(self.signup_window, text="New Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.new_username_entry = tk.Entry(self.signup_window)
        self.new_username_entry.grid(row=0, column=1, padx=10, pady=10)

        # New Password
        tk.Label(self.signup_window, text="New Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.new_password_entry = tk.Entry(self.signup_window, show="*")
        self.new_password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Confirm Password
        tk.Label(self.signup_window, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.confirm_password_entry = tk.Entry(self.signup_window, show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create Account Button
        tk.Button(self.signup_window, text="Create Account", command=self.create_account).grid(row=3, column=0, columnspan=2, pady=10)

    def create_account(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not new_username or not new_password:
            messagebox.showerror("Error", "Username and password cannot be empty.", parent=self.signup_window)
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.", parent=self.signup_window)
            return

        if new_username in self.credentials:
            messagebox.showerror("Error", "Username already exists.", parent=self.signup_window)
            return

        self.credentials[new_username] = new_password
        self.save_credentials()
        messagebox.showinfo("Success", "Account created successfully!", parent=self.signup_window)
        self.signup_window.destroy()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
