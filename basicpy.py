# type for python
num_int = 1
num_flaot = 1.2
name = 'Sean' + ' ' + "Weng"
list = [num_int,num_flaot,name]
cell = (num_int,num_flaot)

# print in console
print("num_int: "+str(num_int))
for item in list:
    print(item)
print(list)
print(cell)

# function
def add(num_int, num_float):
    return num_int+num_float

# loop
num_str = ''
for it in range(0,10):
    num_str += str(it)
print(num_str)
for index in range(len(num_str)):
    if (index<1):
        print(num_str[index])
while (num_int < 5):
    num_int+=1

#condition
if (num_int>=5 and num_flaot<5):
    print (num_int)

# dictionary
index = {'name':"Sean Weng", 'gender':'','age':101}
print(index['name'])
print(index.keys())
index['gender'] = 'unknown'
print(index.values())

# candy
listA = []
listB = [1,2]
listA+=listB
print(listA)
print(listA[-1])
print([x for x in listA])

if __name__ == "__main__":
    print("this is basic python language tutorial!!")