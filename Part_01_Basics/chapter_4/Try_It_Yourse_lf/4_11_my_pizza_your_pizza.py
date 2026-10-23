pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
frind_pizza = pizzas[:]
print (pizzas)
print(frind_pizza)
pizzas.append("tomato")
frind_pizza.append("mashroum")
print(pizzas)
print(frind_pizza)
print ()
print(f"my frind  favorite pizza is :")
for i in frind_pizza:
    print(f"{i}")

print(f"my favorite pizza is :")
for i in pizzas:
    print(f"{i}")

