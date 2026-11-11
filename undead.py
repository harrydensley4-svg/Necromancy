class Undead:
    """
    Represents the creation of an undead warrior.

    Attributes
    ----------
    MIN_HEALTH (int = 0)
    MAX_HEALTH (int = 100)
    MIN_POWER (int = 0)
    MAX_POWER (int = 100)
    MAX_LEVEL (int = 100)
    HEALTH_GAIN (int = 5)
    POWER_GAIN (int = 5)
    undead_ID (int): The unique identifier for each undead.
    name (str): The name of the undead warrior.
    health (int): The health of the undead.
    power (int): The power of the undead.

    Methods
    --------
    get_undead_id():
        Returns the unique undead identifier.
    get_name():
        Returns the name of the undead.
    get_health():
        Returns the health of the undead.
    get_power():
        Returns the power of the undead.
    get_level():
        Returns the level of the undead.
    command():
        Returns a sting.
    level_up():
        levels up the undead creature.
    """
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100
    MAX_LEVEL = 100
    HEALTH_GAIN = 5
    POWER_GAIN = 5

    def __init__(self, undead_ID, name, health, power):
        if not isinstance(undead_ID, int) or undead_ID <= 0:
            raise ValueError('Undead ID must be a positive integer')

        if not isinstance(name, str) or name.strip() == '':
            raise ValueError('Undead name cannot be empty')

        if not isinstance(health, int) or not self.MIN_HEALTH <= health <= self.MAX_HEALTH:
            raise ValueError('Health must be between 0 and 100')

        if not isinstance(power, int) or not self.MIN_POWER <= power <= self.MAX_POWER:
            raise ValueError('Power must be between 0 and 100')
    
        self.__undead_ID = undead_ID
        self.__name = name
        self.__health = health
        self.__power = power
        self.__level = 1

    def get_undead_ID(self):
        """Returns the unique undead ID."""
        return self.__undead_ID

    def get_name(self):
        """Returns the name of the undead."""
        return self.__name

    def get_health(self):
        """Returns the health of the undead."""
        return self.__health

    def get_power(self):
        """Returns the power of the undead."""
        return self.__power

    def get_level(self):
        """Returns the level of the undead."""
        return self.__level

    undead_ID = property(get_undead_ID)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def command(self):
        """Returns a simple command that is overridden by child classes."""
        return f'{self.__name} follows its masters command. '

    def level_up(self):
        """
        Levels up the undead.

        Returns
        -------
        list
            Returns the undeads new level, power, and health.
        """
        if self.__level < self.MAX_LEVEL:
            self.__level += 1
        if self.__health + self.HEALTH_GAIN <= self.MAX_HEALTH:
            self.__health += self.HEALTH_GAIN
        else:
            self.__health = self.MAX_HEALTH

        if self.__power + self.POWER_GAIN <= self.MAX_POWER:
            self.__power += self.POWER_GAIN
        else:
            self.__power = self.MAX_POWER
        return [self.__level, self.__power, self.__health]

    def __str__(self):
        """Returns a readable string description. """
        return f'ID: {self.__undead_ID}, Name: {self.__name}, Level: {self.__level}, Health: {self.__health}, Max Health: {self.MAX_HEALTH}, Power: {self.__power}, Max Power: {self.MAX_POWER}'