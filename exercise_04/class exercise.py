import numpy as np

## 2-dimensinal

a = np.arange(10,30).reshape(4,5)

yellow = a[0,0]
red = a[0,1:4]
cyan = a[:,1::2]
blue = a[::2,-1]

#print(yellow)
#print(red)
#print(cyan)
#print(blue)

## 3-dimensinal cube

a = np.arange(27).reshape(3 ,3 ,3)

first = a[1,1,:]
secound = a[:,1,0]
thrid = a[0,:,2]

#print("first: ", first)
#print("secound: ", secound)
#print("third: ", thrid)

## masking

data = np.arange(1,101).reshape(10,10)

even = data[data % 2 == 0]
ends_with_6 = np.where(data % 10 == 6)

#print("even: ", even)
#print("ends with 6", data[ends_with_6])


## numpy and csv
file_name = "notebooks/data/befkbhalderstatkode.csv"
data = np.genfromtxt(file_name , delimiter=',',dtype=np.uint, skip_header=1)

#print("garman 0 years old: ", sum(data[(data[:,0] == 2015) & (data[:,2] == 0) & (data[:,3] == 5180)][:,-1]))

def info(AAR=2015, BYDEL=None, ALDER=None,STATKODE=None):

    maske_aar = data[:,0] == AAR
    maske_bydel = data[:,1] == BYDEL if BYDEL != None else True
    maske_age = data[:,2] == ALDER if ALDER != None else True
    maske_statkode = data[:,3] == STATKODE if STATKODE != None else True

    return sum(data[maske_aar & maske_bydel & maske_age & maske_statkode][:,-1])

#print(info())



