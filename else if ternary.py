'''num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if(num1>num2):
    print(num1,"num1 is greater")
elif(num1<num2):
    print(num2,"num2 is greater")
else:
    print(num1,"=",num2)'''


'''ternary'''
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
print('num1 is greater'if num1>num2 else 'num2 is greater' if num2>num1 else 'equal' )