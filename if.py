'''if(5>10):
    print('yes')
else:
    print("no")'''


'''age1=int(input('enter age1'))
age2=int(input('enter age2'))
if(age1>age2):
    age3=age1+age2
    print(age3)
else:
    age3=age1-age2
    print(age3)'''



email="poorvi@gmail.com"
pwd=1234
otp=12
email1=str(input("enter email"))
password=int(input("enter pw"))
if(email == email1):
    if(pwd == password):
       print("login success")
       ot=int(input("enter otp"))
       if(otp==ot):
              print("transacation sucess")
       else:
              print("unsucess")
    else:
        print("failed due to pwd")
else:
    print("failed due to email")
    