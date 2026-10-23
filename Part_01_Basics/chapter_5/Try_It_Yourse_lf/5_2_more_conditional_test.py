# Tests for equality and inequality with strings
name = "Sara"

print("String equality:")
print(name == "Sara")          # True
print(name == "Ali")           # False

print("\nString inequality:")
print(name != "Ali")           # True
print(name != "Sara")          # False


# Tests using the lower() function
city = "AMMAN"

print("\nUsing lower():")
print(city.lower() == "amman")     # True
print(city.lower() == "irbid")     # False


# Numerical tests
number = 10

print("\nNumerical tests:")
print(number == 10)            # True
print(number == 5)             # False

print(number != 5)             # True
print(number != 10)            # False

print(number > 5)              # True
print(number > 20)             # False

print(number < 20)             # True
print(number < 5)              # False

print(number >= 10)            # True
print(number >= 15)            # False

print(number <= 10)            # True
print(number <= 5)             # False


# Tests using and / or
age = 20

print("\nUsing and:")
print(age > 18 and age < 30)   # True
print(age > 25 and age < 30)   # False

print("\nUsing or:")
print(age < 18 or age == 20)   # True
print(age < 18 or age > 30)    # False


# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]

print("\nUsing in:")
print("apple" in fruits)       # True
print("grape" in fruits)       # False


# Test whether an item is not in a list
print("\nUsing not in:")
print("grape" not in fruits)   # True
print("banana" not in fruits)  # False
