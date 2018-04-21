import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def roll_die(self):
        return random.randint(1,12) * self.level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)


class Wizard(Creature):
    pass


class SmallAnimal(Creature):
    def roll_die(self):
        return super().roll_die() / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def roll_die(self):
        fire_modifier = 2 if self.breathes_fire else 1
        scales_modifier = self.scaliness / 10
        return super().roll_die() * fire_modifier * scales_modifier


