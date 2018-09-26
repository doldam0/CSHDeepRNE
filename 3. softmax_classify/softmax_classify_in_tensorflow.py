import tensorflow as tf 
import numpy as np 
from sklearn.utils import shuffle

'''
1. 학습 데이터 생성
'''
M = 2		# 입력 데이터의 차원
K = 3		# 클래스 수
n = 100		# 각 클래스에 있는 데이터 수
N = n * K	# 전체 데이터 수

X1 = np.random.randn(n, M) + np.array([10, 0])
X2 = np.random.randn(n, M) + np.array([5, 5])
X3 = np.random.randn(n, M) + np.array([0, 10])

Y1 = [[1, 0, 0] for i in range(n)]
Y2 = [[0, 1, 0] for i in range(n)]
Y3 = [[0, 0, 1] for i in range(n)]

X = np.concatenate((X1, X2, X3))
Y = np.concatenate((Y1, Y2, Y3))

'''
2. 모델 정의
'''
W = tf.Variable(tf.zeros([M, K]))	# 가중치 행렬
b = tf.Variable(tf.zeros())			# 바이어스 벡터

x = tf.placeholder(tf.float32, [None, M])
t = tf.placeholder(tf.float32, [None, K])
y = tf.nn.softmax(tf.matmul(x, W) + b)

'''
3. 오차 함수 정의
'''
cross_entropy = tf.reduce_mean(-tf.reduce_sum(t * tf.log(y), reduction_indices=[1]))

'''
4. 최적화 기법 정의
'''
lr = 0.1	# 학습률
train_step = tf.train.GradientDescentOptimizer(lr).minimize(cross_entropy)

'''
5. 세션 초기화
'''
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

'''
6. 모델 학습
'''
epochs = 20
batch_size = 50
for epoch in range(epochs):
	_X, _Y = shuffle(_X, _Y)

	for i in range(N // batch_size):
		start = i * batch_size
		end = start + batch_size

		_x = _X[start:end]
		_y = _Y[start:end]