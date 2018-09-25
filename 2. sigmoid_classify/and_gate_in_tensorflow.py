import tensorflow as tf 
import numpy as np 

'''
1. 학습 데이터 생성
'''
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [0], [0], [1]])

'''
2. 모델 정의
'''
w = tf.Variable(tf.zeros([2, 1]))	# 가중치 벡터
b = tf.Variable(tf.zeros([1]))		# 바이어스

x = tf.placeholder(tf.float32, shape=[None, 2])	# 입력 벡터
t = tf.placeholder(tf.float32, shape=[None, 1])	# 정답
y = tf.nn.sigmoid(tf.matmul(x, w) + b)			# 출력

'''
3. 오차 함수 정의
'''
cross_entropy = -tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))

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
epochs = 200	# 전체 에폭수
for epoch in range(epochs):
	sess.run(train_step, feed_dict={
		x: X,
		t: Y
	})

'''
7. 학습 결과 확인하기
'''
correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)
classified = correct_prediction.eval(session=sess, feed_dict={
	x: X,
	t: Y
})
print('classified: ', classified, sep='\n')

prob = y.eval(session=sess, feed_dict={
	x: X,
	t: Y
})
print('output probobility: ', prob, sep='\n')
