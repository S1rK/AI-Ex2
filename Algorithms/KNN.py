from Data.DataSet import DataSet
from Data.Example import Example
from Algorithms.Algorithms import Algorithm
from Utilities.Utilities import argmax, count_attribute


class KNN(Algorithm):
    __k: int
    __examples: list
    __classes: list

    def __init__(self, k: int = 5):
        self.__k = k
        self.__examples = None
        self.__classes = None

    def train(self, training_set: DataSet):
        self.__examples = training_set.get_examples()
        self.__classes = training_set.get_attribute_values('class')

    def predict(self, problem: Example) -> str:
        if self.__examples is None:
            raise Exception('Untrained Model')
        else:
            self.__examples.sort(key=lambda other: problem.distance(other))
            k_nearest = self.__examples[:self.__k]
            class_count = count_attribute(k_nearest, 'class')

            return argmax(lambda classification: class_count[classification], self.__classes)

    def __copy__(self) -> 'KNN':
        return KNN(self.__k)

    def __str__(self):
        return f"KNN: {self.__k} Nearest Neighbors"
