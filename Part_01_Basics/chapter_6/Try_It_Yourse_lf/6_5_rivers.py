rivers = {
    "nile": "Egypt",
    "Mississippi": "America",   # if this is the river you meant
    "Euphrates": "Iraq"
}

for key , value in rivers.items():
    print(f"The {key} runs through {value}")
    print()

for value in rivers.keys():
    print(value)
    print()

for value in rivers.values():
    print(value)

