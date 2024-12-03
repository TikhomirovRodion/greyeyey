from tkinter import *
from tkinter import ttk
def click_btn1():
    print("function1")
    canvas.delete('all')     #Очистка окна
    btn3.destroy()
    btn2.destroy()
    btn1.destroy()

    canvas.create_line(200, 100, 200, 300)      #Создание боковых проводов
    canvas.create_line(802, 100, 802, 300)

    n=0                                 #Создание цепочки резисторов
    for i in range(0, 3):
        n1 = 200+86*n
        n2 = n1+86
        n3 = n2+86
        canvas.create_line(n1, 100, n2, 100)
        canvas.create_rectangle(n2, 75, n3, 125)
        n+=2
    canvas.create_line(716, 100, 802, 100)

    canvas.create_line(200, 300, 496, 300)      #Создание нижних проводов
    canvas.create_line(506, 300, 802, 300)

    canvas.create_line(496, 285, 496, 315)      #Создание источника питания
    canvas.create_line(506, 275, 506, 325)

    canvas.create_text(329, 100, text='R1', fill="#004D40")     #Создание обозначений резисторов
    canvas.create_text(501, 100, text='R2', fill="#004D40")
    canvas.create_text(673, 100, text='R3', fill="#004D40")

    entry1 = ttk.Label()
    entry1.pack(x=300, y=500)
    entry = ttk.Entry()
    entry.pack(x=300, y=500)
    entry1["text"] = entry.get()

def click_btn2():
    print("function2")
    canvas.delete('all')
    btn3.destroy()
    btn2.destroy()
    btn1.destroy()

def click_btn3():
    print("function3")
    canvas.delete('all')
    btn3.destroy()
    btn2.destroy()
    btn1.destroy()


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