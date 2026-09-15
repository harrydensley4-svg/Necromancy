from warrior_undead import WarriorUndead

class PhantomGuardian(WarriorUndead):
    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 20
    MAX_POWER = 100

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'The Phantom Guradian protects its master.'

        