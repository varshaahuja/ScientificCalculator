import csv

num1=[]
num2=[]
res=[]
i=0
with open('Unit Test Addition.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        num1.append(row[0])
        num2.append(row[1])
        res.append(row[2])

    while(i!=len(num1)):
        if(num1[i]+num2[i]==res[i]):
            print('i')

