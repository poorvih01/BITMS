apple=[10,5,30,40,50]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
#print(apple[4])
print("for iteration")
for i in apple:
    print(i)
    
apple[1]=-100
apple[2]=(90,67)#one index can contain multiple values oly in python
print(apple)#muteable
print(apple[-1])
apple[3]=500,600,700
print(apple)
apple[1:4]=(-10,-20,-30,-40,-50,-60)#dynamically added ,list is not fixed
print(apple)