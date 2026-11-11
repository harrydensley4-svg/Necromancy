from undead import Undead

class PutridZombie(Undead):
    """
    Represents a putrid zombie.
    It inherits from the Undead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 30): The minimum health.
    MAX_HEALTH (int = 120): The maximum health.
    MIN_POWER (int = 10): The minimum power.
    MAX_POWER (int = 90): The maximum power.

    Methods:
    --------
    command():
        Returns the updated command for putrid zombie types.
    """
    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 10
    MAX_POWER = 90

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the overidden putrid zombie command."""
        return super().command() + 'The putrid zombie attacks.'