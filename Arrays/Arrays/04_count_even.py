# #number = [10, 15, 20, 25, 30]
# count = 0   
#  for num in number 
# if num = num % 2 ==0
# count =0+1
# print(count)

numbers = [10, 15, 20, 25, 30]
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print("Count of even numbers:", count)
