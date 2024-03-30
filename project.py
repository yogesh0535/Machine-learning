# linear algebra
import numpy as np 

# data processing
import pandas as pd 

# data visualization
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
'''
# Algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB
'''
test_df = pd.read_csv("test.csv")
train_df = pd.read_csv("train.csv")

train_df.info()