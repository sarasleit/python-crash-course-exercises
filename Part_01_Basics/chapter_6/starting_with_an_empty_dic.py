alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['pointes']= 5
print(alien_0)
alien_0['color']= 'red'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'fast':
    x_increment = 3
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 1

alien_0['x_position'] = x_increment + alien_0['x_position']

print("New x-position: " + str(alien_0['x_position']))
del alien_0['speed']
print(alien_0)

