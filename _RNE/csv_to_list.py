# 패키지 불러오기
import codecs
import numpy as np
from numpy import random


# 변수 정의
food_dict = {}
next_num = 0


# 함수
def one_hot(num):
    result = [0, 0, 0, 0, 0]
    result[num - 1] = 1
    return result


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


def load_csv(filepath):
    result = []
    with codecs.open(filepath, 'r', encoding='euc-kr', errors='ignore') as f:
        while True:
            read = f.readline()
            if not read:
                break
            result.append(read.split(','))
    return result


def get_data(filepath, slice_rate):
    dataset = load_csv(filepath)

    dataset = [formatting_data(list) for list in dataset]
    random.shuffle(dataset)

    x_data = np.array([item[:-1] for item in dataset])
    y_data = np.array([one_hot(item[-1]) for item in dataset])

    data_slice = int(len(y_data) * slice_rate)

    x_train = x_data[:data_slice]
    y_train = y_data[:data_slice]
    x_test = x_data[data_slice:]
    y_test = y_data[data_slice:]

    return x_train, y_train, x_test, y_test
