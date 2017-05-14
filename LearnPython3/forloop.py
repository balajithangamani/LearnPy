givenString = str.lower(input("Enter a string:"))
vowels = ['a', 'e', 'i', 'o', 'u']
vowelcount = 0
for character in givenString:
    if character in vowels:
        vowelcount += 1

print("The given string has "+ str(vowelcount) + " vowels")
