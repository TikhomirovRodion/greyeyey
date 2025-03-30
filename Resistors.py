from tkinter import *
from tkinter import ttk
from random import randint
def click_btn1():
    print("function1")
    canvas.delete('all')     #Очистка окна

    canvas.create_line(200, 100, 200, 300)      #Создание боковых проводов
    canvas.create_line(802, 100, 802, 300)

    btn3.destroy()
    btn2.destroy()
    btn1.destroy()


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

    canvas.create_text(329, 100, text='R1')     #Создание обозначений резисторов
    canvas.create_text(501, 100, text='R2')
    canvas.create_text(673, 100, text='R3')

    canvas.create_text(365, 430, text='Ответы запишите в формате: X.XX')

    R1 = randint(1, 5)
    R2 = randint(1, 5)
    R3 = randint(1, 5)
    Uv = randint(6, 12)

    I = Uv / (R1 + R2 + R3)
    print(round(I * R1, 2))
    print(round(I * R2, 2))
    print(round(I * R3, 2))
    print(round(I, 2))

    text = ("R1 = " + str(R1) + ' Ом;   R2 = ' + str(R2) + ' Ом;   R3 = ' + str(R3) + ' Ом;   Uv = ' + str(Uv) + ' B')
    canvas.create_text(397, 405, text=text)
    canvas.create_text(220, 465, text='U1')
    canvas.create_text(220, 490, text='U2')
    canvas.create_text(220, 515, text='U3')
    canvas.create_text(220, 540, text='I')


    def click_btnAnsw():
        answU1 = entryU1.get()
        answU2 = entryU2.get()
        answU3 = entryU3.get()
        answI = entryI.get()
        #print(answU1)
        I = Uv / (R1 + R2 + R3)
        U1 = I * R1
        U2 = I * R2
        U3 = I * R3
        if float(answU1) == round(U1, 2):
            canvas.create_text(675, 465, text='Да')
        else:
            canvas.create_text(675, 465, text='Нет')

        if float(answU2) == round(U2, 2):
            canvas.create_text(675, 490, text='Да')
        else:
            canvas.create_text(675, 490, text='Нет')

        if float(answU3) == round(U3, 2):
            canvas.create_text(675, 515, text='Да')
        else:
            canvas.create_text(675, 515, text='Нет')

        if float(answI) == round(I, 2):
            canvas.create_text(675, 540, text='Да')
        else:
            canvas.create_text(675, 540, text='Нет')

    btnAnsw = ttk.Button(text="Ответ", command=click_btnAnsw)
    btnAnsw.place(x=550, y=450)

    entryU1 = ttk.Entry(width=30)
    entryU1.place(x=250, y=450)
    entryU2 = ttk.Entry(width=30)
    entryU2.place(x=250, y=475)
    entryU3 = ttk.Entry(width=30)
    entryU3.place(x=250, y=500)
    entryI = ttk.Entry(width=30)
    entryI.place(x=250, y=525)

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

canvas.create_text(500, 50, text='Выберите тип цепи')

btn1 = ttk.Button(text="Последовательное", command=click_btn1)
btn1.place(x=420, y=80)
btn2 = ttk.Button(text="Параллельное", command=click_btn2)
btn2.place(x=435, y=105)
btn3 = ttk.Button(text="Смешанное", command=click_btn3)
btn3.place(x=444, y=130)

canvas.pack()

tk.mainloop()