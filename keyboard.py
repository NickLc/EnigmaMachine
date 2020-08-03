from tkinter import *
from tkinter import ttk 
import tkinter as tk
from PIL import ImageTk, Image
from maquina import Maquina
from string import ascii_uppercase

### VARIABLES GLOBALES
bgColor = '#2f324a'
activeColor = "#494d70"
pathKeyboard = "./img/keyboard/"
pathLamps = "./img/lamps/"
labels = []
letter = '' #para manejar el evento del boton :c
#Dictionary to find labels to change
dictLetters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n', 'm']
dictNumbers = range(26)
dictNumLet = dict(zip(dictLetters, dictNumbers))
#keyboard onscreen order
keyboard_letters = [
                ['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l'],
                ['z','x','c','v','b','n', 'm']
                ]

class Gui:
	def __init__(self, master, orden_rotores, iniciales_rotores, plugboard_conexiones):
		self.win = master
		self.win.title("ENIGMA MACHINE")
		self.win.configure(bg= bgColor)
		self.machine = Maquina(orden_rotores, iniciales_rotores, plugboard_conexiones)
		self.machine_enabled = False

		self.render_lamps()
		self.render_buttons()

		self.button_destroy_machine = Button(self.win,bg='white', borderwidth =0, text = "Terminar maquina", command = self.terminar_maquina)
		self.button_destroy_machine.pack()

		self.win.mainloop()


	def terminar_maquina(self):
		self.win.destroy()

	def render_lamps(self):
		for keyboard in keyboard_letters:
			self.f = Frame(self.win)
			for button in keyboard:
				render = ImageTk.PhotoImage(Image.open(pathLamps+button+".png").resize((50,50),Image.ANTIALIAS))
				labels.append( Label(self.f, image = render,bg='#2f324a'))
				labels[-1].img = render
				labels[-1].pack(side=LEFT)
			self.f.pack(side=TOP)

	def render_buttons(self):
		for row,keyboard in enumerate(keyboard_letters):
			self.f = Frame(self.win)
			for col,button in enumerate(keyboard):
				#command = lambda x=button: conversion(x)
				load = Image.open(pathKeyboard+button+".png")
				render = ImageTk.PhotoImage(load.resize((30,30),Image.ANTIALIAS))
				img = Button(self.f, image = render,bg='#2f324a',activebackground="#494d70", borderwidth =0)
				img.image = render
				img.bind("<ButtonPress>", lambda event, row=row, col = col: self.turnOnLamp(event, row, col))
				img.bind("<ButtonRelease>", lambda event , row=row, col = col: self.turnOffLamp(event, row, col))
				
				img.pack(side=LEFT)
			self.f.pack(side=TOP)

	def turnOnLamp(self, event, row, col):
		global letter
		letter = self.machine.cifrar(keyboard_letters[row][col].upper())
		loadQ = Image.open(pathLamps+letter.lower()+"_h.png")
		renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
		indexLetter = dictNumLet.get(letter.lower())
		labels[indexLetter].configure(image = renderHQ)
		labels[indexLetter].image = renderHQ

	def turnOffLamp(self, event, row, col):
		loadQ = Image.open(pathLamps+letter.lower()+".png")
		renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
		indexLetter = dictNumLet.get(letter.lower())
		labels[indexLetter].configure(image = renderHQ)
		labels[indexLetter].image = renderHQ