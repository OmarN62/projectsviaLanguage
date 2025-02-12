def evenorodd():
    n = int(input("What's your number:"))
    if n % 2 == 0:
        print("Your number - " + str(n) + " - Is even.")
    elif n % 2 == 1:
        print("Your number - " +str(n) + " - Is odd.")
evenorodd()

def sumofNumbers():
    n = int(input("What's your number:"))
    sum = 0
    for i in range(1,n+1):
        sum += i
    print("Your sum is: " + str(sum))
sumofNumbers()

def reverseString():
    n = input("Enter a word: ")
    print("Your word reversed is " + n[::-1])
reverseString()

def factorial():
    n = int(input("Enter a number"))
    result = 1
    for i in range(1, n+1):
        result *= i
    print("Factorial: " + str(result))
factorial()

def largestNumber():
    numbers = [1,2,3,4,5]
    print("Your max number is: " + str(max(numbers)))
largestNumber()

def vowelCount():
    n = input("Enter a sentence: ")
    vowels = "aeiouAEIOU"
    count = 0

    for char in n:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
vowelCount()

def palindrome(string):
    if(string == string[::-1]):
        return "String is a palindrome"
    else:
        return "String is not a palindrome"

string = input("Enter a word: ")
print(palindrome(string))

