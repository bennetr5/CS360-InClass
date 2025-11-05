import tkinter as tkinter


class note:
    def __init__(self, title, content, id, user):
        self.title = title
        self.content = content
        self.id = id
        self.user = user

    def save():
        # TO-DO Save Notes
        return "No Functionality"
    
    # Getters and Setter
    def getTitle(self):
        return self.title
    
    def setTitle(self, t):
        self.title = t
    
    def getContent(self):
        return self.content
    
    def setContent(self, c):
        self.content = c

    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id

    def getUser(self):
        return self.user
    
    def setUser(self, user):
        self.user = user

root = tkinter.Tk()
root.title("My Tkinter App")
root.geometry("400x300")

label = tkinter.Label(root, text="Hello world!")
label.pack()

root.mainloop()