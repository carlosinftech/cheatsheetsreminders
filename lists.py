listitems = ['item1','item2','item3','item4']
#Unpacking only available in python 3
var1,var2,var3,var4 = listitems

print(var1)
print(var2)
print('--end of lists--')

#List of objects


class Item:
    def __init__(self,name):
        self.name = name

items = [
    Item('item object 1'),
    Item('item object 2'),
    Item('item object 3'),
    Item('item object 4')
]

var1,var2,*others = items

print(var1.name)
print(var2.name)
print(others)
print("others one by one----")
for other in others:
    print(other.name)