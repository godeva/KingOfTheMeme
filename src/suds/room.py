import thing

class Room(thing.Thing):
	'''
	A place where part of the game might take place.
	'''
	def __init__(self, name="Generic Room", desc="If you are seeing this Room then there was probably a bug.", inv=thing.Inventory(), entities=[]):
		Thing.__init__(self, name, desc)
		self.inv = inv
		self.entities = entities

	def to_string(self):

		#@todo(aaron) turn these into one function
		def entity_strlist(self): #should return "entity1, and entity2" ALWAYS USE OXFOED COMMA
			entities = [entity.name for entity in self.entities]
			last_entity = entities[-1]
			entities = entities[:-1]
			entities_desc = ", ".join(entities)
			entities_desc = "{}, and {}".format(entities_desc, last_entity)

		def item_strlist(self): #should return "item1, item2, and item 3"
			items = [item.name for item in self.inv.items]
			last_item = items[-1]
			items = items[:-1]
			items_desc = ", ".join(items)
			items_desc = "{}, and {}".format(items_desc, last_item)

		def exit_strlist(self): #should return "exit1, exit2, exit3, and exit4."
			exits = [exit.name for exit in self.exits]
			last_exit = exits[-1]
			exits = exits[:-1]
			exits_desc = ", ".join(exits)
			exits_desc = "{}, and {}".format(exits_desc, last_exit)

		header = "{}:\n{}".format(self.name, self.desc)
		entities_here = "The following entities are here: {}".format(entity_strlist())
		items_here = "Scattered around the ground is: {}".format(item_strlist())
		exits_here = "This room has the following obvious exits: {}".format(exit_strlist())

		final = "{}\n{}\n{}\n{}".format(header, entities_here, items_here, exits_here)


class Exit(Thing): #@todo(aaron) decide if these should be a subclass of thing or not...
	'''
	The way rooms are connected.
	'''
	def __init__(self, room, obvious=True):
		self.room = room
		self.obvious = obvious #non-obvious exits should be hinted to in the room description