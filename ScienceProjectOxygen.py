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


#basic info

def pressedBI():
    BIwindow = Toplevel(root,height = 600, width = 600, bg = 'white')
    BIText = Label(BIwindow,text = "", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIwindow,text = "", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIwindow,text = "", font = ('Times New Roman',30))
    BIText.pack()
    quitButton = Button(BIwindow, text = 'Quit', width = 25, command = BIwindow.destroy)
    quitButton.pack()
    BIcanvas = Canvas(BIwindow, width = 600, height = 600)
    BIcanvas.pack()
    symbol = PhotoImage(file = 'Symbol.gif')
    symbolpic = BIcanvas.create_image(300,300, image = symbol)
    symbolpic.pack()


BIbutton = Button(root,text = 'Basic Information', command = pressedBI)
BIbutton.pack()

#bibliography

def pressedBib():
    BIBwindow = Toplevel(root,height = 800, width = 800, bg = 'white')
    bibText = Label(BIBwindow,text = 'Farndon, John. The Elements-Oxygen. N.p.: Benchmark, 1999. Print.'
                    , font = ('Times New Roman',30))
                    bibText.pack()
                    bibText = Label(BIBwindow,text = '', font = ('Times New Roman',30))
                    bibText.pack()
                    bibText = Label(BIBwindow,text = '"The Discovery of Oxygen." The Discovery of Oxygen. N.p., n.d. Web. 23 Mar. 2017.', font = ('Times New Roman',30))
                    bibText.pack()
                    bibText = Label(BIBwindow,text = "", font = ('Times New Roman',30))
                    bibText.pack()
                    bibText = Label(BIBwindow,text = '"Oxygen." Wikipedia. Wikimedia Foundation, 22 Mar. 2017. Web. 23 Mar. 2017.'
                                    , font = ('Times New Roman',30))
                    bibText.pack()
                    BIBcanvas = Canvas(BIBwindow, width = 800, height = 800)
                    BIBcanvas.pack()
                    bib = PhotoImage(file = 'Bib.gif')
                    bibpic = BIBcanvas.create_image(300,300, image = bib)
                    bibpic.pack()
                    quitButton = Button(BIBwindow, text = 'Quit', width = 25, command = BIBwindow.destroy)
                    quitButton.pack()    

BibButton = Button(root, text = 'Bibliography', command = pressedBib)
BibButton.pack()

#Interesting Facts




#Values + Uses




#Properties [Physical + Chemical]







#
#
#
#



#Game Time






