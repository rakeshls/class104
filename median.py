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
newData.sort()
if n%2==0:
    m1=float(newData[n//2])
    m2=float(newData[n//2-1])
    m= (m1+m2)/2
else:
    m=newData[n//2]
    print(m)
print('median is '+str(m))
