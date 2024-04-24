pine=[10,20,30]
kiwi=[10,20,30]
print("id of pine:",id(pine))
print("id of kiwi:",id(kiwi))
print(pine is kiwi)  #checks for both datatype n value(in list even if both r same it contains diff address) 
print(pine == kiwi)  #checks only value