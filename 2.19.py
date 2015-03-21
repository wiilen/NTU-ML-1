import numpy as np

def FileData():
    f=open("2train.dat")
    data_ori=[]
    data_set=[]
    for line in f:
        line_list=line.strip('\n').split()
        x_matrix=np.asarray(line_list,dtype=float)
        data_ori.append(x_matrix)        
    f.close
    for i in range(0,10):
        l=[x[i] for x in data_ori]
        data_set.append(l)
    return data_set

def ProduceTheta(x_dataset):
    theta=x_dataset+[-100,100]
    theta.sort()
    theta = [(theta[j]+theta[j+1])/2.0 for j in range(len(theta)-1)]
    return theta


def CalculateEin(x_dataset,y_noiseset,theta):
    Ein=[]
    for i in range(0,len(x_dataset)):
        err1=0
        for j in range(0,len(y_noiseset)):
            if (x_dataset[j]-theta[i])*y_noiseset[j]<0:
                err1+=1
        errRate1=err1/float(len(x_dataset))
        errRate2=1-errRate1
        Ein.append(errRate1)
        Ein.append(errRate2)
    return min(Ein)

data_set=FileData()
y=data_set[-1]
TEin=[]

for i in range(0,len(data_set)-1):
    x=data_set[i]
    theta=ProduceTheta(data_set[i])
    Ein=CalculateEin(x,y,theta)
    TEin.append(Ein)
print min(TEin)

