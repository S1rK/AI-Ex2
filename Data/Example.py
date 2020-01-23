from typing import Dict, KeysView


class Example(object):
    __features: Dict[str, str]

    def __init__(self, features: Dict[str, str]):
        """
        :param features: a dictionary between attributes and their values (including the class/label)
        """
        self.__features = features

    def __getitem__(self, item: str):
        """
        :param item: an attribute name (or 'class')
        :return: the attribute's/class's value
        """
        return self.__features[item]

    def __eq__(self, other: 'Example'):
        """
        :param other: another example to compare to.
        :return: if the examples are equals.
        """
        return self.distance(other) == 0

    def attributes(self) -> KeysView[str]:
        """
        :return: a KeyView of the attributes
        """
        return self.__features.keys()

    def distance(self, other: 'Example') -> float:
        """
        :param other: another example to compare to.
        :return: the number of attributes that doesn't have the same value
        """
        chars_pairs = [(self.__features[key], other.__features[key]) for key in self.__features.keys() if
                       key != 'class']
        return len(list(filter(lambda pair: pair[0] != pair[1], chars_pairs)))
