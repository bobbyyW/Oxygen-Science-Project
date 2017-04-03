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
picture = main.create_image(300,200, image = oxygen)

#label for main screen

oxygenWord = Label(root,text = 'Oxygen', font = ('Times New Roman',60))
oxygenWord.place(x = 255, y = 395)


#basic info IIIIIIIII DONE IIIIIIIIII

def pressedBI():
    BIwindow = Toplevel(root, height = 600, width = 600, bg = 'white')
    BIcanvas = Canvas(BIwindow, width = 600, height = 600, bg = 'white')
    BIcanvas.pack()
    quitButton = Button(BIcanvas, text = 'Quit', width = 25, command = BIwindow.destroy)
    quitButton.pack()
    BIText = Label(BIcanvas,text = "Symbol: O", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Atomic Number + Avg. Mass: 8 + 16", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Classification: Non-Metal Family : Oxygen Family ", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Discoverers: Joseph Priestly + Carl Wilhelm Scheele", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "When it was discovered: 1774 [Joseph] + 1772 [Carl]", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Found in Nature: Air, Water, Atmopshere, Earth's Crust", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Most Common State of Matter: Gas", font = ('Times New Roman',30))
    BIText.pack()
    BIText = Label(BIcanvas,text = "Is it rare: No. It is abundant across the earth", font = ('Times New Roman',30))
    BIText.pack()
    for i in range(10):
        BIText = Label(BIcanvas,text = "", font = ('Times New Roman',30))
        BIText.pack()
    
    BI = PhotoImage(file = 'BI.gif')
    BIpic = Label(BIcanvas, image = BI)
    BIpic.image = BI
    BIpic.place(x = 160, y = 350)

BIbutton = Button(root,text = 'Basic Information', width = 25, command = pressedBI)
BIbutton.place(x = 217, y = 475)


#Bohr + Symbol IIIIIIIIII DONE IIIIIIIIIIIIII

def pressedBS():
    BSwindow = Toplevel(root, height = 800, width = 800, bg = 'white')
    BScanvas = Canvas(BSwindow, height = 800, width = 800, bg = 'white')
    BScanvas.pack()
    quitbutton = Button(BScanvas, text = 'Quit', command = BSwindow.destroy)
    quitbutton.pack()
    BSText = Label(BScanvas, text = 'This is our "Home-Made" Symbol                                             And This is the Bohr Model of Oxygen', font = ('Times New Roman',30))
    BSText.pack()
    for i in range(19):
        BSText = Label(BScanvas, text = '')
        BSText.pack()
    
    Symbol = PhotoImage(file = 'Symbol.gif')
    Symbolpic = Label(BScanvas, image = Symbol)
    Symbolpic.image = Symbol
    Symbolpic.place(x = 40, y = 75)

Bohr = PhotoImage(file = 'Bohr.gif')
    Bohrpic = Label(BScanvas, image = Bohr)
    Bohrpic.image = Bohr
    Bohrpic.place(x = 815, y = 75)


BSbutton = Button(root,text = 'Bohr Model + Symbol', command = pressedBS)
BSbutton.place(x = 267, y = 510)


#Interesting Facts
def pressedIF():
    IFwindow = Toplevel(root, height = 800, width = 800, bg = 'white')
    IFcanvas = Canvas(IFwindow, height = 800, width = 800, bg = 'white')
    IFcanvas.pack()
    quitbutton = Button(IFcanvas, text = 'Quit', command = IFwindow.destroy)
    quitbutton.pack()
    IFtext = Label(IFcanvas, text = '', font = ('Times New Roman', 30))
    IFtext.pack()
    for i in range(20):
        IFtext = Label(IFcanvas, text = '')
        IFtext.pack()
    
    IF = PhotoImage(file = 'Fact.gif')
    IFpic = Label(IFcanvas, image = IF)
    IFpic.image = IF
    IFpic.place(x = 300,y = 300)




IFbutton = Button(root, text = 'Interesting Facts', command = pressedIF)
IFbutton.place(y = 580, x = 275)



#Values + Uses

def pressedVU():
    print('')


VUbutton = Button(root, text = 'Values + Uses', command = pressedVU)
VUbutton.pack()



#Properties [Physical + Chemical]

def pressedP():
    print('')

Pbutton = Button(root, text = 'Properties', command = pressedP)
Pbutton.pack()


#

#

#

#GAME TIME

def pressedGame():
    print('')

Gamebutton = Button(root, text = 'Game', command = pressedGame)
Gamebutton.pack()


#bibliography  IIIIIIIII DONE IIIIIIIIII

def pressedBib():
    BIBwindow = Toplevel(root,height = 600, width = 600, bg = 'white')
    BIBcanvas = Canvas(BIBwindow, height = 600, width = 600, bg = 'white')
    BIBcanvas.pack()
    
    quitButton = Button(BIBcanvas, text = 'Quit', width = 25, command = BIBwindow.destroy)
    quitButton.pack()
    
    bibText = Label(BIBcanvas,text = 'Farndon, John. The Elements-Oxygen. N.p.: Benchmark, 1999. Print.', font = ('Times New Roman',30))
    bibText.pack()
    bibText = Label(BIBcanvas,text = '', font = ('Times New Roman',30))
    bibText.pack()
    bibText = Label(BIBcanvas,text = '"The Discovery of Oxygen." The Discovery of Oxygen. N.p., n.d. Web. 23 Mar. 2017.', font = ('Times New Roman',30))
    bibText.pack()
    bibText = Label(BIBcanvas,text = "", font = ('Times New Roman',30))
    bibText.pack()
    bibText = Label(BIBcanvas,text = '"Oxygen." Wikipedia. Wikimedia Foundation, 22 Mar. 2017. Web. 23 Mar. 2017.', font = ('Times New Roman',30))
    bibText.pack()
    for i in range(10):
        bibText = Label(BIBcanvas,text = '', font = ('Times New Roman',30))
        bibText.pack()
    
    bib = PhotoImage(file = 'Bib.gif')
    bibpic = Label(BIBcanvas, image = bib)
    bibpic.image = bib
    bibpic.place(x = 330, y = 230)


BibButton = Button(root, text = 'Bibliography', command = pressedBib)
BibButton.place(y = 545, x = 290)
