numbers = [70, 20, 90, 40]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)