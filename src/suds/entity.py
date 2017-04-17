import thing

class Entity(Thing):
	'''
	player, monster, basicaly anything in the game that can take an action
	'''
	#A : attack
	#D : defence
	
	#phy : physical
	phyA = 0
	phyD = 0

	#mag : magical
	magA = 0
	magD = 0

	#uti : utility
	utiA = 0
	utiD = 0

	#prio : priority (higher = acts sooner)
	prio = 0

	#zoom : how fast? basicaly how many actions they get per round
	#this doesn't have to be an integer. it can easily be 1.1
	#be careful when having a bunch of multipling effects...
	#1.5 x 1.5 = 2.25
	#THEY STACK UP FASTTT
	zoom = 1

	def __init__(self, name="Generic Entity", desc="If you are seeing this Entity then there was probably a bug.", inv=thing.Inventory()):
		pass #@todo(aaon) code this
