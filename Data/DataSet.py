from .Example import Example
from os import path
from typing import List


class DataSet(object):
    def __init__(self,  *args):
        """
        :param args:  [file_name] or [examples list, attribute dict] or [attribute dict, examples list]
        """
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

        elif len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], dict):
            self.__examples = args[0]
            self.__attributes = args[1]
        elif len(args) == 2 and isinstance(args[0], dict) and isinstance(args[1], list):
            self.__examples = args[1]
            self.__attributes = args[0]
        else:
            raise Exception("DataSet didn't get what he needed")

    def get_attributes(self) -> List[str]:
        return list(self.__attributes.keys())[:-1]

    def get_examples(self) -> List[Example]:
        return self.__examples

    def get_examples_with_attribute_value(self, attributes: List[str], att_values: List[str]) -> List[Example]:
        examples = self.__examples
        for example in self.__examples:
            for att, value in zip(attributes, att_values):
                if example[att] != value:
                    examples.remove(example)
                    break
        return examples

    def get_len_examples_with_attribute_value(self, attribute: str, att_value: str) -> int:
        return len(self.get_examples_with_attribute_value(attribute, att_value))

    def get_attribute_values(self, attribute: str) -> List[str]:
        return self.__attributes[attribute]

    def get_attributes_dict(self):
        return self.__attributes

    def get_attribute_proportions(self, attribute: str) -> List[int]:
        # the list
        portions = []
        for att_value in self.__attributes[attribute]:
            # sum all the examples with the att_class in the attribute
            portions.append(sum([1 for example in self.__examples if example[attribute] is att_value]))

        return portions

    def __str__(self):
        return str(self.get_attributes()) + "\n" + "\n".join(self.__examples)

    def __len__(self):
        return len(self.__examples)
