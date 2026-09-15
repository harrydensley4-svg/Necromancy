from resource_manager import ResourceManager
from undead import Undead
from summoning_ritual import SummoningRitual
from necromancer import Necromancer
from skeleton_warrior import SkeletonWarrior
from venegful_ghost import VengefulGhost
from putrid_zombie import PutridZombie
from phantom_guardian import PhantomGuardian

skeleton_warrior = SummoningRitual("Skeleton Warrior", SkeletonWarrior, 60, 40, 3, 0, 2, 0, 1)
vengeful_ghost = SummoningRitual( "Vengeful Ghost", VengefulGhost, 40, 70, 0, 3, 0, 0, 2)
putrid_zombie = SummoningRitual("Putrid Zombie", PutridZombie, 80, 30, 1, 0, 0, 3, 2)
phantom_guardian = SummoningRitual("Phantom Guardian", PhantomGuardian, 100, 80, 2, 2, 1, 0, 3)
print(phantom_guardian)
print(skeleton_warrior)
print(putrid_zombie)
print(vengeful_ghost)

necro = Necromancer('Harry')
print(necro.resource)
necro.add_resources(100,100,100,100,100)
print(necro.resource)

necro.summon_undead(skeleton_warrior)
necro.summon_undead(vengeful_ghost)
necro.summon_undead(putrid_zombie)
necro.summon_undead(phantom_guardian)
print(necro)
necro.level_up(2)
necro.dismiss(3)
print(necro)

for undead in necro.undead:
    print(undead.command())
