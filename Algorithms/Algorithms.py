from Data.DataSet import DataSet
from Data.Example import Example
from typing import List


class Algorithm(object):
    def train(self, training_set: DataSet):
        """
        :param training_set: the training set to train the algorithm by.
        :return: nothing, void.
        """
        raise NotImplemented("shiz")

    def predict(self, problem: Example) -> str:
        """
        :param problem: a given problem to predict.
        :return: the algorithm's prediction for the given problem.
        """
        raise NotImplemented("shiz")

    def validate(self, validation_set: List[Example]):
        """
        :param validation_set: a list of examples to validate the algorithm by.
        :return: the accuracy to predict the given examples list
        """
        return round(
            sum([1 for example in validation_set if self.predict(example) == example['class']]) / len(validation_set),
            2)

    def __copy__(self) -> 'Algorithm':
        """
        :return: a copy of the algorithm
        """
        return Algorithm()

    def __str__(self):
        """
        :return: a string represent the algorithm
        """
        return "Algorithm"
