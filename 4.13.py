import numpy as np
from math import exp
from numpy.linalg import inv

def FileData():
    f=open("4train.dat")
    data_set=[]
    for line in f:
        line_list=[1]+line.strip('\n').split()
        data_set.append(line_list)
    f.close
    return np.asarray(data_set,dtype=float)

def FileData1():
    f=open("4test.dat")
    data_set=[]
    for line in f:
        line_list=[1]+line.strip('\n').split()
        data_set.append(line_list)
    f.close
    return np.asarray(data_set,dtype=float)

def greWreg(x,y,namda):
    xty=np.dot(x.T,y)
    xtxnumdai=np.asarray(np.dot((x.T),x)+namda*np.eye(3),dtype=float)
    Wreg=np.dot(inv(xtxnumdai),xty)
    return Wreg


data=FileData().tolist()
x=np.asarray([x[0:-1] for x in data],dtype=float)
y=[y[-1] for y in data]
namda=0.1
    
data_set1=FileData1().tolist()
c=[c[0:-1] for c in data_set1]
d=[d[-1] for d in data_set1]

w=greWreg(x,y,namda)
errx=0
for i in range(0,len(y)):
    if np.sign(np.dot(x[i],w))*y[i]<=0:
        errx+=1

erry=0
for i in range(0,len(d)):
    if np.sign(np.dot(c[i],w))*d[i]<=0:
        erry+=1
        
print errx/float(len(y)),erry/float(len(d))

