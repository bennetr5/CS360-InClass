import tkinter as tkinter
import profilepg as profile
import os
import json 

class note:
    def __init__(self, title, content, noteId, user):
        self.title = title
        self.content = content
        self.noteId = noteId
        self.user = user

    def save(self):
        directory = "./contents"
        fileName = str(self.title) + ".json"
        fullPath = os.path.join(directory, fileName)
        data = {
            "content": self.content
        }
        with open(fullPath, 'w', encoding='utf=8') as json_file:
            json.dump(data, json_file, indent=4)
    
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