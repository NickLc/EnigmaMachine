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
	def __init__(self):
		self.win = Tk()
		self.win.title("ENIGMA MACHINE")
		self.win.configure(bg= bgColor)
		self.machine = None
		self.machine_enabled = False

		self.rotors_frames = Frame(self.win)

		self.fastRotorOption = tk.StringVar() 
		self.fastRotorCombo = tk.ttk.Combobox(self.rotors_frames, width = 5, textvariable = self.fastRotorOption) 
		self.fastRotorCombo['values'] = list(ascii_uppercase)
		self.fastRotorCombo.pack(side=LEFT)
		self.fastRotorCombo.current() 

		self.mediumRotorOption = tk.StringVar() 
		self.mediumRotorOption = tk.ttk.Combobox(self.rotors_frames, width = 5, textvariable = self.mediumRotorOption) 
		self.mediumRotorOption['values'] = list(ascii_uppercase)
		self.mediumRotorOption.pack(side=LEFT)
		self.mediumRotorOption.current() 

		self.slowRotorOption = tk.StringVar() 
		self.slowRotorOption = tk.ttk.Combobox(self.rotors_frames, width = 5, textvariable = self.slowRotorOption) 
		self.slowRotorOption['values'] = list(ascii_uppercase)
		self.slowRotorOption.pack(side=LEFT)
		self.slowRotorOption.current() 

		self.createMachineButton = Button(self.rotors_frames, text = "Create machine e.e",bg='#494d70',activebackground="#494d70", borderwidth =0, command=self.create_machine)
		self.createMachineButton.pack(side=LEFT)

		self.rotors_frames.pack(side=TOP)


		self.render_lamps()
		self.render_buttons()
		self.win.mainloop()

	def create_machine(self):
		fr_char = ascii_uppercase[self.fastRotorCombo.current()] if self.fastRotorCombo.current() > 0 else 'A'
		mr_char = ascii_uppercase[self.mediumRotorOption.current()] if self.mediumRotorOption.current() > 0 else 'A'
		sr_char = ascii_uppercase[self.slowRotorOption.current()] if self.slowRotorOption.current() > 0 else 'A'

		self.machine = Maquina(fr_char, mr_char, sr_char)
		self.machine_enabled = True

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
		if self.machine_enabled:
			letter = self.machine.cifrar(keyboard_letters[row][col].upper())
			loadQ = Image.open(pathLamps+letter.lower()+"_h.png")
			renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
			indexLetter = dictNumLet.get(letter.lower())
			labels[indexLetter].configure(image = renderHQ)
			labels[indexLetter].image = renderHQ

	def turnOffLamp(self, event, row, col):
		if self.machine_enabled:
			loadQ = Image.open(pathLamps+letter.lower()+".png")
			renderHQ = ImageTk.PhotoImage(loadQ.resize((50,50),Image.ANTIALIAS))
			indexLetter = dictNumLet.get(letter.lower())
			labels[indexLetter].configure(image = renderHQ)
			labels[indexLetter].image = renderHQ


gui = Gui()