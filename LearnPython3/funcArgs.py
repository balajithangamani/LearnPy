def showname(name, age=60):
    'Function simply displays the inputs'
    print("Name", name)
    print("Age", age)


def showname2(name, *vartuple, **vardict):
    'Advanced version of showname function'
    print("Name", ':', name)
    for tup_arg in vartuple:
        print(tup_arg, sep=':')
    for key in vardict:
        print(key,':', vardict[key])

showname("Anna")
showname("Bala", 34)
showname(34, "Bala")

# showname(34, name="Poda") #TypeError: showname() got multiple values for argument 'name'
# showname(name="Soma", 50) #SyntaxError: positional argument follows keyword argument

showname(age=78, name="hijnb")
showname("noname", age=8)

showname2("jack black")
showname2("balaji", 16, 'M', 'Chennai')
showname2("balaji", 16, sex='M', city='Chennai')