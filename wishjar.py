import tkinter as tk
import random

root = tk.Tk()
root.title("🫙 Wish Jar")
root.geometry("400x500")
root.config(bg="#1a1a2e")

tk.Label(root, text="🫙 Wish Jar", font=("Georgia", 22, "bold"), bg="#1a1a2e", fg="#e2c878").pack(pady=15)

entry = tk.Entry(root, font=("Helvetica", 13), bg="#2d2d44", fg="white", insertbackground="white", relief="flat")
entry.pack(padx=20, fill="x", ipady=8)

listbox = tk.Listbox(root, font=("Helvetica", 12), bg="#16213e", fg="#c9d6ff", relief="flat", highlightthickness=0, selectbackground="#a29bfe")
listbox.pack(padx=20, pady=12, fill="both", expand=True)

magic = tk.Label(root, text="", font=("Georgia", 13, "italic"), bg="#1a1a2e", fg="#f9ca24", wraplength=360)
magic.pack(pady=5)

def add_wish():
    text = entry.get().strip()
    if text:
        listbox.insert("end", f"✦ {text}")
        entry.delete(0, "end")

def pick_wish():
    if listbox.size() == 0:
        magic.config(text="Add some wishes first! ✨")
        return
    listbox.selection_clear(0, "end")
    idx = random.randint(0, listbox.size() - 1)
    listbox.selection_set(idx)
    listbox.see(idx)
    wish = listbox.get(idx).replace("✦ ", "")
    magic.config(text=f"🪄 {wish}")

def delete_wish():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel[0])
        magic.config(text="")

btn_frame = tk.Frame(root, bg="#1a1a2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="✨ Add", font=("Helvetica", 11, "bold"), bg="#6c5ce7", fg="white", relief="flat", padx=14, pady=8, command=add_wish).pack(side="left", padx=5)
tk.Button(btn_frame, text="🪄 Pick a Wish!", font=("Helvetica", 11, "bold"), bg="#fd79a8", fg="white", relief="flat", padx=14, pady=8, command=pick_wish).pack(side="left", padx=5)
tk.Button(btn_frame, text="🗑 Remove", font=("Helvetica", 11), bg="#636e72", fg="white", relief="flat", padx=14, pady=8, command=delete_wish).pack(side="left", padx=5)

entry.bind("<Return>", lambda e: add_wish())
root.mainloop()