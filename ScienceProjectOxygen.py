# The science Project
import tkinter as tk
from tkinter import *
import random
import math
import time

#starting off

root = Tk()
root.title('Oxygen')
root.geometry('700x700')
main = Canvas(root,height = 600, width = 600, bg = 'white')
main.pack()

#main

oxygen = PhotoImage(file = 'Oxygen.gif')
picture = main.create_image(300,300, image = oxygen)
main.move(0,0,picture)

#label for main screen

oxygenWord = Label(root,text = 'Oxygen', font = ('Times New Roman',30))
oxygenWord.pack()

#QUIT BUTTON

def BIB_quit():
    pressedBib.destroy()

def pressedBI():
    print('')

BIbutton = Button(root,text = 'Basic Information', command = pressedBI)
BIbutton.pack()

def pressedBib():
    BIBwindow = tk.Toplevel()
    bibText = Label(BIBwindow,text = 'Oxygen is c00l', font = ('Times New Roman',30))
    bibText.pack()
    quitButton = Button(BIBwindow, text = 'Quit', width = 25, command = BIB_quit)
    quitButton.pack()

BibButton = Button(root, text = 'Bibliography', command = pressedBib)
BibButton.pack()



