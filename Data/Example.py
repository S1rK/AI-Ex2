from typing import List, Dict, KeysView


class Example(object):
    features: Dict[str, str]

    def __init__(self, features: Dict[str, str]):
        self.features = features

    def __getitem__(self, item: str):
        return self.features[item]

    def __eq__(self, other: 'Example'):
        return self.distance(other) == 0

    def attributes(self) -> KeysView[str]:
        return self.features.keys()

    def distance(self, other: 'Example') -> float:
        chars_pairs = [(self.features[key], other.features[key]) for key in self.features.keys() if key != 'class']
        return len(list(filter(lambda pair: pair[0] != pair[1], chars_pairs)))
