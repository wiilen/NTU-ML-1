import numpy as np

def ProduceXData():
    x_dataset=[]
    i=0
    x_data=0
    while i<20:
        x_data=2*np.random.random()-1.0
        x_dataset.append(x_data)
        i+=1
    return x_dataset

def ProduceYNoise(x_dataset):
    y_noiseset=[]
    i=0
    y_data=0
    y_noise=0
    while i<20:
        y_data=np.sign(x_dataset[i])
        y_noise = y_data*np.where(np.random.random()<0.2, -1, 1)
        y_noiseset.append(y_noise)
        i+=1
    return y_noiseset

def ProduceTheta(x_dataset):
    theta=np.array(x_dataset+[-1,1])
    theta.sort()
    theta = np.array([(theta[j]+theta[j+1])/2.0 for j in range(theta.shape[0]-1)])
    return theta

def CalculateEin(x_dataset,y_noiseset,theta):
    Ein=[]
    for i in range(0,20):
        err1=0
        for j in range(0,20):
            if np.sign(x_dataset[j]-theta[i])*y_noiseset[j]<0:
                err1+=1
        errRate1=err1/20.0
        errRate2=1-errRate1
        Ein.append(errRate1)
        Ein.append(errRate2)
    return min(Ein)

totalEin=0
i=0
while i<5000:
    x_data=ProduceXData()
    y_noise=ProduceYNoise(x_data)
    theta=ProduceTheta(x_data)
    Ein=CalculateEin(x_data,y_noise,theta)
    totalEin+=Ein
    i+=1
print totalEin/5000.0



