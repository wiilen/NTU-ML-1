import numpy as np
DATA=[]
Y=[]
W=[0.0,0.0,0.0,0.0,0.0]

def DataRead():
    f=open("train.dat")
    for line in f:
        line_list=line.strip('\n').split()
        t=line_list
        p=[1]
        for i in range(0,len(t)-1):
            p.append(float(t[i]))
        DATA.append(p)
        Y.append(int(t[-1]))
    f.close

def dotProductWithW(val):
    t=0
    for i in range(0,len(W)):
        t=t+W[i]*val[i]
    return t

def SignOfNum(num):
    if num>0:
        return 1
    else:
        return -1

def shift(val,y):
    for i in range(0,len(W)):
        W[i]+=y*val[i]

DataRead()

i=0
stopAt=0
ErrCount=0

while i<len(DATA):
    if SignOfNum(dotProductWithW(DATA[i])!=Y[i]):
        shift(DATA[i],Y[i])
        stopAt=i
        ErrCount+=1
    i+=1
    i%=len(DATA)
    if stopAt==i:
        break;

print W
print ErrCount
