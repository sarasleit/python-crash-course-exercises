print("print num using range function")
for num in range(5):
    print(num)
print("print num using range function with specific  initial value and final value")
print()
for num in range(2,5):
    print(num)
print()
numbers = list(range(1,10))
print(numbers)
print("print num using range function with specific initial value and final value and step size value") 
numbers = list(range(2,10,2))
print(numbers)
print()
numbers = list(range(1,10,2))
print(numbers)
print()
print("initilaize empty list and fill it using append using (for & range)")
squers = []
for value in range(1, 11):
    square = value**2
    squers.append(square)
print(squers)
print()
print("find min , max , sum of given list")
print(min(squers))
print()
print(max(squers))
print()
print(sum(squers))

print("new_list = [expression for item in iterable]")


