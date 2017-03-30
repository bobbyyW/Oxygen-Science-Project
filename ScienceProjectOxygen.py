# The science Project


from tkinter import *
import random
import math
import time

root = Tk()
root.title('Oxygen')
root.geometry('700x700')
canvas = Canvas(root,height = 600, width = 600, bg = 'white')
canvas.pack()

#Photo

oxygen = PhotoImage(file = 'Oxygen.gif')
picture = canvas.create_image(300,300, image = oxygen)
canvas.move(0,0,picture)

#canvas.move(0,0,oxygen)

oxygenWord = Label(root,text = 'Oxygen', font = ('Times New Roman',30))
oxygenWord.pack()


#BUTTONS

#BASIC INFO
def pressedBI():
    print('')

BIbutton = Button(root,text = 'Basic Information', command = pressedBI)
BIbutton.pack()

#Bibliography

def pressedBib():
    print('')

BibButton = Button(root, text = 'Bibliography', command = pressedBib)
BibButton.pack()
