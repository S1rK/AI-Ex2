from typing import List
from math import log2
from os import path


class DataSet:
    def __init__(self, file_name: str = "dataset.txt"):
        if path.isfile(file_name):
            with open(file_name, "r") as f:
                # the first line in the file is the attributes
                attributes_line = f.readline()
                # make a list of them
                attributes_list = attributes_line.split()
                # initialize the examples and the attributes
                self.__examples = []
                self.__attributes = dict([(att, []) for att in attributes_list])
                # get the examples and the attribute's classes
                for line in f:
                    # current example
                    example = line.split()
                    # add the example to the examples list
                    self.__examples.append(example)
                    # for every attribute
                    for i in range(len(attributes_list)):
                        # if the example's class isn't in the attribute's dict, add it
                        if example[i] not in self.__attributes[attributes_list[i]]:
                            self.__attributes[attributes_list[i]].append(example[i])

    def get_attribute_index(self, attribute: str):
        return self.get_attributes().index(attribute)

    def subsets(self, attribute: str):
        # the data sets
        data_sets = []
        # the attribute index in the example
        att_index = self.get_attribute_index(attribute)
        for att_class in self.__attributes[attribute]:
            # copy of the attributes dict with only this att_class in the given attribute
            attributes = self.__attributes
            attributes[attribute] = [att_class]
            # create a new data set
            data_set = DataSet()
            # give it the new attribute dict
            data_set.__attributes = attributes
            # set the examples to be all the examples with the att_class in the attribute
            data_set.__examples = [example for example in self.__examples if example[att_index] is att_class]
            # add the data set to the list
            data_sets.append(data_set)
        # return the list of data sets
        return data_sets

    def get_attributes(self) -> List[str]:
        return list(self.__attributes.keys())

    def get_examples(self) -> List[List[str]]:
        return self.__examples

    def get_examples_with_attribute_class(self, attribute: str, att_class: str) -> List[List[str]]:
        return [example for example in self.__examples if example[self.get_attribute_index(attribute)] == att_class]

    def get_count_examples_with_attribute_class(self, attribute: str, att_class: str) -> int:
        return len(self.get_examples_with_attribute_class(attribute, att_class))

    def get_attribute_classes(self, attribute: str) -> List[str]:
        return self.__attributes[attribute]

    def get_attribute_proportions(self, attribute: str) -> List[int]:
        # the list
        portions = []
        # the attribute index in the example
        att_index = self.get_attribute_index(attribute)
        for att_class in self.__attributes[attribute]:
            # sum all the examples with the att_class in the attribute
            portions.append(sum([1 for example in self.__examples if example[att_index] is att_class]))

        return portions


class Node(object):
    def __init__(self, value: str):
        self.__value = value
        self.__children = []

    def get_value(self) -> str:
        return self.__value

    def add_child(self, child):
        self.__children.append(child)

    def add_children(self, children):
        self.__children += children

    def get_children(self):
        return self.__children

    def get_child(self, value: str):
        for child in self.__children:
            if child.get_value() == value:
                return child
        return None


def proportion(dataset: DataSet, attribute: str, att_class: str) -> float:
    return dataset.get_count_examples_with_attribute_class(attribute, att_class) / len(dataset.get_examples())


def entropy(dataset: DataSet, attribute: str) -> float:
    """
    :param dataset: The current dataset for which entropy is being calculated.
    :param attribute: an attribute.
    :return: the amount of uncertainty in the (data) set S
    """
    return sum(
        [-1 * proportion(dataset, attribute, att_class) * log2(proportion(dataset, attribute, att_class)) for att_class
         in dataset.get_attribute_classes(attribute)])


def information_gain(dataset: DataSet, attribute: str):
    """
    :param dataset: a data set.
    :param attribute: an attribute.
    :return:  the difference in entropy from before to after the set S is split on an attribute A.
              In other words, how much uncertainty in S was reduced after splitting set S on attribute A.
    """

    return entropy(dataset, attribute) - sum([proportion(dataset, attribute, att_class)*entropy(dataset, t) for t in T])


def ID3(examples, target_attribute, attributes):
    """
        Create a root node for the tree
        If all examples are positive, Return the single-node tree Root, with label = +.
        If all examples are negative, Return the single-node tree Root, with label = -.
        If number of predicting attributes is empty, then Return the single node tree Root,
        with label = most common value of the target attribute in the examples.
        Otherwise Begin
            A ← The Attribute that best classifies examples.
            Decision Tree attribute for Root = A.
            For each possible value, vi, of A,
                Add a new tree branch below Root, corresponding to the test A = vi.
                Let Examples(vi) be the subset of examples that have the value vi for A
                If Examples(vi) is empty
                    Then below this new branch add a leaf node with label = most common target value in the examples
                Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
        End
        Return Root
        """
    node = Node()


if __name__ == "__main__":
    ds = DataSet()
    print(ds.get_attribute_classes('gill_spacing'))
