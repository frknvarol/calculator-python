from tkinter import *
from calculator import calculate

root = Tk()

ent = Entry(root)
ent.pack()


def tst():
    print(calculate(ent.get()))


my_button = Button(root, text="Calculate", command=tst)
my_button.pack()

#branch deneme
