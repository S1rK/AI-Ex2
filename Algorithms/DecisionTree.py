from Data.DataSet import DataSet
from Data.Example import Example
from Algorithms.Algorithms import Algorithm
from Utilities.Utilities import argmax, count_attribute
from Algorithms.Tree import Node
from typing import List
from math import log2


class DecisionTree(Algorithm):
	__tree: Node

	def __init__(self):
		self.__tree = None

	def __create_tree(self, training_set: DataSet, attributes: List[str]) -> Node:
		if 'class' in attributes:
			attributes.remove('class')
		# count the number of examples for each classification
		class_values = training_set.count_attribute_values('class')
		# max class
		max_class = argmax(lambda cls: 0 if cls not in class_values.keys() else class_values[cls], training_set.get_attribute_values('class'))

		# if training set is empty
		# if len(training_set) is 0:
		# 	return Node(max_class)
		# if same classification for everyone
		if len(class_values.keys()) == 1:
			return Node(list(class_values.keys())[0])
		# if attributes are empty
		elif len(attributes) == 0:
			return Node(max_class)

		else:
			max_att = argmax(lambda attribute: training_set.information_gain(attribute), attributes)
			# print(max_att)
			node = Node(max_att, max_class)
			attributes.remove(max_att)
			for value in training_set.get_attribute_values(max_att):
				examples = [e for e in training_set.get_examples() if e[max_att] == value]
				examples = DataSet(examples, attributes)
				if len(examples) != 0:
					child = self.__create_tree(examples, attributes.copy())
				else:
					child = Node(max_class)

				node.add_child(child, value)
			return node

	def train(self, training_set: DataSet):
		self.__tree = self.__create_tree(training_set, training_set.get_attributes())

	def predict(self, problem: Example) -> str:
		return self.__tree.predict(problem)

	def copy(self) -> 'DecisionTree':
		return DecisionTree()

	def __str__(self):
		temp = str(self.__tree)
		ret = ""
		for line in temp.split("\n"):
			if line.startswith('|'):
				ret += f"\n{line[1:]}"
			else:
				ret += f"\n{line}"
		return ret
