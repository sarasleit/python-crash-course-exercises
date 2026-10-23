glossary = {
    "variable": "A container that stores data.",
    "string": "A sequence of characters.",
    "list": "An ordered collection of items.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "Repeats a block of code."
        }
for key, value in glossary.items():
    print(f"{key.title()}")
    print("     "+value.title())
