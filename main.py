from files import *

# Introduce some different summmoning rituals.
# Each summoning ritual creates a different undead type 
# and requires different resources.
skeleton_warrior_ritual = SummoningRitual(
    "Skeleton Warrior", 1, SkeletonWarrior, 60, 40, 3, 0, 2, 0, 1)
vengeful_ghost_ritual = SummoningRitual(
    "Vengeful Ghost", 2, VengefulGhost, 40, 70, 0, 3, 0, 0, 2)
putrid_zombie_ritual = SummoningRitual(
    "Putrid Zombie", 3, PutridZombie, 80, 30, 1, 0, 0, 3, 2)
phantom_guardian_ritual = SummoningRitual(
    "Phantom Guardian", 4, PhantomGuardian, 100, 80, 2, 2, 1, 0, 3)
death_knight_ritual = SummoningRitual(
    'Death Knight', 5, DeathKnight, 150, 150, 80, 54, 13, 34, 45)
print(phantom_guardian_ritual)
print(skeleton_warrior_ritual)
print(putrid_zombie_ritual)
print(vengeful_ghost_ritual)
print(death_knight_ritual)

# Create a necromance instance.
necromancer = Necromancer('Harry')
print(necromancer.resource)

# Add some resources so that the summoning rituals can be executed.
necromancer.add_resources(1000, 1000, 1000, 1000, 1000)
print(necromancer.resource)

# Add the rituals to the necromancer
necromancer.add_ritual(skeleton_warrior_ritual)
necromancer.add_ritual(vengeful_ghost_ritual)
necromancer.add_ritual(putrid_zombie_ritual)
necromancer.add_ritual(phantom_guardian_ritual)
necromancer.add_ritual(death_knight_ritual)

# Summon the undead based on their ID
skeleton_warrior = necromancer.summon_undead(1)
vengeful_ghost = necromancer.summon_undead(2)
putrid_zombie = necromancer.summon_undead(3)
phantom_guardian = necromancer.summon_undead(4)
death_knight = necromancer.summon_undead(5)
print(necromancer)

# Level up the vengeful ghost.
# This instance corresponds to the undead_id of 2.
necromancer.level_up(2)

# Dismiss the putrid zombie from the necromancers list of undead.
necromancer.dismiss(3)
print(necromancer)

# Display the different commands for each individual undead instance.
for undead in necromancer.undead:
    print(undead.command())

print(necromancer)
