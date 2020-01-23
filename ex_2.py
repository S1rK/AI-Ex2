from Algorithms.KNN import KNN
from Algorithms.NaiveBayes import NaiveBayes
from Algorithms.DecisionTree import DecisionTree
from Validation import shuffle_validation
from Data.DataSet import DataSet


def calc_accuracy():
    """
    clac the accuracy with the shuffle-k-cross-validation of the 3 algorithms and write their accuracy in "accuracy.txt"
    :return: nothing, void
    """
    # list of algorithms
    algs = [(DecisionTree(), 17), (KNN(), 19), (NaiveBayes(), 4)]
    # open the accuracy file
    with open("accuracy.txt", 'w+') as f:
        # for every algorithm
        for alg, s in algs:
            # calculate it's accuracy
            accuracy = shuffle_validation(alg, DataSet("dataset.txt"), s)
            # write it in the file
            f.write(f"{accuracy}\t")


def print_tree():
    """
    train the tree with the "dataset.txt" and writes into "tree.txt" the decision tree.
    :return: nothing, void.
    """
    # create the algorithm
    decision_tree = DecisionTree()
    # create the data set
    data_set = DataSet("dataset.txt")
    # train the decision tree with the data set
    decision_tree.train(data_set)
    # print the decision tree inside the tree file
    with open("tree.txt", "w+") as f:
        f.write(str(decision_tree))


def test():
    """
    train all the algorithms with "train.txt", and validate with "test.txt". write the tree and the accuracies into "output.txt"
    :return: nothing, void.
    """
    # list of algorithms
    algs = [DecisionTree(), KNN(), NaiveBayes()]
    # open the output file
    with open("output.txt", 'w+') as f:
        # create the algorithm
        decision_tree = DecisionTree()
        # create the training set
        train_set = DataSet("train.txt")
        # train the decision tree with the data set
        decision_tree.train(train_set)
        # print the decision tree inside the tree file
        f.write(str(decision_tree))

        f.write("\n")

        # for every algorithm
        for alg in algs:
            training_set = DataSet("train.txt")
            test_set = DataSet("test.txt").get_examples()
            # train with the training data set
            alg.train(training_set)
            # calculate it's accuracy
            accuracy = alg.validate(test_set)
            # write it in the file
            f.write(f"{accuracy}\t")


if __name__ == "__main__":
    calc_accuracy()

    print_tree()

    #test()
