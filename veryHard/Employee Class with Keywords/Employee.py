class Employee:
	def __init__(self, fullname, **kwargs):
		self.name, self.lastname = fullname.split()
		self.salary = kwargs.get('salary')
		self.height = kwargs.get('height')
		self.nationality = kwargs.get('nationality')
		self.subordinates = kwargs.get('subordinates')