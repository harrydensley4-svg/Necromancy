from warrior_undead import WarriorUndead

class PhantomGuardian(WarriorUndead):
    """
    Represents a Phantom Guardian undead type.
    This inherits from the WarriorUndead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 30): The minimum health for a phantom guardian.
    MAX_HEALTH (int = 120): The maximum health for a phantom guardian.
    MIN_POWER (int = 20): The minimum power for a phantom guardian.
    MAX_POWER (int = 100): The maximum power for a phantom guardian.

    Methods:
    --------
    command()
        Builds upon the command() method found in the WarriorUndead class.
    """
    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 20
    MAX_POWER = 100

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the phantom guardian command."""
        return super().command() + 'The Phantom Guradian protects its master.'

        