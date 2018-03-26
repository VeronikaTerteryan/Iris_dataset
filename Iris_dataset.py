#!/usr/bin/env python
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#Dataset is the collection of all the data taken from sample
print("keys iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193]+"\n...")
#DESCR - The brief description of the keys
print("Names of sorts:{}".format(iris_dataset['target_names']))
#Target_names is an array of strings containing the sorts of flowers
print("Names of features: \n{}".format(iris_dataset['feature_names']))
#Feature_names is a list of strings with descriptions of each characteristic(feature)
#The data stored in target and data arrays.
print("-------------------------------------------------------")
print(("The type of array data:{}".format(type(iris_dataset['data']))))
#data is NumPy array which contains quantitative measurements of sepal length, sepal width, petal length, petal width
print("The form of data: {}".format(iris_dataset['data'].shape))
#Data contains measurements for 150 different flowers according to 4 characteristics
print("-------------------------------------------------------")
print("The first five rows of the array:\n {}".format(iris_dataset['data'][:5]))
#All 5 flowers have a petal width=0.2sm and the first flower has the largest length of sepal= 5.1sm
print("The type of array target: {}".format(type(iris_dataset['target'])))
print("The form of array target:\n {}".format(type(iris_dataset['target'].shape)))
#Sorts are encoded as an integers from 0 to 2
print("The answers:\n{}".format(iris_dataset['target']))