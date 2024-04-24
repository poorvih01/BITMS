mon=input("enter the month")
if mon=='January' or mon=='march' or mon=='may' or mon=='jul' or mon=='aug' or mon=='oct' or mon=='dec':
    print("31 days")
elif mon=='apl' or mon=='june' or mon=='sep' or mon=='nov':
    print("30 days")
else:
    print("28/29 days")