import tkinter as tk


window=tk.Tk()
window.title("input output app")
window.geometry("300x200")

entry=tk.Entry(window)
entry.pack()

label=tk.Label(window,text="")
label.pack()

def submit():
    text=entry.get()
    label.config(text=text)

button=tk.Button(window,text="Submit",command=submit)
button.pack()
window.mainloop()
