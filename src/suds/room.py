import thing

class Room(Thing):
	'''
	A place where part of the game might take place.
	'''
	def __init__(self, name, desc, inv, entities):
		pass #@todo(aaon) code this

	def to_string(self):
		def entity_list(self): #should return "entity1, and entity2" ALWAYS USE OXFOED COMMA
			eta = len(entities) #entity amount
			entities_ = [entity.name for entity in entities]

		def item_list(self): #should return "item1, item2, and item 3"
			return "@todo(aaron): code this" #@todo(aaron): code this

		def exit_list(self): #should return "exit1, exit2, exit3, and exit4."
			return "@todo(aaron): code this" #@todo(aaron): code this

		header = "{}:\n{}".format(self.name, self.desc)
		entities_here = "The following entities are here: {}".format(entity_list())
		items_here = "Scattered around the ground is: {}".format(item_list())
		exits_here = "This room has the following obvious exits: {}".format(exit_list())

		final = "{}\n{}\n{}\n{}".format(hader, entities_here, items_here, exits_here)

class Exit(Thing): #@todo(aaron) decide if these should be a subclass of thing or not...
	'''
	The way rooms are connected.
	'''
	def __init__(self, room, obvious=True):
		self.room = room
		self.obvious = obvious #non-obvious exits should be hinted to in the room description