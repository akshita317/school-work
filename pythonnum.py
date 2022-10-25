# Python program to check
# if a number is Harshad
# Number or not.

def checkHarshad( n ) :
	sum = 0
	temp = n
	while temp > 0 :
		sum = sum + temp % 10
		temp = temp // 10
	# Return true if sum of
	# digits is multiple of n
	return n % sum == 0

# Driver Code
if(checkHarshad(12)) : print("Yes")
else : print ("No")

if (checkHarshad(15)) : print("Yes")
else : print ("No")
	
# This code is contributed
# by Nikita Tiwari
