favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
print 
for name in favorite_languages.values():
    print(name.title())
print 
for key , value in favorite_languages.items():
    print(f"{key},{value}")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
