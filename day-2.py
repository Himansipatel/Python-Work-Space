#from util import my_sum
#print(my_sum(4,3))
import util
print(util.my_sum(4,4))

l=[1,2,3,4]
m=[]
counter=0
print(list(map(lambda x: x*2 , l)))
#for item in l:
#    l[counter]=item*2
#    counter=counter+1
   # m.append(item*2)

   # print(item*2)

#print(l)

for index,item in enumerate(l):
#    print("index = "+str(index))
#    print("item = " + str(item))
    l[index]=item*2

print(l)
