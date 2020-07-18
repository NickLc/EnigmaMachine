from string import ascii_uppercase
from rotores import Rotor

class Maquina:
	fastRotor: Rotor
	mediumRotor: Rotor
	slowRotor: Rotor
	reflector: Rotor


	def __init__(self, char_fr='A', char_mr='A', char_sr='A'):
		slow_rotor_indexes = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
		medium_rotor_indexes = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
		fast_rotor_indexes = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
		reflector_indexes = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

		self.fastRotor = Rotor(char_fr, fast_rotor_indexes)
		self.mediumRotor = Rotor(char_mr, medium_rotor_indexes)
		self.slowRotor = Rotor(char_sr, slow_rotor_indexes)
		self.reflector = Rotor('A', reflector_indexes)

	def cifrar(self, char):
		char_fr = self.fastRotor.push(char)
		char_mr = self.mediumRotor.push(char_fr)
		char_sr = self.slowRotor.push(char_mr)
		char_rr = self.reflector.push(char_sr)
		char_sr = self.slowRotor.antipush(char_rr)
		char_mr = self.mediumRotor.antipush(char_sr)
		char_fr = self.fastRotor.antipush(char_mr)
		self.moveRotors()
		return char_fr

	def moveRotors(self):
		self.fastRotor.move()
		self.fastRotor.count += 1

		if(self.fastRotor.count == 26):
			self.fastRotor.count = 0
			self.mediumRotor.move()
			self.mediumRotor.count += 1

		if(self.mediumRotor.count == 26):
			self.mediumRotor.count = 0
			self.slowRotor.count += 1
			self.slowRotor.move()

            
if __name__ == "__main__":
	mq = Maquina()
	
	#testing
	big_string = ascii_uppercase + ascii_uppercase[::-1]

	big_string_encrypted = ""

	for char in big_string:
		big_string_encrypted += mq.cifrar(char)

	print("\n")
	print("#"*100)

	print(f"Big string big_string_encrypted: {big_string_encrypted}")

	mq_for_decryption = Maquina()

	print(f"Big string decrypted: ")
	for char in big_string_encrypted:
		print(mq_for_decryption.cifrar(char), end = "")		