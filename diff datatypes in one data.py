'''matrix=[[j for j in range(5)] for i in range(3)]
print(matrix)#returntype is list'''


'''integer_input=list(map(int,input("enter integer separated by space:").split()))
float_input=list(map(float,input("enter float separated by space:").split()))
string_input=list(map(str,input("enter string separated by space:").split()))
print("integer input:",integer_input)
print("float input:",float_input)
print("string input:",string_input)'''


#storing multiple data types in the same variable using list.
data=list(map(int,input("enter integers separted by space:").split()))
data.extend(map(float,input("enter float separted by space:").split()))
data.extend(map(str,input("enter integers separted by space:").split()))
print("data:",data)





