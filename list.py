my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15)
list2=[50,60,70]
my_list.extend(list2)
my_list.pop()
my_list.sort()
for i in my_list:
    if i==30:
        print(my_list.index(i))

