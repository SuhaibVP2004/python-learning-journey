text = input("Enter the sentence :")

character = 0
letter = 0
digit = 0
spaces = 0
vowels = 0
consonates = 0
uppercase = 0
lowercase = 0

for i in text:
    character+=1

    if i.isalpha():
        letter+=1

        if i.lower() in "aeiou":
            vowels+=1
        else:
            consonates+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace:
        spaces+=1

    if i.islower():
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    
    
        

    reversed = text[::-1]


print("\t----- Text Analysis -----\n")


print("\tCharacters =",character)
print("\tLetters =",letter)
print("\tDigits =",digit)
print("\tSpaces =",spaces)
print("\tVowels =",vowels)
print("\tConsonates =",consonates)
print("\tUpper case =",uppercase)
print("\tLower case =",lowercase)
print("\tReversed =",reversed)

