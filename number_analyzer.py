number = int(input("Enter the number : "))
print("Your number is :", number)

count = 0
sum = 0
product = 1
even = 0
odd = 0
largest = 0
smallest = 9
reversed = 0
original = number

while number > 0:
    digit = number % 10

    reversed = reversed * 10 + digit
    count += 1
    sum = sum + digit
    product = product * digit

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    number = number // 10


if reversed == original:
    palindrome = "Yes"
else:
    palindrome = "No"


print()
print("=" * 45)
print("             NUMBER ANALYZER")
print("=" * 45)

print("Original number :", original)
print("-" * 45)

print("Number of digits :", count)
print("Sum of digits   :", sum)
print("Product of digits:", product)
print("Even digits     :", even)
print("Odd digits      :", odd)
print("Largest digit   :", largest)
print("Smallest digit  :", smallest)
print("Reverse         :", reversed)
print("Palindrome      :", palindrome)

print("=" * 45)
print("          END OF NUMBER ANALYZER")
print("=" * 45)