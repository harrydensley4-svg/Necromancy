from resource_manager import ResourceManager
from undead import Undead
from summoning_ritual import SummoningRitual
from necromancer import Necromancer
from skeleton_warrior import SkeletonWarrior
from venegful_ghost import VengefulGhost
from putrid_zombie import PutridZombie
from phantom_guardian import PhantomGuardian
from death_knight import DeathKnight
from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead

skeleton_warrior = SummoningRitual("Skeleton Warrior", SkeletonWarrior, 60, 40, 3, 0, 2, 0, 1)
vengeful_ghost = SummoningRitual( "Vengeful Ghost", VengefulGhost, 40, 70, 0, 3, 0, 0, 2)
putrid_zombie = SummoningRitual("Putrid Zombie", PutridZombie, 80, 30, 1, 0, 0, 3, 2)
phantom_guardian = SummoningRitual("Phantom Guardian", PhantomGuardian, 100, 80, 2, 2, 1, 0, 3)
death_knight = SummoningRitual('Death Knight', DeathKnight, 150, 150, 80, 54, 13, 34, 45)
print(phantom_guardian)
print(skeleton_warrior)
print(putrid_zombie)
print(vengeful_ghost)
print(death_knight)

necro = Necromancer('Harry')
print(necro.resource)
necro.add_resources(1000,1000,1000,1000,1000)
print(necro.resource)

skel = necro.summon_undead(skeleton_warrior)
veng = necro.summon_undead(vengeful_ghost)
zomb = necro.summon_undead(putrid_zombie)
phant = necro.summon_undead(phantom_guardian)
print(necro)
necro.level_up(2)
necro.dismiss(3)
print(necro)

for undead in necro.undead:
    print(undead.command())


dk = necro.summon_undead(death_knight)
print(necro)
print(dk)

# CHECK RELATIONSHIPS OF DEATHKNIGHT
print(isinstance(dk, WarriorUndead))
print(isinstance(dk, CursedUndead))
print(isinstance(dk, Undead))

print(dk.combat_style())
print(dk.compare_combat_style())

necro.level_up(5)

print(isinstance(CursedUndead, type))