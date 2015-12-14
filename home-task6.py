###### in worck ######
import random
import datetime

time = []
for n in range(2, 7):
    l = random.sample(range(10 ** n), 10 ** n)
#    print n
    start = datetime.datetime.now()
    l.sort()
    finish = datetime.datetime.now()
    r = finish-start
    time.append(r)
    print r, time
time = time[0 : : 5]
print time
#t = time[3] - time[2]
#print t


#start = datetime.datetime.now()
#for i in range(len(l) - 1):
#    for j in range(len(l) - i - 1):
#        if l[j] > l[j + 1]:
#            l[j], l[j+1] = l[j+1], l[j]
#finish = datetime.datetime.now()
#print (finish-start)

