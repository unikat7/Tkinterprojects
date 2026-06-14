import tkinter as tk


window=tk.Tk()


window.title("addition")
window.geometry("300x200")
firstnumber=tk.Entry(window)
firstnumber.pack()
secondnumber=tk.Entry(window)
secondnumber.pack()

def add():
    num1=int(firstnumber.get())
    num2=int(secondnumber.get())
    add=num1+num2
    result.config(text=f"the sum is {add}")
addbutton=tk.Button(window,text="Add",command=add)
addbutton.pack()
result=tk.Label(window,text="")
result.pack()




window.mainloop()

