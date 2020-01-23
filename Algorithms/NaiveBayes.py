from functools import reduce
from Data.DataSet import DataSet
from Data.Example import Example
from Algorithms.Algorithms import Algorithm
from Utilities.Utilities import argmax, multiply
from typing import Iterable


class NaiveBayes(Algorithm):
    __training_set: DataSet
    __classes: Iterable[str]

    def __init__(self):
        self.__training_set = None
        self.__classes = None

    def train(self, training_set: DataSet) -> None:
        self.__training_set = training_set
        self.__classes = set(training_set.get_attribute_values('class'))

    def predict(self, example: Example) -> str:
        if self.__training_set is None:
            raise Exception('Untrained Model')
        else:
            examples = self.__training_set.get_examples()
            return argmax(lambda cls: reduce(lambda x, y: x * y, [
                1 + sum([1 for e in examples if e[att] == example[att] and e['class'] == cls]) for att in
                example.attributes()]), self.__classes)

    def copy(self) -> 'NaiveBase':
        return NaiveBayes()
