from tkinter import *
from random import *

root = Tk()
root.title('Камень Ножницы Бумага') #название
root.geometry('600x400') #разрешение окна
root.resizable(width=False, height=False) #запрет на изменение размера окна
root['bg'] = 'pink' #параметры bg и fg - цвета фона и текста


def knb():
    knb = ['Камень', 'Ножницы', 'Бумага'] #список
    value = choice(knb)
    labelText.configure(text='Великий рандом говорит: '+value)
    labelText.place(y=125, x=75)


labelText = Label(root, text='Раз, два, три!', fg='black', font=('Comic Sans MS', 20), bg='white')
labelText.place(y=125, x=220)

btn_stone = Button(root,
               text='Камень',
               font=('Comic Sans MS', 20),
               bg='white', #виджет кнопки
               command=knb)
btn_stone.place(y=200, x=85)

btn_scissoers = Button(root,
               text='Ножницы',
               font=('Comic Sans MS', 20),
               bg='white',  # виджет кнопки
               command=knb)
btn_scissors.place(y=200, x=230)

btn_paper = Button(root,
               text='Бумага',
               font=('Comic Sans MS', 20),
               bg='white',  # виджет кнопки
               command=knb)
btn_paper.place(y=200, x=405)

root.mainloop()
