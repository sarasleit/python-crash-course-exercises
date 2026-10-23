class Dog ():
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie' , '6')
your_dog = Dog('lucy', '3')


your_dog.sit()
your_dog.roll_over()


my_dog.sit()
my_dog.roll_over()
