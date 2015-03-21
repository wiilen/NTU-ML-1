import numpy as np

def fileRead():
    f=open("train.dat")
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

def naive_pla(data_set):
    w=np.asarray([0,0,0,0,0],dtype=float)
    iteration=0
    update=0
    while True:
        iteration+=1
        false_data=0
        for data in data_set:
            if np.dot(w,data[0])*data[1]<=0:
                false_data+=1
                update+=1
                w+=data[0]*data[1]
        print 'iter%d (%d / %d)' % (iteration, false_data, len(data_set))
        if false_data == 0:
            break
    print(update)


naive_pla(fileRead())

    
