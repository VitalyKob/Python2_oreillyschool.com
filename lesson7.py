from tkinter import *

def show_sum():
    try:
        num1 = float(e1.get())
        num2 = float(e2.get())
        float_sum = num1 + num2
        output = float_sum
        label.config(text=output)
    except ValueError:
        output = "***ERROR***"
        label.config(text=output)

master = Tk()
Label(master, text="Number 1").grid(row=0)
Label(master, text="Number 2").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

label = Label(text="Output label")
label.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='SUM', command=show_sum).grid(row=7, column=1, sticky=W, pady=4)

mainloop()
