numArray = input("Please entere a valid list of numbers separated by ,")
numArray = numArray.split(",")
uniques = []
for num in numArray:
    if num not in uniques:
        uniques.append(num)

print("Unique Numbers are ", sep=':')
for num in uniques:
    print(num, end=",")
