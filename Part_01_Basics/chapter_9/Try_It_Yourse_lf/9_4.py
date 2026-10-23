class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")
        print(f"Customers the restaurante has served {self.number_served}")
    def open_restaurant(self):
        print("Welcome! The restaurant is open now :)")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Al Zaitonah", "Italian")

restaurant.describe_restaurant()
print()
restaurant.open_restaurant()
print()
restaurant.number_served = 23
print()
print("after update value :\n")
restaurant.set_number_served(90)
print()
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()
print()
print("after increment value :\n")
restaurant.set_number_served(90)
restaurant.describe_restaurant()
print()
restaurant.increment_number_served(7)
print()
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()

