from tkinter import *
windows = Tk()
e = Entry(windows, width = 35)
e.grid(row = 0, column = 0, columnspan = 5)

def click(i):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s+i)

currentsum=0
def add():
    global f_number
    global action
    action = "+"
    f_number = int(e.get())
    e.delete(0, END)

def subtract():
    global f_number
    global action
    action = "-"
    f_number = int(e.get())
    e.delete(0, END)


def multiply():
    global f_number
    global action
    action = "*"
    f_number = int(e.get())
    e.delete(0, END)

def divide():
    global f_number
    global action
    action = "/"
    f_number = int(e.get())
    e.delete(0, END)

def answer():
    s_number = int(e.get())
    e.delete(0, END)
    if action == "+":
        s = str(f_number) + "+" + str(s_number) + "=" + str(f_number + s_number)
    elif action == "-":
        s = str(f_number) + "-" + str(s_number) + "=" + str(f_number - s_number)
    elif action == "*":
        s = str(f_number) + "x" + str(s_number) + "=" + str(f_number * s_number)
    elif action == "/":
        s = str(f_number) + "/" + str(s_number) + "=" + str(f_number / s_number)

    e.insert(0, s)
def clear():
    e.delete(0, END)

Button(windows, text = "1", padx = 40, pady = 20, command = lambda: click("1")).grid(row = 4, column = 0)
Button(windows, text = "2", padx = 40, pady = 20, command = lambda: click("2")).grid(row = 4, column = 1)
Button(windows, text = "3", padx = 40, pady = 20, command = lambda: click("3")).grid(row = 4, column = 2)
Button(windows, text = "4", padx = 40, pady = 20, command = lambda: click("4")).grid(row = 3, column = 0)
Button(windows, text = "5", padx = 40, pady = 20, command = lambda: click("5")).grid(row = 3, column = 1)
Button(windows, text = "6", padx = 40, pady = 20, command = lambda: click("6")).grid(row = 3, column = 2)
Button(windows, text = "7", padx = 40, pady = 20, command = lambda: click("7")).grid(row = 2, column = 0)
Button(windows, text = "8", padx = 40, pady = 20, command = lambda: click("8")).grid(row = 2, column = 1)
Button(windows, text = "9", padx = 40, pady = 20, command = lambda: click("9")).grid(row = 2, column = 2)
Button(windows, text = "0", padx = 137, pady = 20, command = lambda: click("0")).grid(row = 5, column = 0, columnspan = 3)

Button(windows, text = "Clear", padx = 126, pady = 20, command = clear).grid(row = 1, column = 0, columnspan = 3)
Button(windows, text = "=", padx = 39, pady = 20, command = answer).grid(row = 5, column = 4)
Button(windows, text = "+", padx = 39, pady = 20, command = add).grid(row = 4, column = 4)
Button(windows, text = "-", padx = 39, pady = 20, command = subtract).grid(row = 3, column = 4)
Button(windows, text = "x", padx = 39, pady = 20, command = multiply).grid(row = 2, column = 4)
Button(windows, text = "/", padx = 39, pady = 20, command = divide).grid(row = 1, column = 4)


windows.mainloop()