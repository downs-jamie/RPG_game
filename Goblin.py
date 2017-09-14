from Character import Character

class Goblin(Character):
	def __init__(self):
		super(Goblin,self).__init__('Goblin',6,2)
	# 	self.name = "Goblin"
	# 	self.health = 6
	# 	self.power = 2
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def get_health(self):
	# 	return self.health
	# def is_alive(self):
	# 	return self.health > 0		
	def do_a_dance(self):
		print "The goblin has done a dance. You are mezmerized and stupified, but not hurt!!"
