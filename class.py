import os

from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire

from random import randint
# instantiate a hero object from the Hero class
the_hero = Hero()
# ditto
a_goblin = Goblin()
monsters = []

print "what is your name ?"

the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()

print "how many enimies do you want to challenge brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))

for i in range(0,number_of_enemies):
	rand_num = randint(0,1)
	if(rand_num == 1):
		monsters.append(Goblin())
	if(rand_num == 0):
		monsters.append(Vampire())	
#Run the game as long as BOTH characters have health (are alive)
while a_goblin.is_alive() and the_hero.is_alive():
	# game is on!
	os.system("clear")
	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	print "The %s has %d health and %d power." % (moster.name, a_goblin.power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> "
	user_input = raw_input()
	if user_input == "1":
		# User has chosen to attack. 
		# Take away health from the goblin based on hero power
		# goblin_health -= hero_power
		# the goblin class should be managing the goblins health
		# the hero is going to do the_hero.power damage to the goblin
		a_goblin.take_damage(the_hero.power)

	elif user_input == "2":
		# Hero is going to stand there like an idiot
		pass
	elif user_input == "3":
		print "Goodbye, coward! You remind me of Goober."
		os.system("say Goodbye, coward! You remind me of Goober.")
		# call break, to end the while loop
		break
	else:
		print "Invalid input %s" % user_input

	# goblins turn to attack!! (only if he's still alive)
	if a_goblin.get_health() > 0:
		# just like the goblin, the hero should be changing its own stuff
		# so... call take_damage on the hero
		# hero_health -= goblin_power
		the_hero.take_damage(a_goblin.power)

		print "The goblin hits you for %d damage" % a_goblin.power
		# goblin has attacked, now check to see if hero is still alive...
		if the_goblin.health <= 0:
			print "You have been killed by the weak goblin. Shame on you."