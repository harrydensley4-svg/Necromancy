from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead

class DeathKnight(WarriorUndead, CursedUndead):
    """
    Represenst a Death Knight undead type.
    It is an example of multiple inheritance.
    It inherits from both the WarriorUndead and CursedUndead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 0): The minimum health.
    MAX_HEALTH (int = 200): The maximum health.
    MIN_POWER (int = 40): The minimum power.
    MAX_POWER (int = 150): The maximum power.
    MAX_LEVEL (int = 150): The maximum level.
    HEALTH_GAIN (int = 7): The health gained during a level up.
    POWER_GAIN (int = 8): The power gained during a level up.

    Methods:
    --------
    combat_style()
        Returns the death knight combat style.
    compare_combat_style()
        Compares the combat style of each parent class.

    """
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
        """Returns the combat style of a Death Knight type."""
        return super().combat_style()

    def compare_combat_style(self):
        """Compares the combat style of both parent classes."""
        warrior = WarriorUndead.combat_style(self)
        cursed = CursedUndead.combat_style(self)

        return (
            f'Warrior style: {warrior}\n'
            f'Cursed Style: {cursed}\n'
        )
