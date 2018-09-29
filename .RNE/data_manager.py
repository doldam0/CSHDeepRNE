import numpy as np 
import pickle

'''
데이터 읽어들여 피클로 저장하기
'''
def import_data():
	result = []
	with open('.RNE/data.csv', 'r') as f:	# CSV 파일 열기
		while True:
			read = f.readline()				# 한 줄 읽어들이기
			if not read:
				break

			row_data = [item for item in read.split(',')]	# 쉼표 기준으로 끊어 리스트 생성
			result.append(row_data)		# 생성한 리스트 데이터에 추가
	
	with open('.RNE/data.pickle', 'wb') as f:
		pickle.dump(result, f)

'''
피클로 저장한 데이터 불러오기
'''
def get_data_list():
	with open('data.pickle', 'rb') as f:
		data = pickle.load(f)
		return data

'''
메뉴 데이터와 잔반량 반환
'''
def get_menu_data():
	data = get_data_list()
	return np.array(data[:, 5:15])

'''
모든 데이터 반환
'''
def get_all_data():
	data = get_data_list()
	return np.array(data)


if __name__ == "__main__":
	import_data()