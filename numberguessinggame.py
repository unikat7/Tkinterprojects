import tkinter as tk
import random

window = tk.Tk()
window.title("🔢 Number Guessing Game")
window.geometry("400x320")
window.config(bg="#e8f4f8")

secret = random.randint(1, 20)
attempts = 0

def check_guess():
    global secret, attempts
    guess = entry.get()
    if not guess.isdigit():
        label.config(text="Please type a number! 😊", fg="red")
        return
    guess = int(guess)
    attempts += 1
    remaining = 3 - attempts
    if guess == secret:
        label.config(text=f"🎉 Correct! It was {secret}!\nYou got it in {attempts} attempt(s)!", fg="green")
        button.config(state="disabled")
    elif attempts >= 3:
        label.config(text=f"😢 Game Over! The number was {secret}!\nNo more chances!", fg="red")
        button.config(state="disabled")
    elif guess < secret:
        label.config(text=f"Too Low! 🔽 Try higher!\n{remaining} chance(s) left!", fg="blue")
    else:
        label.config(text=f"Too High! 🔼 Try lower!\n{remaining} chance(s) left!", fg="orange")
    entry.delete(0, tk.END)

def play_again():
    global secret, attempts
    secret = random.randint(1, 20)
    attempts = 0
    label.config(text="I picked a number! Start guessing 😄", fg="#333")
    button.config(state="normal")
    entry.delete(0, tk.END)

tk.Label(window, text="🔢 Guess My Number!", font=("Arial", 18, "bold"), bg="#e8f4f8").pack(pady=15)
tk.Label(window, text="I'm thinking of a number between 1 and 20", font=("Arial", 11), bg="#e8f4f8", fg="#555").pack()

entry = tk.Entry(window, font=("Arial", 16), width=8, justify="center")
entry.pack(pady=12)

button = tk.Button(window, text="Guess! 🎯", font=("Arial", 13, "bold"),
                   bg="#4CAF50", fg="white", padx=15, pady=8, command=check_guess)
button.pack()

label = tk.Label(window, text="I picked a number! Start guessing 😄",
                 font=("Arial", 13, "bold"), bg="#e8f4f8", fg="#333", wraplength=350)
label.pack(pady=15)

tk.Button(window, text="Play Again 🔄", font=("Arial", 11),
          bg="white", padx=10, pady=5, command=play_again).pack()

window.mainloop()