import random
from string import ascii_uppercase

class Rotor:
    #permutacion de rel en cada giro
    dest_go: str
    count: int

    def __init__(self, char_init='A', dest_go=""):
        
        self.count = 0
        self.dest_go = dest_go

        if(char_init != 'A'):
            ind_init = ascii_uppercase.find(char_init)
            self.dest_go = self.dest_go[ind_init:] + self.dest_go[:ind_init]

        if(len(dest_go) == 0):
            self.dest_go = self.set_random_string()

    def move(self):
        aux_dest_go = self.dest_go[0]
        self.dest_go = self.dest_go[1:] + aux_dest_go
            
    def set_random_string(self):
        return "BDFHJLCPRTXVZNYEIWGAKMUSQO"    
    
    def push(self, char_to_encrypt):
        new_char = self.dest_go[ascii_uppercase.find(char_to_encrypt)]
        return new_char

    def antipush(self, reflected_char):
        new_char = ascii_uppercase[self.dest_go.find(reflected_char)]
        return new_char


if __name__ == "__main__":
    # default start in 0
    aux_go = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    
    rt = Rotor('B', aux_go)
    print(rt.antipush('B'))
 
