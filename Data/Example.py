from typing import Dict, KeysView


class Example(object):
    __features: Dict[str, str]

    def __init__(self, features: Dict[str, str]):
        self.__features = features

    def __getitem__(self, item: str):
        return self.__features[item]

    def __eq__(self, other: 'Example'):
        return self.distance(other) == 0

    def attributes(self) -> KeysView[str]:
        return self.__features.keys()

    def distance(self, other: 'Example') -> float:
        chars_pairs = [(self.__features[key], other.__features[key]) for key in self.__features.keys() if
                       key != 'class']
        return len(list(filter(lambda pair: pair[0] != pair[1], chars_pairs)))
