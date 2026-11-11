from cursed_undead import CursedUndead

class VengefulGhost(CursedUndead):
    """"
    This class represents a Vengeful Ghost
    It inherits from the CursedUndead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 10): The minimum health.
    MAX_HEALTH (int = 100): The maximum health.
    MIN_POWER (int = 30): The minimum power.
    MAX_POWER (int = 120): The maximum power.

    Methods:
    --------
    command()
        Returns the updated command for a vengeful ghost type.
    """
    MIN_HEALTH = 10
    MAX_HEALTH = 100
    MIN_POWER = 30
    MAX_POWER = 120

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the overidden vengeful ghost command."""
        return super().command() + 'The ghost seeks its revenge.'