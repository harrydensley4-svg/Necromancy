from resource_manager import ResourceManager
from undead import Undead
from summoning_ritual import SummoningRitual
from necromancer import Necromancer

skeleton_warrior = SummoningRitual("Skeleton Warrior","Skeleton Warrior",60,40,3,0,2,0,1)
vengeful_ghost = SummoningRitual( "Vengeful Ghost","Vengeful Ghost",40,70,0,3,0,0, 2)
putrid_zombie = SummoningRitual("Putrid Zombie","Putrid Zombie",80,30, 1,0,0,3,2)
phantom_guardian = SummoningRitual("Phantom Guardian", "Phantom Guardian", 100, 80,2, 2,1, 0,3)

print(phantom_guardian)
print(skeleton_warrior)
print(putrid_zombie)
print(vengeful_ghost)
necro = Necromancer('Harry')
necro.add_resources(100,100,100,100,100)
necro.summon(skeleton_warrior)
necro.summon(vengeful_ghost)
necro.summon(putrid_zombie)
necro.summon(phantom_guardian)
necro.level_up(2)
necro.dismiss(3)
print(necro)