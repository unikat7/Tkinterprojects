import tkinter as tk

window=tk.Tk()
window.title("my first app")
window.geometry("300x200")

label=tk.Label(window,text="hello tkinter")
label.pack()
textbox=tk.Entry(window,text="type here")
textbox.pack()
window.mainloop()








