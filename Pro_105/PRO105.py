import math
import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

o =0
for i in squared_list:
    o = o+ i

res = o/(len(data)-1)


std = math.sqrt(res)
print(std)
