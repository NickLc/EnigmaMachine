from tkinter import *
from PIL import ImageTk, Image
from maquina import Maquina
enigMachine = Maquina()
win = Tk()
def printEncrypted(character):
    print(enigMachine.cifrar(character))

win.title("Keyboard")
win.config(bg='#2f324a')

keyboard_letters = [
                ['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l'],
                ['z','x','c','v','b','n', 'm']
]

for keyboard in keyboard_letters:
    f = Frame(win)
    for button in keyboard:
        command = lambda x=button: printEncrypted(x)
        load = Image.open("./img/keyboard/"+button+".png")
        render = ImageTk.PhotoImage(load.resize((30,30),Image.ANTIALIAS))
        img = Button(f, image = render,bg='#2f324a',activebackground="#494d70", borderwidth =0, command= command)
        img.image = render
        img.pack(side=LEFT)
    f.pack(side=TOP)
win.mainloop()