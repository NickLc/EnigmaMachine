from string import ascii_uppercase
from rotores import Rotor
from plugboard import Plugboard

class Maquina:
	list_of_rotors: list
	reflector: Rotor
	plugboard: Plugboard

	def __init__(self, nmrRotors, initCharRotors, cables):

		self.list_of_rotors = []
		reflector_indexes = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

		#rotors_orders = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
		rotors_orders = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "RMSLNIXCYPTZAHJOUFDBQGWKVE", "ZIHFQEMASYPOWDBKVXCNLRTUGJ"]
		
		# "RMSLNIXCYPTZAHJOUFDBQGWKVE", "ZIHFQEMASYPOWDBKVXCNLRTUGJ"
		# imaginemos nmrRotor = [2,1] y charRotor = ['C','G']

		for index, (nmrRotor, charRotor) in enumerate(zip(nmrRotors, initCharRotors)):
			self.list_of_rotors.append(Rotor(charRotor, rotors_orders[nmrRotor-1]))			    

		self.plugboard = Plugboard(cables)
		self.reflector = Rotor('A', reflector_indexes)

	def cifrar(self, char):
		char_processed = char

		char_processed = self.plugboard.procesar_caracter(char_processed)

		for rotor in self.list_of_rotors:
			char_processed = rotor.push(char_processed)

		char_processed = self.reflector.push(char_processed)

		for rotor in self.list_of_rotors[::-1]:
			char_processed = rotor.antipush(char_processed)

		char_processed = self.plugboard.procesar_caracter(char_processed)	

		self.moveListOfRotors()

		"""
		for rotor in self.list_of_rotors:
			print(f"Rotor: {rotor.dest_go} count: {rotor.count}")
		"""
		
		return char_processed

	def moveListOfRotors(self):
		for index,rotor in enumerate(self.list_of_rotors):
			if index == 0:
				rotor.move()
				rotor.count += 1
			else:
				if self.list_of_rotors[index-1].count == 26:
					self.list_of_rotors[index-1].count = 0
					rotor.move()
					rotor.count += 1

if __name__ == "__main__":

	rotors_numbers = [2,1,3,5,4]
	init_chars = ['C','F','G','B','M']
	cables = {
	'A' : 'C',
	'B' : 'F',
	'G' : 'H'
	}

	mq = Maquina(rotors_numbers, init_chars, cables)
	
	#testing
	big_string = ascii_uppercase * 25

	big_string_encrypted = ""

	for char in big_string:
		big_string_encrypted += mq.cifrar(char)

	print("\n")
	print("#"*100)

	print(f"Big string big_string_encrypted: {big_string_encrypted}")

	mq_for_decryption = Maquina(rotors_numbers, init_chars, cables)

	print(f"Big string decrypted: ")
	for char in big_string_encrypted:
		print(mq_for_decryption.cifrar(char), end = "")		