from Data.Example import Example


class Node(object):
	__children: dict
	__attribute: str
	__default: str
	__class: str

	def __init__(self, *args):
		"""

		:param args: [attribute, default] or [classification]
		"""
		if len(args) == 1 and isinstance(args[0], str):
			self.__attribute = None
			self.__default = None
			self.__children = {}
			self.__class = args[0]
		elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
			self.__attribute = args[0]
			self.__default = args[1]
			self.__children = {}
			self.__class = None
		else:
			raise Exception(f"Node: got {args}, expected: [attribute, default] or [classification]")

	def add_child(self, child: 'Node', attribute_value: str) -> None:
		self.__children[attribute_value] = child

	def predict(self, problem: Example):
		if self.__class is None and self.__attribute is None:
			raise Exception('Tree not finished')

		if self.__class is not None:
			return self.__class
		elif problem[self.__attribute] in self.__children.keys():
			return self.__children[problem[self.__attribute]].predict(problem)
		else:
			return self.__default

	def __str__(self):
		if len(self.__children) == 0:
			return self.__class
		else:
			ret = ""
			for value, child in self.__children.items():
				temp = '\n\t'.join(str(child).split('\n'))
				ret += f"\n|{self.__attribute}={value}:{temp}"
			return ret



