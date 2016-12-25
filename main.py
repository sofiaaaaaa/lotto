import csv

# extract data from CSV file
def makedata():
    with open('lottos_615.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        orgindata = []

        for row in reader:
            orgindata.append(row)

        result = sorted(orgindata)
        return result

# extract duplication numbers
def dupcheck(idata):
    dupresult = []

    for i in range(len(idata)):
        for y in range(len(idata)):
            if idata[i] == idata[y]:
                dupresult.append(idata[i])
            else:
                pass

    return dupresult

data = makedata()
result = dupcheck(data)
print(result)