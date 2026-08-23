number = int(input("Enter a number: "))

new_num = number

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if new_num == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

