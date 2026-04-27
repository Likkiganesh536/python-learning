# write a program using for loop print even numbers

n=int(input('enter a number:'))
for i in range(n):
    if(i%2==0):
        print(i)     
       
print('-------------------')
#write a program using while loop print even numbers
n=int(input('enter a number:'))
i=0
while(i<n):
    if(i%2==0):
        print(i)
    i+=1
print('-------------------')


