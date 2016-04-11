data = open("visdata.csv")

headers = data.readline()
print(headers)
templist = []
for line in data:
    line = line.strip()
    datalist = line.split(',')
    print(float(datalist[1]))
    templist.append(float(datalist[1]))

print(templist)

