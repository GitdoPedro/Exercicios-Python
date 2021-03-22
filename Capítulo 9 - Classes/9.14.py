from random import randint


class Die():
    def __init__(self,sides):
        self.sides = sides



    def roll_dice(self):
        print(randint(1,self.sides))


dado = Die(6)
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado = Die(10)
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado = Die(20)
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
