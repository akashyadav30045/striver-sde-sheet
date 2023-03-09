#approach 1 using string slicing

num = 85
print(str(num)[::-1])

#approach 2

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))