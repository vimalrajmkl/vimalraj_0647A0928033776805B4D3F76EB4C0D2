#we define function called factorial
def factorial(n):
#we check the value 
    if (n==1 or n==0):
       #calculate the factorial of 1 & 0 and print this value 
        return 1
     
    else:
         #we calculate the factorial value
        return (n * factorial(n - 1))
 
num = int(input("Enter a number: "))#input from the user
print("number : ",num)#display the user input
print("Factorial : ",factorial(num))#display the factorial which is given by the user