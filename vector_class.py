class Vector:
	"""Vector class with simple actions."""
	def __init__(self, vec):
		if not isinstance(vec, list):
			raise ValueError
		self.vector = vec

	def add(self, vec):
		if not len(self.vector) == len(vec.vector):
			raise Exception("Size of vectors must equal to each other")
		else:
			result = []
			for index in range(len(self.vector)):
				total = self.vector[index] + vec.vector[index]
				result.append(total)
			result = Vector(result)
			return result
	
	def equals(self, vec):
		if self.vector == vec.vector:
			return True
		else:
			return False

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.add(b).equals(Vector([4, 6, 8])))
print(Vector([1, 2, 3]).vector)