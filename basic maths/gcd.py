a=int(input("enter the number a"))
b=int(input("enter the number b "))
# we will take minimum of both the numbers because coomon factor is smallest .
small = min(a,b)
for i in range(1,small+1):
    if (a%i==0 and b%i==0):
            gcd=i
print("the gcd of number is " , gcd) 
