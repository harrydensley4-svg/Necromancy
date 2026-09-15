from warrior_undead import WarriorUndead

class SkeletonWarrior(WarriorUndead):
    MIN_HEALTH = 20
    MAX_HEALTH = 120
    MIN_POWER = 10
    MAX_POWER = 100

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'The skeleton warrior strikes.'