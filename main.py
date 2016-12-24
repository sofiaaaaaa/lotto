import csv

def makedata():
    with open('/Users/HyogeunKim/PycharmProjects/lotto/lottos_615.csv', 'rt') as f:
        reader = csv.reader(f)
        result = []

        for row in reader:
            result.append(row)

        return result


def duplication(data1, data2):
    result = []
    count = 0
    sortedata1 = sorted(data1)
    sortedata2 = sorted(data2)

    for datum1 in sortedata1:
        for datum2 in sortedata2:
            if datum1 == datum2:
                result.append(datum1)
                count += 1
            else:
                pass
    return count, result


dics1value = makedata()
dics2value = makedata()

print(dics1value)