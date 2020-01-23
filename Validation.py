from multiprocessing import Pool
from random import seed
from typing import List, Tuple, Iterable

from Algorithms.Algorithms import Algorithm
from Data.DataSet import DataSet
from Data.Example import Example
from Utilities.Utilities import argmax


def test_validation(tup: Tuple[Algorithm, DataSet, List[Example]]) -> float:
    """
    :param tup: a tuple of Algorithm, Dataset and a List of Examples
    :return: the algorithm's validation with the list of examples after training him with the data set
    """
    alg = tup[0]
    alg.train(tup[1])
    return alg.validate(tup[2])


def k_cross_validation(alg: Algorithm, dataset: DataSet, k=5) -> float:
    """
    :param alg: an algorithm
    :param dataset: the training and validation set
    :param k: the k for the k-cross
    :return: the k-cross validation for the given algorithm.
    """
    chunk_size = len(dataset) // k
    examples = dataset.get_examples()
    attributes = dataset.get_attributes_dict()
    pool = Pool(k)
    exec_arg_lst: List[Tuple[Algorithm, DataSet, List[Example]]] = []
    for i in range(k):
        train_set = DataSet(examples[0:i * chunk_size] + examples[(i + 1) * chunk_size:], attributes)
        validation_set = examples[i * chunk_size:(i + 1) * chunk_size]
        exec_arg_lst.append((alg, train_set, validation_set))
    res = pool.map(test_validation, exec_arg_lst)
    pool.close()
    pool.join()
    return round(sum(res) / k, 2)


def shuffle_validation(alg: Algorithm, dataset: DataSet, s: int = 0, k: int = 5) -> float:
    """
    :param alg: an algorithm
    :param dataset: the training and validation set
    :param s: the seed to shuffle by
    :param k: the k for the k-cross
    :return: shuffles the data set with the given seed and then k-cross validate with it
    """
    seed(s)
    dataset = dataset.__copy__()
    dataset.shuffle()
    return k_cross_validation(alg, dataset, k)


def max_seed_for_alg(alg: Algorithm, dataset: DataSet, k=5, seed_range: Iterable[int] = range(20)) -> Tuple[int, float]:
    """
    :param alg: an algorithm
    :param dataset: the training and validation set
    :param k: the k for the k-cross
    :param seed_range: an iterable of seeds to test
    :return: a tuple of the best seed and it's shuffle k-cross validation return value
    """
    s = argmax(lambda s: shuffle_validation(alg, dataset, s, k), seed_range)
    return (s, shuffle_validation(alg, dataset, s, k))
