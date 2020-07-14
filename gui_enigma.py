import tkinter as tk
from maquina import Maquina
from string import ascii_uppercase

class Aplicacion:
	def __init__(self):
		self.chars = "ABCDEFG"
		self.mq = Maquina()
		self.ventana1=tk.Tk()
		self.ventana1.title("Prueba")
		self.label1=tk.Label(self.ventana1, text="Encriptando...")
		self.label1.grid(column=0, row=0)

		self.buttons = []

		for index, char in enumerate(ascii_uppercase):
			self.buttons.append(tk.Button(self.ventana1, text=char))
		

		for index, button in enumerate(self.buttons):
			button.grid(column=index, row=1)
			button['command'] = lambda ind = index : self.change_label(ind)

		self.ventana1.mainloop()


	def change_label(self,texto):
		print(f"Texto: {texto}")
		self.label1.configure(text = ascii_uppercase[self.mq.cifrar(texto)])

aplicacion1=Aplicacion()