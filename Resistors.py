from tkinter import *
from tkinter import ttk
def click_btn1():
    print("function1")

def click_btn2():
    print("function2")

def click_btn3():
    print("function3")
tk = Tk()
tk.title("Resistors")
canvas = Canvas(tk, height=700, width=1000)

canvas.create_text(500, 50, text='Выберите тип цепи', fill="#004D40")

btn1 = ttk.Button(text="Последовательное", command=click_btn1)
btn1.place(x=420, y=80)
btn2 = ttk.Button(text="Параллельное", command=click_btn2)
btn2.place(x=435, y=105)
btn3 = ttk.Button(text="Смешанное", command=click_btn3)
btn3.place(x=444, y=130)

canvas.pack()

tk.mainloop()