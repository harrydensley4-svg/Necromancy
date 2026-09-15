class Undead:
    """
    Represents the creation of an undead warrior

    Attributes
    -------
    undead_ID : int
    name : str
    health : int
    power : int

    Methods
    -------
    level_up()
    """
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100
    MAX_LEVEL = 100
    HEALTH_GAIN = 5
    POWER_GAIN = 5

    def __init__(self, undead_ID, name, health, power):
        self.__undead_ID = undead_ID
        self.__name = name
        self.__health = health
        self.__power = power
        self.__level = 1

    def get_undead_ID(self):
        return self.__undead_ID

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level

    undead_ID = property(get_undead_ID)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def command(self):
        return f'{self.__name} follows its masters command. '

    def level_up(self):
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

    def __str__(self):
        """Returns a readable string description. """
        return f'ID: {self.__undead_ID}, Name: {self.__name}, Level: {self.__level}, Health: {self.__health}, Max Health: {self.MAX_HEALTH}, Power: {self.__power}, Max Power: {self.MAX_POWER}'