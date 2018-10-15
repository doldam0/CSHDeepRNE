rep = [
    ['계란', '달걀'],
    ['덥밥', '덮밥'],
    ['카레덮밥', '카레라이스'],
    ['쥬스', '주스'],
    ['야쿠르트', '요구르트'],
    ['금귤', '귤'],
    ['감귤', '귤'],
    ['(찹쌀밥)', '찹쌀밥'],
    ['케익', '케이크'],
    ['케잌', '케이크'],
    ['찌게', '찌개'],
    ['추러스', '츄러스'],
    ['티라미슈', '티라미수']
]

if __name__ == "__main__":
    with open('data.csv', 'r', encoding='euc-kr', errors='ignore') as fin:
        with open('data_rg.csv', 'wt', encoding='euc-kr') as fout:
            while True:
                read = fin.readline()
                if not read:
                    break

                # 오타 수정
                for rep_item in rep:
                    read = read.replace(rep_item[0], rep_item[1])

                # 괄호 수정
                read = read.replace(')', '(')
                read_split = read.split('(')[::2]

                '''
                read_split = []
                num_of_comma = 0
                for i, item in enumerate(read):
                    if i != len(read) - 1:
                        if i % 2 == 0:
                            read_split.append(item)
                        else:
                            if ',' in item:
                                num_of_comma += 1
                    else:
                        for j in range(num_of_comma):
                            read_split.append(',')
                            read_split.append(item)
                '''

                read = ""
                for i in read_split:
                    read += i

                fout.write(read)

