from string import ascii_uppercase

class Plugboard:

	cableado : dict


	def __init__(self, cableado = {}):
		self.cableado = cableado


	def procesar_caracter(self, char):
		char_procesado = ''

		cableado_claves = list(self.cableado.keys()) 
		cableado_valores = list(self.cableado.values()) 

		if char in cableado_claves:
			char_procesado = self.cableado[char]
		elif char in cableado_valores:
			char_procesado = cableado_claves[cableado_valores.index(char)]
		else:
			char_procesado = char

		return char_procesado


if __name__ == "__main__":
    # default start in 0
    cables = {
    'A' : 'C',
    'B' : 'F',
    'G' : 'H',
    'L' : 'N',
    'K' : 'R',
    'Q' : 'E'
    }
    

    plugboard = Plugboard(cables)

    for char in ascii_uppercase:
    	print(f"Char: {char} ---> procesado: {plugboard.procesar_caracter(char)}")