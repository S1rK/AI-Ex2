from Data.DataSet import DataSet
from Data.Example import Example
from typing import List


class Algorithm(object):
    def train(self, training_set: DataSet):
        raise NotImplemented("shiz")

    def predict(self, problem: Example) -> str:
        raise NotImplemented("shiz")

    def predict_problems(self, problems: List[Example]) -> List[str]:
        return [self.predict(problem) for problem in problems]

    def validate(self, validation_set: List[Example]):
        return sum([1 for example in validation_set if self.predict(example) == example['class']]) / len(validation_set)

    def copy(self) -> 'Algorithm':
        return Algorithm()
