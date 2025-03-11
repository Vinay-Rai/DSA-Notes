from array import *

my_array = array("i",[4,2,6,8,3,1,5])
my_array1 = array("i",[1,5,4,2])

my_array.append(10)
my_array.insert(0,11)
my_array.extend(my_array1)

templist = [12,14,15]
my_array.fromlist(templist) #extend aray form list last three element comes from list datatype not array so fromlist method convert it from list to array

my_array.remove(12)
my_array.pop()

my_array.reverse()

my_array.buffer_info()

my_array.append(20)
my_array.count(4)  #no of occurence of element

print(my_array.tolist())
print(my_array[1:5])   #slicing


