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

canvas.create_text(10, 10, text='Выберите тип цепи', fill="#004D40")

btn1 = ttk.Button(text="Последовательное", command=click_btn1)
btn1.pack()
btn2 = ttk.Button(text="Параллельное", command=click_btn1)
btn2.pack()
btn3 = ttk.Button(text="Смешанное", command=click_btn1)
btn3.pack()

canvas.pack()

tk.mainloop()