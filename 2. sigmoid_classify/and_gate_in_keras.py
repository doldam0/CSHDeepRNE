from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
import numpy as np 
import matplotlib.pyplot as plt

'''
1. 학습 데이터 생성
'''
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [0], [0], [1]])

'''
2. 모델 정의
'''
model = Sequential()
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer=SGD(lr=0.1), loss='binary_crossentropy')

'''
3. 모델 학습
'''
hist = model.fit(X, Y, batch_size=1, epochs=200)

'''
4. 학습 결과 확인
'''
classes = model.predict_classes(X, batch_size=1)
prob = model.predict_proba(X, batch_size=1)

print('classified: ', Y == classes, sep='\n')
print('output probability: ', prob, sep='\n')