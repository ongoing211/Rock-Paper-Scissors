from tkinter import *
from random import *

root = Tk()
root.title('Камень Ножницы Бумага') #название
root.geometry('600x400') #разрешение окна
root.resizable(width=False, height=False) #запрет на изменение размера окна
root['bg'] = 'pink' #параметры bg и fg - цвета фона и текста

labelText = Label(root, text='hi', fg='white', font=('Comic Sans MS', 20), bg='black')
labelText.place(y=175, x=275)


root.mainloop()
