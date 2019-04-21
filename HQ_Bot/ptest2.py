from _ast import Num
l = [0,1,2,3,4]
xx = 21

for num in range(xx):
    l_num =  (num % len(l))
#     print(l_num)
    print(l[l_num])

