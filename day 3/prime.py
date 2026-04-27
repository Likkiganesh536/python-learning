#using for loop to find whether a number is prime or not
n=int(input("enter a number:"))
for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break
else:
    print("prime")
print("----------------------")
#using while loop to find whether a number is prime or not
n=int(input("enter a number:"))
i=2
while i<n:
    if n%i==0:
        print("not prime")
        break
    i+=1
else:
    print("prime")
print("-----------------")