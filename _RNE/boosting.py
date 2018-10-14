from numpy import loadtxt
from xgboost import XGBClassifier, plot_importance
from matplotlib import pyplot
import numpy as np
from numpy import random
import codecs

def load_csv(filepath):
    result = []
    with codecs.open(filepath, 'r', encoding='euc-kr', errors='ignore') as f:
        while True:
            read = f.readline()
            if not read:
                break
            result.append(read.split(','))
    return result


food_dict = {}
next_num = 0

def formatting_data(_list):
    global food_dict
    global next_num
    result = []
    for _i in _list:
        if len(_i) > 0 and '0' <= _i[0] <= '9':
            result.append(int(_i[0]))
        else:
            if _i not in food_dict:
                food_dict[_i] = next_num
                next_num += 1
            result.append(food_dict[_i])
    return result


dataset = load_csv('data_classify.csv')
dataset = [formatting_data(list) for list in dataset]
random.shuffle(dataset)

X = np.array([item[:9] for item in dataset])
y = np.array([item[9] for item in dataset])

model = XGBClassifier()
model.fit(X, y)

plot_importance(model)
pyplot.show()