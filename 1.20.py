import numpy as np
import random
from random import shuffle

def fileRead():
    f=open("train1.dat")
    data_set=[]
    for line in f:
        line_list=line.strip('\n').split()
        x=[1]+line_list[0:4]
        x_matrix=np.asarray(x,dtype=float)
        y=int(line_list[-1])
        data_list=[x_matrix,y]
        data_set.append(data_list)
    f.close
    return data_set

def random_pocket(data_set):
    w=np.asarray([0,0,0,0,0],dtype=float)
    ww=w.copy()
    ww_false_data=400
    update=0
    while True:
        false_data=0
        c=random.choice(data_set)
        if np.dot(w,c[0])*c[1]<=0:
            update+=1
            w+=c[0]*c[1]
            for data in data_set:
                if np.dot(w,data[0])*data[1]<=0:
                    false_data+=1
                    if false_data < ww_false_data:
                        ww_false_data=false_data
                        ww=w.copy()
        if update==100:
            break
    return ww

def fileRead2():
    f=open("test.dat")
    data_set2=[]
    for line in f:
        line_list=line.strip('\n').split()
        x=[1]+line_list[0:4]
        x_matrix=np.asarray(x,dtype=float)
        y=int(line_list[-1])
        data_list=[x_matrix,y]
        data_set2.append(data_list)
    f.close
    return data_set2

def ErrRate(data_set2,ww):
    Err=0
    rate=0
    for d in data_set2:
        if np.dot(ww,d[0])*d[1]<=0:
            Err+=1
    rate=Err/float(len(data_set2))
    return rate

i=0
sumRate=0
l=fileRead2()
k=fileRead()
while i<20:
    sumRate+=ErrRate(l,random_pocket(k))
    i+=1
print sumRate/20.0

