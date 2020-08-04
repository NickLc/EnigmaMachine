import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from string import ascii_uppercase

from keyboard import Gui


TOTAL_ROTORS = 5

class Win1:
	def __init__(self, master):
		self.master = master
		self.master.geometry("500x400")
		self.frame = tk.Frame(self.master)
		
		# self.butnew("Click to open Window 2", "2", Win2)
		# self.butnew("Click to open Window 3", "3", m)
		
		self.frame.pack()

		#VARIABLES PARA EL PLUGBOARD
		self.dict = ascii_uppercase
		self.valuesRel =  list(self.dict)
		self.relation = []

		# VARIABLES PARA PODER CONSTRUIR LA MAQUINA ENIGMA
		self.comboBoxes_for_numbers = []
		self.comboBoxes_for_chars = []
		self.plugboard_conexiones = {}

		self.label1=ttk.Label(self.frame, text="Seleccione la cantidad de rotores:")
		self.label1.pack()
		self.spinbox1=ttk.Spinbox(self.frame, from_=0, to=5, width=10, state='readonly')        
		self.spinbox1.set(1)        
		self.spinbox1.pack()
		self.boton1=ttk.Button(self.frame, text="Configurar", command=self.sortear)
		self.boton1.pack()

	def crear_maquina_enigma(self):

		orden_rotores = []
		inicializacion_rotores = []

		for index,box in enumerate(self.comboBoxes_for_numbers):
			orden_rotores.append(int(box.get()))

		for index,box in enumerate(self.comboBoxes_for_chars):
			inicializacion_rotores.append(box.get())
	

		print(f"comboBoxes_for_numbers: {orden_rotores}")
		print(f"comboBoxes_for_chars: {inicializacion_rotores}")
		print(f"plugboard_conexiones: {self.plugboard_conexiones}")

		self.new = tk.Toplevel(self.master)
		Gui(self.new, orden_rotores, inicializacion_rotores, self.plugboard_conexiones)

	def sortear(self):
		for box_number, box_char in zip(self.comboBoxes_for_numbers, self.comboBoxes_for_chars):
			box_number.destroy()
			box_char.destroy()

		self.comboBoxes_for_numbers = []
		self.comboBoxes_for_chars = []

		options_number = int(self.spinbox1.get())  

		options = list(range(1,TOTAL_ROTORS + 1))
		char_options = list(ascii_uppercase)

		self.frame_for_numbers = tk.Frame(self.master)
		self.frame_for_numbers.pack()

		self.rotores_orden=ttk.Label(self.frame_for_numbers, text="Orden de los rotores\n(izq a der) :")
		self.rotores_orden.pack(side = tk.LEFT)

		for i in range(options_number):
			numberChosen = ttk.Combobox(self.frame_for_numbers, width = 5)
			numberChosen['values'] = options
			numberChosen.current() 
			numberChosen.pack(side = tk.LEFT)
			self.comboBoxes_for_numbers.append(numberChosen)



		self.frame_for_chars = tk.Frame(self.master)
		self.frame_for_chars.pack()

		self.rotores_inicializacion=ttk.Label(self.frame_for_chars, text="Inicializar rotores:")
		self.rotores_inicializacion.pack(side = tk.LEFT)
		
		for i in range(options_number):
			charChosen = ttk.Combobox(self.frame_for_chars, width = 5)
			charChosen['values'] = char_options
			charChosen.current() 
			charChosen.pack(side = tk.LEFT)
			self.comboBoxes_for_chars.append(charChosen)

		self.generate_plugboard_selection()

	def butnew(self, text, number, _class):
		tk.Button(self.frame, text = text, command= lambda: self.new_window(number, _class)).pack()

	def new_window(self, number, _class):
		self.new = tk.Toplevel(self.master)
		_class(self.new, number)

	def generate_plugboard_selection(self):
		self.frame_for_plugboard_options = tk.Frame(self.master)
		self.frame_for_plugboard_options.pack()

		self.label1=ttk.Label(self.frame_for_plugboard_options, text="Conectar:")
		self.label1.pack(side = tk.LEFT)
		
		self.comboA = ttk.Combobox(self.frame_for_plugboard_options, width = 5)
		self.comboA['values'] = list(ascii_uppercase)
		self.comboA.current() 
		self.comboA.pack(side = tk.LEFT)

		self.label2=ttk.Label(self.frame_for_plugboard_options, text="con:")
		self.label2.pack(side = tk.LEFT)

		self.comboB = ttk.Combobox(self.frame_for_plugboard_options, width = 5)
		self.comboB['values'] = list(ascii_uppercase)
		self.comboB.current() 
		self.comboB.pack(side = tk.LEFT)

		self.conectar_plugboard=ttk.Button(self.frame_for_plugboard_options, text="Agregar", command=self.agregar_plugboard)
		self.conectar_plugboard.pack()

		self.frame_for_plugboard_scroller = tk.Frame(self.master)
		self.frame_for_plugboard_scroller.pack()

		self.generador_maquina=ttk.Button(self.frame_for_plugboard_scroller, text="Crear maquina", command=self.crear_maquina_enigma)
		self.generador_maquina.pack(side= tk.BOTTOM)

		self.scrollTxtRel = scrolledtext.ScrolledText(self.frame_for_plugboard_scroller,width=6,height=10)
		self.scrollTxtRel.pack(side= tk.BOTTOM)
		
	def agregar_plugboard(self):
		relA = self.comboA.get()
		relB = self.comboB.get()

		if(len(self.valuesRel)==0):
			messagebox.showinfo('Mensaje Info', 'Se establecio todas las conexiones') 

		elif(relA == relB):
			messagebox.showerror('Mensaje Error', 'Debes conectar dos caracteres diferentes') 

		elif(relA not in list(self.dict) or relB not in list(self.dict)):
		    messagebox.showerror('Mensaje Error', 'Debes ingresar caracteres correctos') 

		else:
			# self.scrollTxtRel.delete(0.0, tk.END)
			try:
				self.valuesRel.remove(relA)
				try:
					self.valuesRel.remove(relB)
					self.comboA['values'] = self.valuesRel
					self.comboB['values'] = self.valuesRel
					newRel = [relA, relB]
					
					# agregando conexion al diccionario de conexiones
					self.plugboard_conexiones[relA] = relB

					self.relation.append(newRel)
					self.scrollTxtRel.insert(tk.INSERT, ','.join(newRel) + '\n')	
					if(len(self.valuesRel)==0):
						messagebox.showinfo('Mensaje Info', 'Se establecio todas las conexiones') 

				except:
					self.valuesRel.append(relA)
					messagebox.showerror('Mensaje Error', 'El valor '+relB+' ya esta en uso')
			except:
				messagebox.showerror('Mensaje Error', 'El valor '+relA+' ya esta en uso')
			
			# Put new string into of stroll 
			

root = tk.Tk()
root.title("MAQUINA ENIGMA UNI")
app = Win1(root)
root.mainloop()