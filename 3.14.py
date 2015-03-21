import numpy as np

def ProduceXData():
    x_dataset=[]
    i=0
    while i<1000:
        x_data1=2*np.random.random()-1.0
        x_data2=2*np.random.random()-1.0
        x_dataset.append([1,x_data1,x_data2,x_data1*x_data2,x_data1*x_data1,x_data2*x_data2])
        i+=1
    return np.asarray(x_dataset)

def ProduceYNoise(x_dataset):
    y_noiseset=[]
    for x_data in x_dataset:
        y_data=np.sign(x_data[1]*x_data[1]+x_data[2]*x_data[2]-0.6)
        y_noise = y_data*np.where(np.random.random()<0.1, -1, 1)
        y_noiseset.append(y_noise)
    return np.asarray(y_noiseset)

x_data=ProduceXData()
y_data=ProduceYNoise(x_data)
XtXi=np.linalg.pinv(np.dot(x_data.T,x_data))
Wlin=np.dot(np.dot(XtXi,x_data.T),y_data)

err=0
for i in range(0,len(y_data)):
    if np.sign(np.dot(x_data[i],Wlin))*y_data[i]<=0:
        err+=1

print Wlin
        
