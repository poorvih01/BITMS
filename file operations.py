fp=open("xyz.txt","w")
fp.write("hiii")
print(fp)
if fp:
    print("done")
print(fp.closed)
fp.close()


fp1=open("xyz.txt",'a')#append
fp1.write("were are u from??")#write to a file
fp1.writelines("good weather")
print(fp1)
if fp1:
    print("done")
print(fp1.name)
fp1.close()


fp2=open("xyz.txt",'r')
print(fp2.read(5))
fp2.seek(0)#cursor points to the loc
print(fp2.readline(6))
print(fp2.mode)
fp2.close()
