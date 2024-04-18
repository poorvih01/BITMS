#set method
'''state={"GOA","KARNATAKA","TN","AP"}
print(state)
print(type(state))
print("looping through set elemnts")
for i in state:
    print(i)'''
    
    
    
'''set1={10,20,30,40,50,60,70,80,90,90,100}
print(set1)#set is unordered ,removes duplicates,immuteable(v cannot access)



districts=set(["ooty","bly","bangl"])
print(districts)
districts.add("kanyakumari")
districts.update(["kovai","chennai"])
'''for i in districts:
    print("    ",districts)'''
print(districts)
districts.discard("chennai")
print(districts)
districts.remove("kovai")#if v use remove if the ele  not there it shows an error ,v can use discard  so that error does not occur
print(districts)
districts.pop()#pops random ele.
print(districts)
districts.clear()#clears all ele in set
print(districts)'''
    
    
