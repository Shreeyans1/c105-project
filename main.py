import csv
import pandas as pd
import math

with open("data.csv",newline = '') as f:
    r1 = csv.reader(f)
    data1 = list(r1)

data = data1[0]

def mean(data):
    total = 0
    n = len(data)
    for i in data:
        total = total+int(i)
    mean = total/n
    return mean

sq_list = []
for i in data:
    a = int(i)-mean(data)
    a = a*a
    sq_list.append(a)

sum = 0
for i in sq_list:
    sum = sum+i

result = sum/(len(data)-1)
std_dev = math.sqrt(result)
print(std_dev)