givenString = str.lower(input("Enter a string:"))
vowels = ['a', 'e', 'i', 'o', 'u']
vowelcount = 0
i = 0
while i < len(givenString):
    if givenString[i] in vowels:
        vowelcount +=1
    i += 1


print("The given string has ", str(vowelcount), " vowels")
