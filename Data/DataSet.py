from .Example import Example
from os import path
from typing import List, Dict
from math import log2
from random import shuffle


class DataSet(object):
    def __init__(self,  *args):
        """
        :param args:  [file_name] or [examples list, attributes list] or [examples list, attribute dict] or [attribute dict, examples list]
        """
        # [file name]
        if len(args) == 1 and isinstance(args[0], str):
            if path.isfile(args[0]):
                with open(args[0], "r") as f:
                    # the first line in the file is the attributes
                    attributes_line = f.readline()
                    # make a list of them
                    attributes_list = attributes_line.split()[:-1] + ["class"]
                    # initialize the examples and the attributes
                    self.__examples = []
                    self.__attributes = dict([(att, []) for att in attributes_list])
                    # get the examples and the attribute's values
                    for line in f:
                        # current example
                        example = Example(dict(zip(attributes_list, line.split())))
                        # add the example to the examples list
                        self.__examples.append(example)
                        # for every attribute
                        for att in attributes_list:
                            # if the example's value isn't in the attribute's dict, add it
                            if example[att] not in self.__attributes[att]:
                                self.__attributes[att].append(example[att])
            else:
                raise Exception(f"DataSet: {args[0]} doesnt exist")
        # [examples list, attributes list]
        elif len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], list):
            self.__examples = args[0]
            if 'class' not in args[1]:
                args[1].append('class')
            self.__attributes = dict([(att, []) for att in args[1]])
            for e in args[0]:
                # for every attribute
                for att in args[1]:
                    # if the example's value isn't in the attribute's dict, add it
                    if e[att] not in self.__attributes[att]:
                        self.__attributes[att].append(e[att])
        # [examples list, attributes dict]
        elif len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], dict):
            self.__examples = args[0]
            self.__attributes = args[1]
        # [attributes dict, examples list]
        elif len(args) == 2 and isinstance(args[0], dict) and isinstance(args[1], list):
            self.__examples = args[1]
            self.__attributes = args[0]
        else:
            raise Exception(
                f"""DataSet: got {args},\n
                expected: [file_name] or [examples list, attribute dict] or [attribute dict, examples list]""")

    def get_attributes(self) -> List[str]:
        """
        :return: a list of the attributes
        """
        return list(self.__attributes.keys())[:-1]

    def get_examples(self) -> List[Example]:
        """
        :return: a list of examples
        """
        return self.__examples

    def get_examples_with_attribute_value(self, attributes: List[str], att_values: List[str]) -> List[Example]:
        """
        :param attributes: a list of attributes
        :param att_values: a list of values (aligned with the attributes list)
        :return: a list of examples that have the values of the given attributes
        """
        examples = self.__examples
        for example in self.__examples:
            for att, value in zip(attributes, att_values):
                if example[att] != value:
                    examples.remove(example)
                    break
        return examples

    def get_len_examples_with_attribute_value(self, attribute: str, att_value: str) -> int:
        """
        :param attribute: an attribute
        :param att_value: the attribute value
        :return: return the number of examples with the attribute's value
        """
        return len(self.get_examples_with_attribute_value([attribute], [att_value]))

    def get_attribute_values(self, attribute: str) -> List[str]:
        """
        :param attribute: an attribute
        :return: a list of the attribute's value
        """
        return self.__attributes[attribute]

    def count_attribute_values(self, attribute: str) -> Dict[str, int]:
        """
        :param attribute: an attribute
        :return: a dict between the attribute's values and the number of examples that have those values
        """
        count_dict = dict([(value, 0) for value in self.__attributes[attribute]])
        for example in self.__examples:
            count_dict[example[attribute]] += 1
        for value in self.__attributes[attribute]:
            if count_dict[value] == 0:
                del count_dict[value]
        return count_dict

    def get_attributes_dict(self):
        """
        :return: a dict between attribute to a list of the attribute's  values
        """
        return self.__attributes

    def subset(self, examples: List[Example]) -> 'DataSet':
        """
        :param examples: a list of examples
        :return: a data set with the given examples and this data set's attributes dict
        """
        return DataSet(examples.copy(), self.__attributes)

    def __entropy(self) -> float:
        """
        :return: The dataset's entropy
        """
        total = len(self.__examples)
        cls_count = self.count_attribute_values('class')

        return -1 * sum([value * log2(value / total) for value in cls_count.values()]) / total

    def information_gain(self, attribute: str) -> float:
        """
        :param attribute: an attribute
        :return: returns the information gain for this attribute
        """
        att_count = self.count_attribute_values(attribute)
        examples = self.get_examples()

        lst = []

        for val, cnt in att_count.items():
            examples = [e for e in examples if e[attribute] == val]
            if len(examples) == 0:
                continue
            ds = self.subset(examples)
            lst.append(cnt * ds.__entropy())
        return self.__entropy() - sum(lst) / sum(att_count.values())

    def shuffle(self):
        """
        shuffles the examples list
        :return: Nothing, void
        """
        shuffle(self.__examples)

    def __str__(self):
        """
        :return: "{attributes dict}\n{examples list}"
        """
        return str(self.get_attributes()) + "\n" + "\n".join(self.__examples)

    def __len__(self):
        """
        :return: the number of examples
        """
        return len(self.__examples)

    def __copy__(self):
        """
        :return: a copy of this data set
        """
        return DataSet(self.__examples, self.__attributes)
