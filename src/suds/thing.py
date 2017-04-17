class Thing:
	'''
	Abstract class.
	Lots of 'Things' in this game will have a name and description.
	@todo(aaron) learn how to make a proper abstract class
	'''
	def __init__(self, name="Generic Thing", description="If you are seeing this then there was probably a bug."):
		self.name = name
		self.description = description

class Inventory:
	'''
	Might just get its own file in the future
	'''
	def __init__(self,max_size=0, items=[]):
		self.max_size = max_size
		self.items = items

	def empty_slots(self):
		'''
		returns how many empty slots are in the inventory
		a negative number indicates how many items are in the inventory over the maximum amount
		'''
		return max_size - len(items)

	def is_full(self):
		'''
		returns true if the inventory is full of items or is overflowing
		returns false otherwise
		'''
		return max_size >= len(items)

	def add_item(self, item):
		'''
		@params item is an item that is being added to the inventory
		'''
		if not self.is_full(): #todo(aaron) add an isinstance() call
			items.append(item)
			return None
		return item

	#@todo(aaron) add remove_item