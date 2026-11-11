from resource_manager import ResourceManager
from summoning_ritual import SummoningRitual


class Necromancer:
    """
    Represents a necromancer object.
    This controls the resources, and summoning undead.

    Attributes
    ------
    MAX_UNDEAD (int = 10): The maximum undead creatures for each 
                           necromancer.
    name (str): The name of the necromancer.


    Methods
    ------
    get_name()
        Returns the name of the necromancer.
    get_rituals()
        Returns the list of rituals.
    get_resources()
        Returns the resource manager class.
    get_undead()
        Returns the list of the undead.
    get_id()
        Returns the necromancer ID.
    add_resources(necrotic, spirit, bone, flesh, ectoplasm)
        Add resources to the resource manager.
    add_ritual(ritual)
        Adds a ritual to the necromancers list of rituals
    summon_undead(ritual_id)
        Summon an undead, based on some summoning ritual_id.
    dismiss(undead_id)
        Remove an undead creature from the necromancers collection. 
    __find_undead(undead_id)
        A helper method used to find the undead creature in the list.
    level_up(undead_id)
        Level up the undead creature corresponding to that undead_id.
    """
    MAX_UNDEAD = 10

    def __init__(self, name):
        self.__name = name
        self.__resource = ResourceManager(0, 0, 0, 0, 0)
        self.__undead_list = []
        self.__rituals = []
        self.__id = 1

    def get_rituals(self):
        """Returns the list of rituals."""
        return self.__rituals

    def get_name(self):
        """Returns the necromancer name."""
        return self.__name

    def get_resource(self):
        """Returns. the resource manager."""
        return self.__resource

    def get_undead(self):
        """Returns the list of undead creatures."""
        return self.__undead_list

    def get_id(self):
        """Returns the necromancer's identifier."""
        return self.__id

    rituals = property(get_rituals)
    name = property(get_name)
    resource = property(get_resource)
    undead = property(get_undead)
    id = property(get_id)

    def add_resources(self, necrotic, spirit, bone, flesh, ectoplasm):
        """Add resources to the resource manager."""
        return self.__resource.collect_resources(
            necrotic, spirit, bone, flesh, ectoplasm
        )

    def add_ritual(self, ritual):
        if isinstance(ritual, SummoningRitual):
            self.__rituals.append(ritual)
            return True
        return False

    def __find_ritual(self, ritual_id):
        """Helper method to find a given ritual."""
        for ritual in self.__rituals:
            if ritual.ritual_ID == ritual_id:
                return ritual

        return None

    def summon_undead(self, ritual_id):
        """
        Summon an undead corresponding to a specific summoning ritual

        Parameters:
        ----------
        ritual : SummoningRitual
            The summoning ritual for the undead creature

        Returns
        -------
        Undead
            Returns the summoned undead.
            If the ritual can not be performed, it returns none.
        """
        ritual = self.__find_ritual(ritual_id)

        if ritual is None:
            return None

        if (ritual.check_ritual(self.__resource)
                and len(self.__undead_list) < self.MAX_UNDEAD):

            ritual.consume_resources(self.__resource)
            undead = ritual.create_undead(self.__id)
            self.__undead_list.append(undead)
            self.__id += 1
            return undead

        return None

    def dismiss(self, undead_id):
        """
        Dismiss an undead creature correpsonding to the id.

        Parameters:
        -----------
        undead_id : int
            The identifier for the undead creature to be removed.

        Returns
        --------
        bool
            If the undead is removed, return true.
            Otherwise, false is returned. 
        """
        undead = self.__find_undead(undead_id)
        if undead == None:
            return False
        self.__undead_list.remove(undead)
        return True

    def __find_undead(self, undead_id):
        """
        A helper method.
        Finds the undead instance based on the undead_id.

        Parameters:
        -----------
        undead_id : int
            The identifier for the undead to be found.

        Returns
        -------
        Undead
            If the undead instance can be found it returns it.
            Otherwise, it returns none.
        """
        for undead in self.__undead_list:
            if undead.undead_ID == undead_id:
                return undead
        return None

    def level_up(self, undead_id):
        """
        Levels up the undead corresponding to the undead id.

        Parameters
        ----------
        undead_id : int
            The unique identifier for the undead object to be 
            levelled up.

        Returns
        -------
        List[]
            Returns a list of the new level, 
            health, and power for the specific undead.
        """
        undead = self.__find_undead(undead_id)
        return undead.level_up()

    def __str__(self):
        """Returns a readable string description of the object. """
        new = ''
        for undead in self.__undead_list:
            new += 'UNDEAD ' + str(undead) + '\n'
        return (
            f'Resources: {self.__resource}' +
            '\n' + f'{self.__name.upper()}\'S ARMY:' +
            '\n' + f'{new}'
        )
