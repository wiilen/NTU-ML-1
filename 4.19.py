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

def greWreg(x,y,namda):
    xty=np.dot(x.T,y)
    xtxnumdai=np.asarray(np.dot((x.T),x)+namda*np.eye(3),dtype=float)
    Wreg=np.dot(inv(xtxnumdai),xty)
    return Wreg


data=FileData().tolist()

namda=1

fisdatax=np.asarray([x[0:-1] for x in data[0:40]],dtype=float)
sedatax=np.asarray([x[0:-1] for x in data[40:80]],dtype=float)
thdatax=np.asarray([x[0:-1] for x in data[80:120]],dtype=float)
fodatax=np.asarray([x[0:-1] for x in data[120:160]],dtype=float)
fivdatax=np.asarray([x[0:-1] for x in data[160:200]],dtype=float)

fisdatay=np.asarray([y[-1] for y in data[0:40]],dtype=float)
sedatay=np.asarray([y[-1] for y in data[40:80]],dtype=float)
thdatay=np.asarray([y[-1] for y in data[80:120]],dtype=float)
fodatay=np.asarray([y[-1] for y in data[120:160]],dtype=float)
fivdatay=np.asarray([y[-1] for y in data[160:200]],dtype=float)

fistrainx=sedatax+thdatax+fodatax+fivdatax
fistrainy=sedatay+thdatay+fodatay+fivdatay

setrainx=fisdatax+thdatax+fodatax+fivdatax
setrainy=fisdatay+thdatay+fodatay+fivdatay

thtrainx=sedatax+fisdatax+fodatax+fivdatax
thtrainy=sedatay+fisdatay+fodatay+fivdatay

fotrainx=sedatax+thdatax+fisdatax+fivdatax
fotrainy=sedatay+thdatay+fisdatay+fivdatay

fivtrainx=sedatax+thdatax+fodatax+fisdatax
fivtrainy=sedatay+thdatay+fodatay+fisdatay


w=greWreg(fistrainx,fistrainy,namda)

errx=0
for i in range(0,len(fisdatay)):
    if np.sign(np.dot(fisdatax[i],w))*fisdatay[i]<=0:
        errx+=1

w=greWreg(setrainx,setrainy,namda)

erry=0
for i in range(0,len(sedatay)):
    if np.sign(np.dot(sedatax[i],w))*sedatay[i]<=0:
        erry+=1

w=greWreg(thtrainx,thtrainy,namda)

errz=0
for i in range(0,len(thdatay)):
    if np.sign(np.dot(thdatax[i],w))*thdatay[i]<=0:
        errz+=1

w=greWreg(fotrainx,fotrainy,namda)

erra=0
for i in range(0,len(fodatay)):
    if np.sign(np.dot(fodatax[i],w))*fodatay[i]<=0:
        erra+=1

w=greWreg(fivtrainx,fivtrainy,namda)

errb=0
for i in range(0,len(fivdatay)):
    if np.sign(np.dot(fivdatax[i],w))*fivdatay[i]<=0:
        errb+=1

print (errx/float(len(fisdatay))+erry/float(len(sedatay))+errz/float(len(thdatay))+erra/float(len(fodatay))+errb/float(len(fivdatay)))/5.0

