import tkinter as tk
import random

window = tk.Tk()
window.title("Who is More Likely Game")
window.geometry("450x500")
window.config(bg="#ffe6f0")

names = []

questions = [
    "Who is more likely to talk to their food before eating? 🍔🗣️",
    "Who is more likely to laugh at a serious moment? 🤣",
    "Who is more likely to say 'I am not hungry' and still eat? 😋",
    "Who is more likely to forget homework? 📚",
    "Who is more likely to say ‘I’m coming’ but never arrive? 🚶‍♂️😆",
    "Who is more likely to sleep in class? 😴",
    "Who is more likely to become a meme without trying? 😂",
    "Who is more likely to eat pizza every day? 🍕",
]

# Title
title = tk.Label(
    window,
    text="🎮 Who is More Likely?",
    font=("Arial", 20, "bold"),
    bg="#ffe6f0",
    fg="#ff3399"
)
title.pack(pady=15)

# Entry
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Result
result = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#ffe6f0",
    fg="#333333",
    wraplength=400,
    justify="center"
)
result.pack(pady=20)

# Add player
def add_name():
    name = entry.get().strip()

    if name == "":
        result.config(text="⚠ Enter a valid name!", fg="red")
        return

    if name in names:
        result.config(text="⚠ Name already added!", fg="orange")
        return

    names.append(name)
    entry.delete(0, tk.END)

    result.config(text="✅ Added: " + name, fg="green")

# Play game
def play_game():
    if len(names) < 2:
        result.config(text="⚠ Add at least 2 players!", fg="red")
        return

    question = random.choice(questions)

    p1 = random.choice(names)
    p2 = random.choice(names)

    while p1 == p2:
        p2 = random.choice(names)

    winner = random.choice([p1, p2])

    result.config(
        text=f"{question}\n\n🎉 Winner: {winner} 😂 hahaha",
        fg="#6a0dad"
    )

# Buttons
tk.Button(
    window,
    text="➕ Add Player",
    command=add_name,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18
).pack(pady=5)

tk.Button(
    window,
    text="🎲 Play Game",
    command=play_game,
    font=("Arial", 12, "bold"),
    bg="#ff6600",
    fg="white",
    width=18
).pack(pady=5)

window.mainloop()