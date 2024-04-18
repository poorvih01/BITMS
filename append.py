poo=[]
n=int(input("enter the list size"))
for i in range(0,n):
    ele=int(input('enter the elements'))
    poo.append(ele)
print(poo)

prag=[]
n=int(input("enter the list size"))
for i in range(0,n):
    ele=int(input('enter the elements'))
    prag.append(ele)
print(prag)

for i in poo:
    for j in prag:
        if i ==j:
            print(i)





