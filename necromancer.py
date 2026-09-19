from resource_manager import ResourceManager
from summoning_ritual import SummoningRitual

class Necromancer:
    """
    represents a necromancer

    Attributes
    ------
    name : str

    Methods
    ------
    add_resources()
    summon()
    dismiss()
    __find_undead()
    level_up()
    """
    MAX_UNDEAD = 10

    #TODO: TAKE A LIST OF RESOURCES AND THEN SPLIT UP INTO ITS CONSTITUENT PARTS AND THEN FEED THROUGH RESOURCEMANAGER
    def __init__(self, name):
        self.__name = name
        # Begin with no resources (?) Not sure if this is right.
        self.__resource = ResourceManager(0,0,0,0,0)
        self.__undead_list = []
        self.__id = 1

    def get_name(self):
        return self.__name

    def get_resource(self):
        return self.__resource

    def get_undead(self):
        return self.__undead_list

    def get_id(self):
        return self.__id

    name = property(get_name)
    resource = property(get_resource)
    undead = property(get_undead)
    id = property(get_id)

    def add_resources(self, necrotic, spirit, bone, flesh, ectoplasm):
        return self.__resource.collect_resources(necrotic, spirit, bone, flesh, ectoplasm)

    def summon_undead(self, ritual):
        if isinstance(ritual, SummoningRitual):
            if ritual.check_ritual(self.__resource):
                ritual.consume_resources(self.__resource)
                undead = ritual.create_undead(self.__id)
                self.__undead_list.append(undead)
                self.__id += 1
                return undead
            else:
                print('Not enough resources')
        else:
            print('Not valid')

    def dismiss(self, undead_id):
        undead = self.__find_undead(undead_id)
        if undead == None:
            return False
        self.__undead_list.remove(undead)
        return True

    def __find_undead(self, undead_id):
        # Helper method
        for undead in self.__undead_list:
            if undead.undead_ID == undead_id:
                return undead
        return None

    def level_up(self, undead_id):
        undead = self.__find_undead(undead_id)
        return undead.level_up()

    def __str__(self):
        """Returns a readable string description of the object. """
        new = ''
        for undead in self.__undead_list:
            new += 'UNDEAD ' + str(undead) + '\n'
        return f'Resources: {self.__resource}' + '\n' + f'{self.__name.upper()}\'S ARMY:'+ '\n' + f'{new}'
    