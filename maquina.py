
from rotores import Rotor

class Maquina:
    fastRotor: Rotor
    mediumRotor: Rotor
    slowRotor: Rotor
    reflector: Rotor

    def __init__(self, idx_fr=0, idx_mr=0, idx_sr=0):
            
        aux_go = [1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14] 
        aux_return = [19,0,6,1,15,2,18,3,16,4,20,5,21,13,25,7,24,8,23,9,22,11,17,10,14,12]
        self.fastRotor = Rotor(idx_fr, aux_go, aux_return)
        """aux_go = [0,9,3,10,18,8,17,20,1,11,7,22,19,12,2,16,25,13,15,25,5,21,14,4]
        aux_return = [0,] """
        self.mediumRotor = Rotor(idx_mr, aux_go, aux_return)
        self.slowRotor = Rotor(idx_sr, aux_go, aux_return)
        self.reflector = Rotor(0, aux_go, aux_return)

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
    print(mq.cifrar(1))
   
    