from Algorithms.KNN import KNN
from Algorithms.NaiveBayes import NaiveBayes
from Algorithms.DecisionTree import DecisionTree
from Validation import k_cross_validation_tpool
from Data.DataSet import DataSet


if __name__ == "__main__":
    knn = KNN()
    dt = DecisionTree()
    print(k_cross_validation_tpool(dt, DataSet("dataset.txt")))

    dt.train(DataSet("dataset.txt"))

    print(str(dt))
