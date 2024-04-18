'''day1={"monday","tue","wed","thur","sun"}
day2={"fri","sat","sun"}
print(day1|day2)#printing use or

day1={"monday","tue","wed","thur"}
day2={"fri","sat","sun"}
print(day1.union(day2))#printing using union


set1={1,2,3}
set2={2,3,4}
set3={3,4,5,6}
common=set1.union(set2,set3)#finding common among 3 sets
print(common)'''


'''day1={"monday","tue","wed","thur"}
day2={"fri","sat","sun"}
print(day1&day2)#intersection of two sets


set1={"prag","poo","guubbi","subbi"}
set2={"pavi","div","sindhu","prag"}
set3=set1.intersection(set2)
print(set3)'''

'''day1={"mon","tue","wed","thur"}
day2={"mon","tue","sun"}
print(day1-day2)#difference

day1={"mon","tue","wed","thur"}
day2={"mon","tue","sun"}
print(day1.difference(day2))'''


a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b#symmetric operator:common ele are removed 
print(c)

a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a.symmetric_difference(b)
print(c)