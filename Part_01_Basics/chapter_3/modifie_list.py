#list_name[index] = new_value
"""
append() → add an item.
insert() → insert an item at a specific position.
remove() → remove an item.
pop() → remove and return an item.

"""
names = ['sara', 'noor', 'musaab', 'abeer']
for i in names:
    print(f"new student name is: {i}")
print(f"\n\nafter make change in list : \n\n")
names[0] = 'hala'
for i in names:
    print(f"new student name is: {i}")
names.append('baba')
print("'\n\n")
for i in names:
    print(f"new student name is: {i}")
degree = []
degree.append(10)
degree.append(19)
degree.append(89)
for i in degree :
    print (f"degree is {i}")
print(degree)

print ("\n\n")
degree.insert(0,8)
print(degree)
print("\n\n")
del degree[0]
print(degree)
print("\n\n")
del degree[2]
print(degree)
print()
fruits = ["Apple", "Banana", "Orange"]
print(fruits)
favorite = fruits.pop(1)

print(favorite)
print(fruits)
print()
fruits.remove('Apple')
print(fruits)
