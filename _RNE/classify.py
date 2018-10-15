'''
1) 밥    2) 면    3) 국    4) 빵
5) 고기  6) 야채  7) 김치  8) 음료
9) 후식  10) 기타
'''
classify = [
    ['밥', '라이스'],
    ['면', '국수', '잔치국수'],
    ['국', '백숙', '찌개', '스프', '전골', '죽', '삼계탕'],
    ['빵', '케이크', '츄러스', '티라미수'],
    ['닭', '치킨', '돼지', '등심', '안심', '갈비',
     '목살', '고기', '연어', '고등어', '꽁치', '멸치볶음'],
    ['나물', '무침'],
    ['김치', '석박지', '깍두기'],
    ['우유', '요구르트', '주스', '요플레', '폴리또'],
    [],
    ['전']
]


if __name__ == "__main__":
    with open('data_rg.csv', 'r', encoding='euc-kr') as fin:
        with open('data_classify.csv', 'wt', encoding='euc-kr') as fout:
            while True:
                read = fin.readline()
                if not read:
                    break

                last_index = 10
                read_split = read.split(',')
                for i, class_item in enumerate(classify):
                    for j in range(i, last_index):
                        j_break = False
                        for cur in class_item:
                            if cur in read_split[j]:
                                tmp = read_split[i]
                                read_split[i] = read_split[j]
                                read_split[j] = tmp
                                j_break = True
                                break
                        if j_break:
                            break
                        else:
                            tmp = read_split[last_index]
                            read_split[last_index] = read_split[j]
                            read_split[j] = tmp


                result = ""
                for i, item in enumerate(read_split):
                    if len(item) > 0 and '0' <= item[0] <= '9':
                        result += item[0]
                    else:
                        result += item

                    if i != len(read_split) - 1:
                        result += ','
                result += '\n'
                fout.write(result)
