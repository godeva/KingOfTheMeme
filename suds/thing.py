class Thing:
	'''
	Abstract class.
	Lots of 'Things' in this game will have a name and description.
	@todo(aaron) learn how to make a proper abstract class
	'''
	def __init__(self, name="Generic Thing", description="If you are seeing this then there was probably a bug."):
		self.name = name
		self.description = description