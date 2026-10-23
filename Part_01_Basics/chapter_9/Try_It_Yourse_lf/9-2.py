class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("Welcome! The restaurant is open now :)")


restaurant1 = Restaurant("Al Zaitonah", "Italian")
restaurant2 = Restaurant("McDonald's", "Fast Food")
restaurant3 = Restaurant("Sakura", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
