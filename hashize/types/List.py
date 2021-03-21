class List:
	def __init__(self, *args, **kwargs):

		if 'list' in kwargs:
			self.list = kwargs['list']

		else:
			self.list = []
			for key, value in kwargs:
				self.list.append([key, value])

		if args:
			self.list = list(args)

	def indexes(self):
		return list(range(self.__len__()))

	def __repr__(self):
		return 'HashizeList(%s)' % self.list

	def __str__(self):
		return str(self.list)

	def __int__(self):
		return self.__len__()

	def __set__(self):
		return set(self.list)

	def __reversed__(self):
		return self.reverse()

	def __len__(self):
		return len(self.list)

	def __getitem__(self, index):
		if type(index) == str:
			try:
				index = int(index)
				return self.list[index]
			except ValueError:
				return self.list[self.list.index(index, 0)]

		if type(index) == slice:
			try:
				start = int(index.start)
			except (ValueError, TypeError):
				start = 0
			try:
				stop = int(index.stop)
			except (ValueError, TypeError):
				stop = self.__len__() ## basically the end
			try:
				step = int(index.stop)
			except (ValueError, TypeError):
				step = 1

			return self.list[start:stop:step]

		return self.list[index]

	def __setitem__(self, index, object):
		if index not in self.indexes():
			if type(index) != int:
				index = int(index)

			gap = index - self.__len__()
			for i in range(gap):
				self.list.append(None)
			self.list.append(object)

		else:
			self.list[index] = object

		return self.list

	def __add__(self, other):
		if type(other) == list:
			self.list = self.list + other

		elif type(other) == tuple:
			self.list = self.list + list(other)

		elif type(other) == List:
			self.list = self.list + other.list

		else:
			self.list.append(other)

		return self.list

	def __truediv__(self, number):
		if type(number) == str:
			try:
				number = int(number)
			except ValueError:
				number = self.index(number, default=True)
		return self.split(number)

	def __mul__(self, other):
		if type(other) in [int, float]:
			self.list = self.list*int(other)

		elif type(other) == str:
			try:
				self.list = self.list*int(float(other))
			except ValueError:
				self.list = self.list*self.index(other, default=True)

		else:
			raise TypeError('Multiplier must be either int or str not [%s]' % other.__class__.__name__)

		return self.list

	def __delitem__(self, index):
		if index not in self.list:
			return
		del self.list[index]

	def __eq__(self, other):
		if type(other) == int:
			return other == self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other) == self.list

		elif type(other) == dict:
			return list(dict.items()) == self.list

		elif type(other) == List:
			return other.list == self.list

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def __ne__(self, other):
		if type(other) == int:
			return other != self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other) != self.list

		elif type(other) == dict:
			return list(dict.items()) != self.list

		elif type(other) == List:
			return other.list != self.list

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def __gt__(self, other):
		if type(other) == int:
			return other > self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other).__len__() > self.list

		elif type(other) == dict:
			return list(dict.items()).__len__() > self.list

		elif type(other) == List:
			return other.length > self.length

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def __lt__(self, other):
		if type(other) == int:
			return other < self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other).__len__() < self.list

		elif type(other) == dict:
			return list(dict.items()).__len__() < self.list

		elif type(other) == List:
			return other.length < self.length

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def __ge__(self, other):
		if type(other) == int:
			return other >= self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other).__len__() >= self.list

		elif type(other) == dict:
			return list(dict.items()).__len__() >= self.list

		elif type(other) == List:
			return other.length >= self.length

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def __le__(self, other):
		if type(other) == int:
			return other <= self.__len__()

		elif type(other) in [list, tuple, set]:
			return list(other).__len__() <= self.list

		elif type(other) == dict:
			return list(dict.items()).__len__() <= self.list

		elif type(other) == List:
			return other.length <= self.length

		raise TypeError('Cannot compare type %s with type List' % other.__class__.__name__)

	def remove_many(*values):
		for value in values:
			try:
				self.pop(value)
			except (IndexError, TypeError):
				pass
		return self.list

	def append(self, value):
		self.list.append(value)
		return self.list

	def pop(self, index):
		if type(index) == str:
			try:
				index = int(index)
			except ValueError:
				index = self.index(index, 0)
		popped = self.list.pop(index)
		return popped

	def insert(self, value, index):
		if type(index) == str:
			try:
				index = int(float(index))
			except ValueError:
				index = self.index(index)

		self.list.insert(int(index), value)
		return self.list

	def remove(self, value):
		self.pop(value)
		return self.list

	def sort(self):
		self.list = sorted(self.list, key=lambda key: str(key))
		return self.list

	def clear(self):
		self.list = []
		return self.list

	def copy(self):
		return self.list

	def split(self, index):
		first_half = self.list[index:]
		second_half = self.list[:index]
		return (first_half, second_half)

	def index(self, value, start: int = 0, end: int = None, step: int = 1, default=False):
		if not default:
			if not end:
				end = self.__len__()
			new_list = self.list[start:end:step] 
			return new_list.index((value + start))
		return self.list.index(value, start)

	def reverse(self):
		return self.list[::-1]

	@property
	def length(self):
		return self.__len__()

	@property
	def dupes(self):
		return self.__len__() - self.__set__()
