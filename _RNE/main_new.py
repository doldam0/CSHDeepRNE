# -*- coding: utf-8 -*- #
########################
#     Park Geup Sick    #
########################
# start from 2018-9-27 #
#        made by        #
#     Kim DongHyeon     #
#     Jang JinWoo       #
#       GODPARK         #
########################


# Import package
import random
import codecs
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.metrics import categorical_accuracy

'''
1. 학습 데이터 생성
'''

'''
2. 모델 정의
'''
hidden_layer = 2    # 은닉층 개수
hidden_node = 8     # 은닉층 노드 개수

model = Sequential()
for i in range(hidden_layer):
    model.add(Dense(units=hidden_node, activation='relu'))
model.add(Dense(units=5, activation='softmax'))

# 모델 컴파일
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['categorical_accuracy'])

'''
3. 모델 학습
'''
model.fit()     # TODO: 데이터 생성하면 여기에 매개변수로 넣을 것!

'''
4. 학습 결과 확인
'''
loss_and_metrics = model.evaluate()     # TODO: 데이터 생성하면 여기에 매개변수로 넣을 것!
