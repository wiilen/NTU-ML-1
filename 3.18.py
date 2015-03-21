import numpy as np
from math import exp

def FileData():
    f=open("3train.dat")
    data_set=[]
    for line in f:
        line_list=line.strip('\n').split()
        data_set.append(line_list)
    f.close
    return np.asarray(data_set,dtype=float)

def FileData1():
    f=open("3test.dat")
    data_set1=[]
    for line in f:
        line_list=line.strip('\n').split()
        data_set1.append(line_list)
    f.close
    return np.asarray(data_set1,dtype=float)

def greEin(x,y,w):
    wtx=np.dot(x,w)
    theta=exp(-np.dot(y,wtx))/(1+exp(-np.dot(y,wtx)))
    n=len(y)
    ge=[]
    for i in range(0,20):
        xrow=[t[i] for t in x]
        yx=np.dot(theta,-np.dot(y,xrow))
        gein=1/float(n)*(theta*(yx))
        ge.append(gein)
    return ge


w=[]
for i in range(0,20):
    w.append(0)

data=FileData().tolist()
x=[x[0:-1] for x in data]
y=[y[-1] for y in data]



j=0
while j<2000:
    g=greEin(x,y,w)
    w-=np.dot(0.01,g)
    j+=1

data_set1=FileData1().tolist()
c=[c[0:-1] for c in data_set1]
d=[d[-1] for d in data_set1]

err=0
for i in range(0,len(d)):
    if np.sign(np.dot(c[i],w))*d[i]<=0:
        err+=1

print err
