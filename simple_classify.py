import numpy as np
import matplotlib.pyplot as plt

def step(x):
	return float(x > 0)

def y(x):
	return step(np.dot(w, x) + b)

def t(i):
	return float(i >= N)

d = 2		# 데이터의 차원
N = 10		# 각 패턴마다의 데이터 수
mean = 5	# 뉴런이 발화하는 데이터의 평균값

x1 = np.random.randn(N, d) + np.array([0, 0])			# 뉴런이 발화하지 않는 데이터
x2 = np.random.randn(N, d) + np.array([mean, mean])	# 뉴런이 발화하는 데이터

plt.figure()
plt.scatter(x1[:, 0], x1[:, 1])
plt.scatter(x2[:, 0], x2[:, 1], marker='>')

x = np.concatenate((x1, x2), axis=0)	# 데이터 합치기

w = np.random.randn(d)	# 가중치 벡터
b = np.random.randn()	# 바이어스

# 학습
count = 0
while True:
	classified = True
	for n in range(N * 2):
		count += 1
		print('training... (%d)' % count)

		delta_w = (t(n) - y(x[n])) * x[n]	# Δw 계산
		delta_b = t(n) - y(x[n])			# Δb 계산

		print(delta_w, delta_b)
		if not (all(delta_w == 0) and delta_b == 0):	# 모든 Δw와 Δb중 하나라도 0이 아니라면
			classified = False							# 분류 실패

		w += delta_w	# w값 갱신
		b += delta_b	# b값 갱신
	
	if classified:
		break

# 학습한 가중치화 바이어스 값 출력
print(w, b)

# 분류 그래프 설정
x_1 = np.arange(-4, 8, 0.01)
x_2 = (-w[0] * x_1 - b) / w[1]
plt.plot(x_1, x_2, color='k')

# 그래프 그리기
plt.grid()
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Result of Training')
plt.show()
