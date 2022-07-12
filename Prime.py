c=0
print("Enter number to be checked is prime number or not")
p=int(input())
for i in range(1,p+1):
	if(p%i==0):
		c=c+1
if(c==2):
	print(" Given Number ",p," is Prime Number")
else:
	print(" Given Number ",p," is a non Prime Number")




	



