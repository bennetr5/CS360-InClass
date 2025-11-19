import tkinter as tk
import json
from json import JSONDecodeError

class Message(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Message App")
        self.geometry("350x300")
        self.messageFile = "messages.json"

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

    def loadMessages(self):
        try:
            with open(self.messageFile, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {k: (v if isinstance(v, list) else [v]) for k, v in data.items()}
        except (FileNotFoundError, JSONDecodeError):
            return {}

    def uploadMessages(self):
        with open(self.messageFile, "w", encoding="utf-8") as f:
            json.dump(self.messages, f, indent=2, ensure_ascii=False)

    def sendMsg(self):
        user = self.userEntry.get().strip()
        message = self.msgEntry.get().strip()
        if not user or not message:
            self.display_output("Please enter both a user and a message.")
            return

        self.messages.setdefault(user, []).append(message)
        self.uploadMessages()

        self.display_output(f"Message sent to {user}: {message}")
        self.msgEntry.delete(0, tk.END)

    def viewMessages(self):
        user = self.userEntry.get().strip()
        if not user:
            self.display_output("Please enter a username to view their messages.")
            return

        messages = self.messages.get(user)
        if not messages:
            self.display_output(f"No messages found for {user}.")
        else:
            display_text = f"Messages for {user}:\n" + "\n".join(f"- {m}" for m in messages)
            self.display_output(display_text)

    def display_output(self, text):
        self.outputBox.config(state="normal")
        self.outputBox.delete(1.0, tk.END)
        self.outputBox.insert(tk.END, text)
        self.outputBox.config(state="disabled")

if __name__ == "__main__":
    app = Message()
    app.mainloop()
