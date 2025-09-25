import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from difflib import get_close_matches

# Load dataset
df = pd.read_csv("dreamweaver_ai_100.csv")

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    # Try exact or partial keyword match
    for _, row in df.iterrows():
        if user_input in row['description'].lower() or user_input in row['name'].lower():
            return f"✨ {row['name']} ({row['category']})\n{row['description']}\n🔗 Website: {row['website']}"

    # If not found, try fuzzy matching on descriptions
    descriptions = df['description'].str.lower().tolist()
    matches = get_close_matches(user_input, descriptions, n=1, cutoff=0.3)

    if matches:
        matched_row = df[df['description'].str.lower() == matches[0]].iloc[0]
        return f"✨ {matched_row['name']} ({matched_row['category']})\n{matched_row['description']}\n🔗 Website: {matched_row['website']}"

    return "😴 Sorry, I couldn’t find a matching DreamWeaver AI tool."

# Function to handle sending a message
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    response = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    entry.delete(0, tk.END)

# Tkinter GUI
root = tk.Tk()
root.title("DreamWeaver AI Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_window.pack(padx=10, pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
