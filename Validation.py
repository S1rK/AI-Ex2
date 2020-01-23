from Algorithms.Algorithms import Algorithm
from Data.DataSet import DataSet
from Data.Example import Example
from multiprocessing import Pool
from typing import List, Tuple


def test_validation(tup: Tuple[Algorithm, DataSet, List[Example]]) -> float:
    alg = tup[0]
    alg.train(tup[1])
    return alg.validate(tup[2])


def k_cross_validation_tpool(alg: Algorithm, dataset: DataSet, k=5) -> float:
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
    return sum(res) / k
