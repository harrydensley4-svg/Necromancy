from undead import Undead

class PutridZombie(Undead):
    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 10
    MAX_POWER = 90

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'The putrid zombie attacks.'