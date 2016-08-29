x=int(input("Enter a Number: "))
y=x
z=0
while(y!=0):
    z=z+y%10
    y=y/10
    y=int(y)
print("The sum of digits of",x," is ",z)
input("Press enter to close............")
