from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead

class DeathKnight(WarriorUndead, CursedUndead):
    MIN_HEALTH = 0
    MAX_HEALTH = 200
    MIN_POWER = 40
    MAX_POWER = 150
    MAX_LEVEL = 150
    HEALTH_GAIN = 7
    POWER_GAIN = 8

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def combat_style(self):
        return super().combat_style()

    def compare_combat_style(self):
        warrior = WarriorUndead.combat_style(self)
        cursed = CursedUndead.combat_style(self)

        return (
            f'Warrior style: {warrior}\n'
            f'Cursed Style: {cursed}\n'
        )


death_knight = DeathKnight(1, 'Death Knight', 60, 80)

print(DeathKnight.mro())

print(death_knight.combat_style())

print(death_knight.compare_combat_style())