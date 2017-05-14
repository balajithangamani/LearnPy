import sys

numArray = sys.argv
uniques = []
for num in numArray:
    if num not in uniques:
        uniques.append(num)

print("Unique Numbers are ", end=':')
for num in uniques:
    print(num, sep=",")
