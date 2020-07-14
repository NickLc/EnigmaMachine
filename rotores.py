import random

class Rotor:
    #permutacion de rel en cada giro
    dest_go: list
    count: int

    def __init__(self, ind_init=0, dest_go=[]):
        
        self.count = 0
        self.dest_go = dest_go

        if(ind_init != 0):
            self.dest_go = self.dest_go[ind_init:] + self.dest_go[:ind_init]

        if(len(dest_go) == 0):
            self.dest_go = self.set_random_arr()

    def move(self):
        aux_dest_go = self.dest_go[0]
        self.dest_go = self.dest_go[1:]+ [aux_dest_go]
            

    def set_random_arr(self):
        new_rel = list(range(len(26)))
        for i in range(len(new_rel)):
            index = random.randint(0,len(new_rel)-1)
            new_rel[i], new_rel[index] = new_rel[index], new_rel[i]
        return new_rel    
    
    def push(self, idx):
        new_idx = self.dest_go[idx]
        return new_idx

    def antipush(self, reflected_value):
        new_idx = self.dest_go.index(reflected_value)
        return new_idx


if __name__ == "__main__":
    # default start in 0
    aux_go = [1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14] 
    
    rt = Rotor(1, aux_go)
    print(rt.antipush(0))
 
