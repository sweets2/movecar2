

file = 'app/data/rawdata/raw_hoboken_rules.txt'

data = []
with open(file, 'r') as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        data.append(line)



print(data)
# print(*data,sep="\n")
