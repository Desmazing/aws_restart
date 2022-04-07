import json
filename = 'username.json'
name = ''

try:
    with open(filename, 'r') as rrr:
        name = json.load(rrr)
except IOError:
    print('first time login')

if name != '': 
    print("Welcome back, " + name + "!")
else: 
    name = input('Hello, what is your name?')

try:
    with open(filename, 'w') as f:
        name = json.dump(name, f)
except IOError:
    print('Try again')
