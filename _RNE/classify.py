classify = [
    ['밥', '라이스', '면', '국수'],
    ['국', '찌개', '스프', '전골']
]


if __name__ == "__main__":
    with open('data_rg.csv', 'r', encoding='euc-kr') as fin:
        with open('data_classify.csv', 'wt', encoding='euc-kr') as fout:
            while True:
                read = fin.readline()
                if not read:
                    break

                read_split = read.split(',')
                for i, class_item in enumerate(classify):
                    for j in range(i, len(read_split)):
                        j_break = False
                        for cur in class_item:
                            if cur in read_split[j]:
                                print(i, j)
                                tmp = read_split[i]
                                read_split[i] = read_split[j]
                                read_split[j] = tmp
                                j_break = True
                        if j_break:
                            break

                result = ""
                print(read_split)
                for i, item in enumerate(read_split):
                    if len(item) > 0 and '0' <= item[0] <= '9':
                        result += item[0]
                    else:
                        result += item

                    if i != len(read_split) - 1:
                        result += ','
                result += '\n'
                fout.write(result)
