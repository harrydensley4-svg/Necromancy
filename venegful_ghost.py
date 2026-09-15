from cursed_undead import CursedUndead

class VengefulGhost(CursedUndead):
    MIN_HEALTH = 10
    MAX_HEALTH = 100
    MIN_POWER = 30
    MAX_POWER = 120

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'The ghost seeks its revenge.'