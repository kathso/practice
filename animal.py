class Animal:
	# Base Class = Animal = parent
	#       /     /   \
	#    Bird    Dog   Cat = Derived classes = children
	
	def __init__(self):
		# type: int
		# Number of legs our animal has
		self.legs = None
		# type: bool
		# Does our animal have a tail
		self.tail = None

	def set_legs(self, num_legs):
	   if type(num_legs) is int:
	      self.legs = num_legs
	   else:
	      print('num_legs should be an int!')

	def set_tail(self, is_tail):
           if type(is_tail) is bool:
              self.tail = is_tail
           else:
              print('is_tail should be a bool')

        def get_legs(self):
           return self.legs

        def get_tail(self):
           return self.tail
