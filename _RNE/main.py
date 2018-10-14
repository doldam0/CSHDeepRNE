# -*- coding: utf-8 -*-
#######################
#    Park Geup Sick   #
#######################
# start from 2018-8-9 #
#       made by       #
#     Kim DongHyeon   #
#     Jang JinWoo     #
#       GODPARK       #
#######################

# Import package
import random
import codecs
import numpy as np
from keras.layers import Dense, Dropout
from keras.models import Sequential
from matplotlib import pyplot as plt


# Function
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


# DataSet
food_dict = {}
next_num = 0
x_data = []
y_data = []

if __name__ == "__main__":
    dataset = load_csv('data_classify.csv')
    print(dataset)

    dataset = [formatting_data(list) for list in dataset]
    random.shuffle(dataset)

    x_data = np.array([item[:9] for item in dataset])
    y_data = np.array([one_hot(item[9]) for item in dataset])
    print(x_data)
    print(y_data)

    data_slice = int(len(y_data) * 0.8)

    x_train = x_data[:data_slice]
    y_train = y_data[:data_slice]
    x_test = x_data[data_slice:]
    y_test = y_data[data_slice:]

    # Design
    model = Sequential()
    num_of_hidden = 3
    hidden_layer = 8
    model.add(Dense(units=hidden_layer, input_dim=9, activation='relu'))
    for i in range(num_of_hidden):
        model.add(Dense(units=hidden_layer, activation='relu'))
    model.add(Dense(units=5, activation='softmax'))

    # Compile
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fitting
    this_epochs = 500
    this_batch_size = 25
    hist = model.fit(x_train, y_train, epochs=this_epochs, batch_size=this_batch_size)

    # Process
    print(' ## GOD PARK GEUP SICK ## ')
    print(hist.history['loss'])
    print(hist.history['acc'])

    # Evaluate
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=this_batch_size)
    print(' ## GOD PARK GEUP SICK IS BEING EVALUATED ## ')
    print('loss and metrics')
    print(loss_and_metrics)

    # Save
    print(' ## Now Saving... ## ')
    json_string = model.to_json()
    model.save('park_sick.h5')
    print(' ## ...Success! ## ')

    # Graph
    plt.title('Loss')
    plt.plot(hist.history['loss'])
    plt.show()

    plt.title('Accurancy')
    plt.plot(hist.history['acc'], c='y')
    plt.show()