import csv
import pandas as pd
import plotly.express as px

with open("class1.csv",newline = '') as f:
    r1 = csv.reader(f)
    data = list(r1)

data.pop(0)
total = 0
n = len(data)
for i in data:
    total = total+float(i[1])

mean = total/n
print(mean)

df = pd.read_csv("class1.csv")
fig = px.scatter(df,x = "Student Number",y = "Marks")
fig.update_layout(shapes = [dict(type = 'line',x0 = 0,y0 = mean,x1 = n,y1 = mean)])
fig.show()