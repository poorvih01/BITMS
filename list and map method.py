'''x,y=[int(x) for x in input().split()]
print(x)
print(y)--->list'''

'''x,y=map(int,input().split())
print(x)
print(y)'''


numb=[10,20,30,40,50]
double_no=[num*2 for num in numb]
print(double_no)

'''prev in normal for loop
numb=[10,20,30,40,50]
double_num=[]
for num in numb:
    double_num.append(num*2)
print(double_num)'''


#condidtionals in list comphrhnsion
#filtering enen nos from list
'''even_no=[num for num in range(1,20) if num%2==0 ]
print(even_no)'''


a="bc"
vowels="aeiou"
vowel=[char for char in a if char in vowels]
print(vowel)