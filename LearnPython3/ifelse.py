num = input("Please enter a number to see the magic: ")
num = float(num)
range_start = 15
range_end = 30
if num >= range_start:
    if num <= range_end:
        print("The number you entered is between {start} and {end}".format(start=range_start, end=range_end))
    else:
        print("The number {0:.2f} is above {1:d}".format(num, range_end))
else:
    print(" The value is less than 15")