from tkinter import *
from tkinter import ttk
from random import randint

tk = Tk()
tk.title("Resistors")
canvas = Canvas(tk, height=700, width=1000)


def click_btn1():
    print("function1")
    tk1 = Toplevel()  # Открывается новое окно для последовательного соединения
    tk1.title('Последовательное соединение')
    tk1.geometry("1000x800")
    canvas1 = Canvas(tk1, height=700, width=1000)
    canvas1.pack()
    canvas1.create_line(200, 100, 200, 300)  # Создание боковых проводов
    canvas1.create_line(802, 100, 802, 300)

    n = 0  # Создание цепочки резисторов
    for i in range(0, 3):
        n1 = 200 + 86 * n
        n2 = n1 + 86
        n3 = n2 + 86
        canvas1.create_line(n1, 100, n2, 100)
        canvas1.create_rectangle(n2, 75, n3, 125)
        n += 2
    canvas1.create_line(716, 100, 802, 100)

    canvas1.create_line(200, 300, 496, 300)  # Создание нижних проводов
    canvas1.create_line(506, 300, 802, 300)

    canvas1.create_line(400, 300, 400, 200)  # Создание вольтметра
    canvas1.create_line(600, 300, 600, 200)
    canvas1.create_line(400, 200, 470, 200)
    canvas1.create_line(530, 200, 600, 200)
    canvas1.create_text(500, 200, text='V')

    canvas1.create_oval(470, 170, 530, 230)

    canvas1.create_line(496, 285, 496, 315)  # Создание источника питания
    canvas1.create_line(506, 275, 506, 325)

    canvas1.create_text(329, 100, text='R1')  # Создание обозначений резисторов
    canvas1.create_text(501, 100, text='R2')
    canvas1.create_text(673, 100, text='R3')

    canvas1.create_text(365, 430, text='Ответы запишите в формате: X.XX')

    R1 = randint(1, 5)
    R2 = randint(1, 5)
    R3 = randint(1, 5)
    Uv = randint(6, 12)

    text = ("R1 = " + str(R1) + ' Ом;   R2 = ' + str(R2) + ' Ом;   R3 = ' + str(R3) + ' Ом;   Uv = ' + str(Uv) + ' B')
    canvas1.create_text(397, 405, text=text)
    canvas1.create_text(220, 465, text='U1')
    canvas1.create_text(220, 490, text='U2')
    canvas1.create_text(220, 515, text='U3')
    canvas1.create_text(220, 540, text='I')

    label1 = ttk.Label(tk1, text='')
    label2 = ttk.Label(tk1, text='')
    label3 = ttk.Label(tk1, text='')
    label4 = ttk.Label(tk1, text='')

    def click_btnAnsw():
        answU1 = entryU1.get()
        answU2 = entryU2.get()
        answU3 = entryU3.get()
        answI = entryI.get()
        label1.config(text='')
        label2.config(text='')
        label3.config(text='')
        label4.config(text='')

        I = Uv / (R1 + R2 + R3)
        U1 = I * R1
        U2 = I * R2
        U3 = I * R3
        if float(answU1) == round(U1, 2):
            label1.config(text='Да')
            label1.place(x=700, y=450)
        else:
            label1.config(text='Нет')
            label1.place(x=700, y=450)

        if float(answU2) == round(U2, 2):
            label2.config(text='Да')
            label2.place(x=700, y=475)
        else:
            label2.config(text='Нет')
            label2.place(x=700, y=475)

        if float(answU3) == round(U3, 2):
            label3.config(text='Да')
            label3.place(x=700, y=500)
        else:
            label3.config(text='Нет')
            label3.place(x=700, y=500)

        if float(answI) == round(I, 2):
            label4.config(text='Да')
            label4.place(x=700, y=525)
        else:
            label4.config(text='Нет')
            label4.place(x=700, y=525)

    btnAnsw = ttk.Button(tk1, text="Ответ", command=click_btnAnsw)
    btnAnsw.place(x=550, y=450)

    entryU1 = ttk.Entry(tk1, width=30)
    entryU1.place(x=250, y=450)
    entryU2 = ttk.Entry(tk1, width=30)
    entryU2.place(x=250, y=475)
    entryU3 = ttk.Entry(tk1, width=30)
    entryU3.place(x=250, y=500)
    entryI = ttk.Entry(tk1, width=30)
    entryI.place(x=250, y=525)


def click_btn2():
    print("function2")
    tk2 = Toplevel()  # Открывается новое окно для параллельного соединения
    tk2.title('Параллельное соединение')
    tk2.geometry("1000x800")
    canvas2 = Canvas(tk2, height=700, width=1000)
    canvas2.pack()

    canvas2.create_line(200, 300, 320, 300)  # Создание нижних проводов
    canvas2.create_line(380, 300, 496, 300)
    canvas2.create_line(506, 300, 802, 300)

    canvas2.create_line(496, 285, 496, 315)  # Создание источника питания
    canvas2.create_line(506, 275, 506, 325)

    canvas2.create_line(200, 100, 200, 300)  # Создание боковых проводов
    canvas2.create_line(802, 100, 802, 300)

    canvas2.create_line(200, 100, 440, 100)  # Создание цепочки резисторов
    canvas2.create_line(440, 80, 560, 80)
    canvas2.create_line(440, 120, 560, 120)
    canvas2.create_line(440, 80, 440, 120)
    canvas2.create_line(560, 80, 560, 120)
    canvas2.create_line(560, 100, 802, 100)

    canvas2.create_line(320, 40, 320, 160)
    canvas2.create_line(320, 40, 440, 40)
    canvas2.create_line(320, 160, 440, 160)
    canvas2.create_line(440, 20, 440, 60)
    canvas2.create_line(440, 140, 440, 180)
    canvas2.create_line(440, 20, 560, 20)
    canvas2.create_line(440, 60, 560, 60)
    canvas2.create_line(440, 140, 560, 140)
    canvas2.create_line(440, 180, 560, 180)
    canvas2.create_line(560, 20, 560, 60)
    canvas2.create_line(560, 140, 560, 180)
    canvas2.create_line(560, 40, 680, 40)
    canvas2.create_line(560, 160, 680, 160)
    canvas2.create_line(680, 40, 680, 160)

    canvas2.create_text(501, 40, text='R1')  # Создание обозначений резисторов
    canvas2.create_text(501, 100, text='R2')
    canvas2.create_text(501, 160, text='R3')

    canvas2.create_oval(380, 330, 320, 270) #Создание амперметра
    canvas2.create_text(350, 300, text='А')


    canvas2.create_text(365, 430, text='Ответы запишите в формате: X.XX')

    R1 = randint(1, 5)
    R2 = randint(1, 5)
    R3 = randint(1, 5)
    Ia = randint(6, 12)

    text = ("R1 = " + str(R1) + ' Ом;   R2 = ' + str(R2) + ' Ом;   R3 = ' + str(R3) + ' Ом;   Ia = ' + str(Ia) + ' A')
    canvas2.create_text(397, 405, text=text)
    canvas2.create_text(220, 465, text='I1')
    canvas2.create_text(220, 490, text='I2')
    canvas2.create_text(220, 515, text='I3')
    canvas2.create_text(220, 540, text='U')

    label1 = ttk.Label(tk2, text='')
    label2 = ttk.Label(tk2, text='')
    label3 = ttk.Label(tk2, text='')
    label4 = ttk.Label(tk2, text='')

    def click_btnAnsw():
        answI1 = entryI1.get()
        answI2 = entryI2.get()
        answI3 = entryI3.get()
        answUcom = entryUcom.get()
        Rcom = 1 / (1 / R1 + 1 / R2 + 1 / R3)
        Ucom = Ia * Rcom
        I1 = Ucom / R1
        I2 = Ucom / R2
        I3 = Ucom / R3
        if float(answI1) == round(I1, 2):
            label1.config(text='Да')
            label1.place(x=675, y=450)
        else:
            label1.config(text='Нет')
            label1.place(x=675, y=450)

        if float(answI2) == round(I2, 2):
            label2.config(text='Да')
            label2.place(x=675, y=475)
        else:
            label2.config(text='Нет')
            label2.place(x=675, y=475)

        if float(answI3) == round(I3, 2):
            label3.config(text='Да')
            label3.place(x=675, y=500)
        else:
            label3.config(text='Нет')
            label3.place(x=675, y=500)

        if float(answUcom) == round(Ucom, 2):
            label4.config(text='Да')
            label4.place(x=675, y=525)
        else:
            label4.config(text='Нет')
            label4.place(x=675, y=525)


    btnAnsw = ttk.Button(tk2, text="Ответ", command=click_btnAnsw)
    btnAnsw.place(x=550, y=450)

    entryI1 = ttk.Entry(tk2, width=30)
    entryI1.place(x=250, y=450)
    entryI2 = ttk.Entry(tk2, width=30)
    entryI2.place(x=250, y=475)
    entryI3 = ttk.Entry(tk2, width=30)
    entryI3.place(x=250, y=500)
    entryUcom = ttk.Entry(tk2, width=30)
    entryUcom.place(x=250, y=525)


def click_btn3():
    print("function3")
    tk3 = Toplevel()  # Открывается новое окно для смешанного соединения
    tk3.title('Смешанное соединение')
    tk3.geometry("1000x800")
    canvas3 = Canvas(tk3, height=700, width=1000)
    canvas3.pack()

    canvas3.create_line(200, 300, 496, 300)  # Создание нижних проводов
    canvas3.create_line(506, 300, 802, 300)


    canvas3.create_line(496, 285, 496, 315)  # Создание источника питания
    canvas3.create_line(506, 275, 506, 325)

    canvas3.create_line(200, 100, 200, 300)  # Создание боковых проводов
    canvas3.create_line(802, 100, 802, 300)

    canvas3.create_line(300, 80, 400, 80)   #Создание резисторов
    canvas3.create_line(300, 120, 400, 120)
    canvas3.create_line(300, 80, 300, 120)
    canvas3.create_line(400, 80, 400, 120)

    canvas3.create_line(600, 150, 700, 150)
    canvas3.create_line(600, 110, 700, 110)
    canvas3.create_line(600, 150, 600, 110)
    canvas3.create_line(700, 150, 700, 110)

    canvas3.create_line(600, 90, 700, 90)
    canvas3.create_line(600, 50, 700, 50)
    canvas3.create_line(600, 90, 600, 50)
    canvas3.create_line(700, 90, 700, 50)

    canvas3.create_line(200, 100, 300, 100)  #Создание проводов
    canvas3.create_line(400, 100, 550, 100)
    canvas3.create_line(550, 130, 550, 70)
    canvas3.create_line(550, 130, 600, 130)
    canvas3.create_line(550, 70, 600, 70)
    canvas3.create_line(700, 130, 750, 130)
    canvas3.create_line(700, 70, 750, 70)
    canvas3.create_line(750, 130, 750, 70)
    canvas3.create_line(802, 100, 750, 100)

    canvas3.create_text(365, 430, text='Ответы запишите в формате: X.XX')

    R1 = randint(1, 5)
    R2 = randint(1, 5)
    R3 = randint(1, 5)
    Uv = randint(6, 12)

    text = ("R1 = " + str(R1) + ' Ом;   R2 = ' + str(R2) + ' Ом;   R3 = ' + str(R3) + ' Ом;   Uv = ' + str(Uv) + ' B')
    canvas3.create_text(397, 405, text=text)
    canvas3.create_text(220, 465, text='I')
    canvas3.create_text(220, 490, text='U1')
    canvas3.create_text(220, 515, text='U2')
    canvas3.create_text(220, 540, text='U3')
    canvas3.create_text(220, 565, text='I1')
    canvas3.create_text(220, 590, text='I2')
    canvas3.create_text(220, 615, text='I3')

    label1 = ttk.Label(tk3, text='')
    label2 = ttk.Label(tk3, text='')
    label3 = ttk.Label(tk3, text='')
    label4 = ttk.Label(tk3, text='')
    label5 = ttk.Label(tk3, text='')
    label6 = ttk.Label(tk3, text='')
    label7 = ttk.Label(tk3, text='')

    def click_btnAnsw():
        answI = entryI.get()
        answU1 = entryU1.get()
        answU2 = entryU2.get()
        answU3 = entryU3.get()
        answI1 = entryU1.get()
        answI2 = entryU2.get()
        answI3 = entryU3.get()

        label1.config(text='')
        label2.config(text='')
        label3.config(text='')
        label4.config(text='')
        label5.config(text='')
        label6.config(text='')
        label7.config(text='')

        R23 = (R2 * R3) / (R2 + R3)
        Rcom = R1 + R23
        Icom = Uv / Rcom
        I1 = Icom
        U1 = I1 * R1
        U2 = Uv - U1
        U3 = U2
        I2 = U2 / R2
        I3 = U3 / R3



        if float(answI) == round(Icom, 2):
            label1.config(text='Да')
            label1.place(x=700, y=525)
        else:
            label1.config(text='Нет')
            label1.place(x=700, y=525)

        if float(answU1) == round(U1, 2):
            label2.config(text='Да')
            label2.place(x=700, y=450)
        else:
            label2.config(text='Нет')
            label2.place(x=700, y=450)

        if float(answU2) == round(U2, 2):
            label3.config(text='Да')
            label3.place(x=700, y=475)
        else:
            label3.config(text='Нет')
            label3.place(x=700, y=475)

        if float(answU3) == round(U3, 2):
            label4.config(text='Да')
            label4.place(x=700, y=500)
        else:
            label4.config(text='Нет')
            label4.place(x=700, y=500)

        if float(answI1) == round(I1, 2):
            label5.config(text='Да')
            label5.place(x=700, y=525)
        else:
            label5.config(text='Нет')
            label5.place(x=700, y=525)

        if float(answI2) == round(I2, 2):
            label6.config(text='Да')
            label6.place(x=700, y=525)
        else:
            label6.config(text='Нет')
            label6.place(x=700, y=525)

        if float(answI3) == round(I3, 2):
            label7.config(text='Да')
            label7.place(x=700, y=525)
        else:
            label7.config(text='Нет')
            label7.place(x=700, y=525)

    btnAnsw = ttk.Button(tk3, text="Ответ", command=click_btnAnsw)
    btnAnsw.place(x=550, y=450)

    entryI = ttk.Entry(tk3, width=30)
    entryI.place(x=250, y=450)
    entryU1 = ttk.Entry(tk3, width=30)
    entryU1.place(x=250, y=475)
    entryU2 = ttk.Entry(tk3, width=30)
    entryU2.place(x=250, y=500)
    entryU3 = ttk.Entry(tk3, width=30)
    entryU3.place(x=250, y=525)
    entryI1 = ttk.Entry(tk3, width=30)
    entryI1.place(x=250, y=550)
    entryI2 = ttk.Entry(tk3, width=30)
    entryI2.place(x=250, y=575)
    entryI3 = ttk.Entry(tk3, width=30)
    entryI3.place(x=250, y=600)

    tk3.mainloop()


canvas.create_text(500, 50, text='Выберите тип цепи')

btn1 = ttk.Button(text="Последовательное", command=click_btn1)
btn1.place(x=420, y=80)
btn2 = ttk.Button(text="Параллельное", command=click_btn2)
btn2.place(x=435, y=105)
btn3 = ttk.Button(text="Смешанное", command=click_btn3)
btn3.place(x=444, y=130)

canvas.pack()

tk.mainloop()