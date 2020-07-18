from tkinter import *
from PIL import ImageTk, Image
from maquina import Maquina
# Global objects
enigMachine = Maquina()
bgColor = '#2f324a'
activeColor = "#494d70"
pathKeyboard = "./img/keyboard/"
pathLamps = "./img/lamps/"
labels = []
letter = '' #para manejar el evento del boton :c
# Get letter's position that trigger an event
def getPosition(widgetName):
    # Pattern .!frame().!button()
    row = int(str(widgetName)[7]) - 4
    if len(widgetName) == 16:
        col = 0
    else:
        col = int(str(widgetName)[-1]) - 1
    return row, col
#Bind to turn on/off lamps
def turnOnLamp(event):
    position = getPosition(str(event.widget))
    row = position[0]
    col = position[1]
    global letter
    letter = enigMachine.cifrar(keyboard_letters[row][col].upper())
    loadQ = Image.open(pathLamps+letter.lower()+"_h.png")
    renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
    indexLetter = dictNumLet.get(letter.lower())
    labels[indexLetter].configure(image = renderHQ)
    labels[indexLetter].image = renderHQ
def turnOffLamp(event):
    loadQ = Image.open(pathLamps+letter.lower()+".png")
    renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
    indexLetter = dictNumLet.get(letter.lower())
    labels[indexLetter].configure(image = renderHQ)
    labels[indexLetter].image = renderHQ

#Dictionary to find labels to change
dictLetters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n', 'm']
dictNumbers = range(26)
dictNumLet = dict(zip(dictLetters, dictNumbers))

#Main window
win = Tk()
win.title("ENIGMA MACHINE")
win.configure(bg= bgColor)

#keyboard onscreen order
keyboard_letters = [
                ['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l'],
                ['z','x','c','v','b','n', 'm']
                ]

#Lamps
for keyboard in keyboard_letters:
    f = Frame(win)
    for button in keyboard:
        render = ImageTk.PhotoImage(Image.open(pathLamps+button+".png").resize((50,50),Image.ANTIALIAS))
        labels.append( Label(f, image = render,bg='#2f324a'))
        labels[-1].img = render
        labels[-1].pack(side=LEFT)
    f.pack(side=TOP)
# Keyboard
for keyboard in keyboard_letters:
    f = Frame(win)
    for button in keyboard:
        #command = lambda x=button: conversion(x)
        load = Image.open(pathKeyboard+button+".png")
        render = ImageTk.PhotoImage(load.resize((30,30),Image.ANTIALIAS))
        img = Button(f, image = render,bg='#2f324a',activebackground="#494d70", borderwidth =0)
        img.image = render
        img.bind("<ButtonPress>", turnOnLamp)
        img.bind("<ButtonRelease>", turnOffLamp)
        img.pack(side=LEFT)
    f.pack(side=TOP)
win.mainloop()