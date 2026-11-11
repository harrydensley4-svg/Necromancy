from warrior_undead import WarriorUndead

class SkeletonWarrior(WarriorUndead):
    """
    Represent a Skeleton Warrior.
    It inherits from the WarriorUndead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 20): The minimum health.
    MAX_HEALTH (int = 120): The maximum health.
    MIN_POWER (int = 10): The minimum power.
    MAX_POWER (int = 100): The maximum power.

    Methods:
    --------
    command()
        Returns the updated command for a skeleton warrior.
    """
    MIN_HEALTH = 20
    MAX_HEALTH = 120
    MIN_POWER = 10
    MAX_POWER = 100

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the updated command."""
        return super().command() + 'The skeleton warrior strikes.'