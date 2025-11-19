import tkinter

class Profile:
    def __init__(self, username, email, courses):
        self.username = username
        self.email = email
        self.courses = courses

    def update_email(self, new_email):
        self.email = new_email

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)