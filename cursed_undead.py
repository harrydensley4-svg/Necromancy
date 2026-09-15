from undead import Undead

class CursedUndead(Undead):
    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'It casts a curse. '

    def __str__(self):
        return 'Cursed Undead' + super().__str__()