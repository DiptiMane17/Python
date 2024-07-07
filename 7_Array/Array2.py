import array

my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array)
print(my_array[0])
my_array[2] = 10
print(my_array)
my_array.append(6)
print(my_array)
my_array.remove(10)
print(my_array)
