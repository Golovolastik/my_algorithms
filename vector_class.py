class Vector:
	"""Vector class with simple actions."""
	def __init__(self, vec):
		if not isinstance(vec, list):
			raise ValueError
		self.vector = vec

	def add(self, vec):
		"""Adding two vectors."""
		if not len(self.vector) == len(vec.vector):
			raise Exception("Size of vectors must equal to each other")
		else:
			result = []
			for index in range(len(self.vector)):
				total = self.vector[index] + vec.vector[index]
				result.append(total)
			result = Vector(result)
			return result

	def subtract(self, vec):
		"""Subtracting two vectors."""
		if not len(self.vector) == len(vec.vector):
			raise Exception("Size of vectors must equal to each other")
		else:
			result = []
			for index in range(len(self.vector)):
				total = self.vector[index] - vec.vector[index]
				result.append(total)
			result = Vector(result)
			return result
	
	def equals(self, vec):
		"""Compares two vectors."""
		if self.vector == vec.vector:
			return True
		else:
			return False

	def dot(self, vec):
		"""Dot product of two vectors."""
		if not len(self.vector) == len(vec.vector):
			raise Exception("Size of vectors must equal to each other")
		else:
			result = 0
			for index in range(len(self.vector)):
				total = self.vector[index] * vec.vector[index]
				result += total
			return result

	def norm(self):
		"""Return the length of vector."""
		result = 0
		for number in self.vector:
			result += number ** 2
		return result ** 0.5

	def __str__(self):
		"""Necessary condition to complete Kata. Method that returns string."""
		return f"({','.join(str(number) for number in self.vector)})"

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.add(b).equals(Vector([4, 6, 8])))
print(str(a))
print(a.subtract(b))
print(a.dot(b))
print(a.norm())