list = [2, 4, 6, 8, 20]
squares = []
iterator = iter(list)

def add10(num):
    return num+10

squares = [x**2 for x in list]
manip = [x**2 for x in list if x < 10]
#manip = [x**2 for x in list if x < 10 else add10(x)] #SyntaxError: invalid syntax
print('Manipulated:', manip)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print('Squared: ', squares)