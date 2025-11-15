import tkinter as tk
import json
import os

class StudyGroupApp(tk.Tk):
    def __init__(self, json_file="studygroup.json"):
        super().__init__()

        self.json_file = json_file
        self.load_data()

        self.title("Study Group")
        self.geometry("500x500")

        self.create_session()
        self.update_user_list()

    def load_data(self):
        if not os.path.exists(self.json_file):
            self.description = ""
            self.users = []
            self.save_data()
        else:
            with open(self.json_file, "r") as f:
                data = json.load(f)
            self.description = data.get("description", "")
            self.users = data.get("users", [])

    def save_data(self):
        with open(self.json_file, "w") as f:
            json.dump({"description": self.description, "users": self.users}, f, indent=4)

    def add_user(self, name):
        if name and name not in self.users:
            self.users.append(name)
            self.save_data()
            self.update_user_list()

    def remove_user(self, name):
        if name in self.users:
            self.users.remove(name)
            self.save_data()
            self.update_user_list()

    def set_description(self, text):
        self.description = text
        self.save_data()

    def create_session(self):
        #description
        tk.Label(self, text="Group Description:").pack(pady=5)
        self.desc_box = tk.Text(self, height=4, width=35)
        self.desc_box.pack()
        self.desc_box.insert("1.0", self.description)
        tk.Button(self, text="Save Description", command=self.save_description).pack(pady=5)

        #Users
        tk.Label(self, text="Users:").pack(pady=5)
        self.user_listbox = tk.Listbox(self, width=35, height=6)
        self.user_listbox.pack()

        #adds user
        tk.Label(self, text="Add User:").pack(pady=5)
        self.add_entry = tk.Entry(self)
        self.add_entry.pack()
        tk.Button(self, text="+", command=lambda: (self.add_user(self.add_entry.get().strip()), self.add_entry.delete(0, tk.END))).pack(pady=5)

        #removes user
        tk.Label(self, text="Remove User:").pack(pady=5)
        self.remove_entry = tk.Entry(self)
        self.remove_entry.pack()
        tk.Button(self, text="-", command=lambda: (self.remove_user(self.remove_entry.get().strip()), self.remove_entry.delete(0, tk.END))).pack(pady=5)

    def save_description(self):
        self.set_description(self.desc_box.get("1.0", tk.END).strip())

    def update_user_list(self):
        self.user_listbox.delete(0, tk.END)
        for u in self.users:
            self.user_listbox.insert(tk.END, u)


if __name__ == "__main__":
    app = StudyGroupApp()
    app.mainloop()
