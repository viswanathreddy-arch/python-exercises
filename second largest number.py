number = [10, 5, 8, 20, 20, 3]

largest = number[0]
second_largest = number[0]

for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"Second Largest Number: {second_largest}")