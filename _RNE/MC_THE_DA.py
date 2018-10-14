import numpy as np
import pickle

def what_class(classify, menu):
    print('1. 밥     2. 국     3. 주식')
    print('4. 부식   5. 간식   6. 기타(소스 등)')
    print('0. 공백   7. 지우기 8. 바꾸기')
    print(menu)
    print('INPUT> ', sep='')

    inp = int(input())
    if inp == 7:
        print('지울 데이터를 입력하세요> ', sep='')
        inp = int(input())

        remove_item(classify, inp)

    elif inp == 8:
        print('바꿀 데이터를 입력하세요> ', sep='')
        inp1 = input()

        print('1. 밥     2. 국     3. 주식')
        print('4. 부식   5. 간식   6. 기타(소스 등)')
        print('바꿀 분류항목을 입력하세요> ', sep='')
        inp2 = int(input())

        remove_item(classify, inp1)
        add_item(classify, inp1, inp2)

    else:
        add_item(classify, menu, inp)

def add_item(classify, menu, my_class):
    classify[my_class - 1].append(menu)

def remove_item(classify, menu):
    for item in classify:
        if menu in item:
            item.remove(menu)

def load_classify():
    with open('classify.pck', 'rb') as f:
        classify = pickle.load(f)
        return classify

def save_classify(classify):
    with open('classify.pck', 'wb') as f:
        pickle.dump(classify, f)

if __name__ == "__main__":
    classify = load_classify()
    print(classify)

    with open('data_enc.csv', 'r', encoding='euc-kr') as f:
        while True:
            read = f.readline()
            if not read:
                break

            for i, item in enumerate(read.split(',')):
                if 3 <= i <= 11:
                    is_exist = False
                    for array in classify:
                        if item in array:
                            is_exist = True
                            break

                    if not is_exist:
                        what_class(classify, item)
                        print(classify)
                        save_classify(classify)
