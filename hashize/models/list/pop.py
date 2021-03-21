class Pop:
	def __init__(self, value, index, **others):
    	self.value = value
    	self.index = index
		
		for arg in others:
			exec('self.{} = {}'.format(arg, str(other[arg])))
			
	def __call__(self):
		return self.value
