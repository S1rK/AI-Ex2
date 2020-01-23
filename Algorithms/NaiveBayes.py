from functools import reduce
from Data.DataSet import DataSet
from Data.Example import Example
from Algorithms.Algorithms import Algorithm
from Utilities.Utilities import argmax
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

    def predict(self, problem: Example) -> str:
        if self.__training_set is None:
            raise Exception('Untrained Model')
        else:
            examples = self.__training_set.get_examples()
            return argmax(lambda cls: reduce(lambda x, y: x * y, [
                1 + sum([1 for e in examples if e[att] == problem[att] and e['class'] == cls]) for att in
                problem.attributes()]), self.__classes)

    def __copy__(self) -> 'NaiveBase':
        return NaiveBayes()

    def __str__(self):
        return "Naive Bayes"
