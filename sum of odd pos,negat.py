num=[2,4,1,-3,-5,7]
neg=sum(i for i in num if i<0)
pos=sum(j for j in num if j%2==0)
odd=sum(k for k in num if k%2!=0 and k>0)
print(neg)
print(pos)
print(odd)