import tkinter as tk
import json
from json import JSONDecodeError

MESSAGE_FILE = "messages.json"
WINDOW_TITLE = "Message App"
WINDOW_SIZE = "350x300"


class Message(tk.Tk):
    # Simple Tkinter app for sending and viewing text messages stored in a JSON file.

    def __init__(self) -> None:
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        self.messageFile = MESSAGE_FILE
        self.messages = self.loadMessages()

        self.userLabel = tk.Label(self, text="Send message to:")
        self.userLabel.pack(pady=5)

        self.userEntry = tk.Entry(self)
        self.userEntry.pack(pady=5)

        self.msgLabel = tk.Label(self, text="Enter message:")
        self.msgLabel.pack(pady=5)

        self.msgEntry = tk.Entry(self)
        self.msgEntry.pack(pady=5)

        self.sendButton = tk.Button(self, text="Send Message", command=self.sendMsg)
        self.sendButton.pack(pady=5)

        self.viewButton = tk.Button(self, text="View Messages", command=self.viewMessages)
        self.viewButton.pack(pady=5)

        self.outputBox = tk.Text(self, height=6, width=40, state="disabled", wrap="word")
        self.outputBox.pack(pady=10)
    
    def getMessages(self):
        try:
            with open(self.messageFile, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {k: (v if isinstance(v, list) else [v]) for k, v in data.items()}
        except (FileNotFoundError, JSONDecodeError):
            return {}

    def saveMessages(self):
        with open(self.messageFile, "w", encoding="utf-8") as f:
            json.dump(self.messages, f, indent=2, ensure_ascii=False)

    def validateUsernameAndMessages(self, username, messages):
        if not username:
            self.dislplayOutput("Please enter a username.")
            return False
        if not messages:
            self.dislplayOutput(f"No messages found for {username}.")
            return False
        return True

    def sendMsg(self):
        user = self.userEntry.get().strip()
        messages = self.msgEntry.get().strip()
        if self.validateUsernameAndMessages(user, messages):
            self.messages.setdefault(user, []).append(messages)
            self.uploadMessages()

            self.dislplayOutput(f"Message sent to {user}: {messages}")
            self.msgEntry.delete(0, tk.END)
    
    def viewMessages(self):
        user = self.userEntry.get().strip()
        messages = self.messages.get(user)
        if self.validateUsernameAndMessages(user, messages):
            displayText = f"Messages for {user}:\n" + "\n".join(f"- {m}" for m in messages)
            self.dislplayOutput(displayText)
    

    def _displayOutput(self, text):
        self.outputBox.config(state="normal")
        self.outputBox.delete(1.0, tk.END)
        self.outputBox.insert(tk.END, text)
        self.outputBox.config(state="disabled")

if __name__ == "__main__":
    app = Message()
    app.mainloop()
