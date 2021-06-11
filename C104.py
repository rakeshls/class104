import csv
with open('heightWeight.csv',newline='')as f:
    reader= csv.reader(f)
    data =list(reader)
data.pop(0)
newData=[]
for i in range(len(data)):
    num=data[i][1]
    newData.append(float(num))
n = len(newData)
sum = 0
for x in newData :
    sum = sum+x
mean = sum/n
print('mean is '+str(mean)) 
print(newData)