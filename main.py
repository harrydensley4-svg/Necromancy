from files import *

skeleton_warrior_ritual = SummoningRitual("Skeleton Warrior", SkeletonWarrior, 60, 40, 3, 0, 2, 0, 1)
vengeful_ghost_ritual = SummoningRitual( "Vengeful Ghost", VengefulGhost, 40, 70, 0, 3, 0, 0, 2)
putrid_zombie_ritual = SummoningRitual("Putrid Zombie", PutridZombie, 80, 30, 1, 0, 0, 3, 2)
phantom_guardian_ritual = SummoningRitual("Phantom Guardian", PhantomGuardian, 100, 80, 2, 2, 1, 0, 3)
death_knight_ritual = SummoningRitual('Death Knight', DeathKnight, 150, 150, 80, 54, 13, 34, 45)
print(phantom_guardian_ritual)
print(skeleton_warrior_ritual)
print(putrid_zombie_ritual)
print(vengeful_ghost_ritual)
print(death_knight_ritual)

necromancer = Necromancer('Harry')
print(necromancer.resource)
necromancer.add_resources(1000,1000,1000,1000,1000)
print(necromancer.resource)

skeleton_warrior = necromancer.summon_undead(skeleton_warrior_ritual)
vengeful_ghost = necromancer.summon_undead(vengeful_ghost_ritual)
putrid_zombie = necromancer.summon_undead(putrid_zombie_ritual)
phantom_guardian = necromancer.summon_undead(phantom_guardian_ritual)
death_knight = necromancer.summon_undead(death_knight_ritual)
print(necromancer)
necromancer.level_up(2)
necromancer.dismiss(3)
print(necromancer)

for undead in necromancer.undead:
    print(undead.command())

print(necromancer)

# CHECK RELATIONSHIPS OF DEATHKNIGHT
print(isinstance(death_knight, WarriorUndead))
print(isinstance(death_knight, CursedUndead))
print(isinstance(death_knight, Undead))

print(death_knight.combat_style())
print(death_knight.compare_combat_style())

necromancer.level_up(5)

print(isinstance(CursedUndead, type))