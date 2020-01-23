from Algorithms.KNN import KNN
from Algorithms.NaiveBayes import NaiveBayes
from Validation import k_cross_validation_tpool
from Data.DataSet import DataSet


if __name__ == "__main__":
    knn = KNN()
    nb = NaiveBayes()
    print(k_cross_validation_tpool(nb, DataSet("dataset.txt")))
