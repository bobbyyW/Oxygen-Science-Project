# The science Project

import tkinter
from tkinter import *
import random
import math
import time

def pressedBI():
    print('Yay')


root = Tk()
root.geometry('200x600')
canvas = tkinter.Canvas()
#oxygen = tkinter.PhotoImage(file = 'Oxygen.gif')
#canvas.create_image(0,0, image = oxygen)


def info():
    button = Button(root,text = 'Basic Information', command = pressedBI)
    button.pack(padx = 20, pady = 20)
    root.mainloop()

info()


a
