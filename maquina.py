
from rotores import Rotor

class Maquina:
	fastRotor: Rotor
	mediumRotor: Rotor
	slowRotor: Rotor
	reflector: Rotor

	def __init__(self, idx_fr=0, idx_mr=0, idx_sr=0):
		slow_rotor_indexes = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
		medium_rotor_indexes = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
		fast_rotor_indexes = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
		reflector_indexes = [8, 23, 20, 7, 5, 4, 25, 3, 0, 14, 12, 19, 10, 16, 9, 22, 13, 18, 17, 11, 2, 24, 15, 1, 21, 6]

		self.fastRotor = Rotor(idx_fr, fast_rotor_indexes)
		self.mediumRotor = Rotor(idx_mr, medium_rotor_indexes)
		self.slowRotor = Rotor(idx_sr, slow_rotor_indexes)
		self.reflector = Rotor(0, reflector_indexes)

	def cifrar(self, idx):
		idx_fr = self.fastRotor.push(idx)
		idx_mr = self.mediumRotor.push(idx_fr)
		idx_sr = self.slowRotor.push(idx_mr)
		idx_rr = self.reflector.push(idx_sr)
		idx_sr = self.slowRotor.antipush(idx_rr)
		idx_mr = self.mediumRotor.antipush(idx_sr)
		idx_fr = self.fastRotor.antipush(idx_mr)
		self.moveRotors()
		return idx_fr

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
	#print(mq.cifrar(0))
	print(mq.cifrar(15))
   
    