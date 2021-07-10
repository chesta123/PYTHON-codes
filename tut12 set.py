s=set()
# print(type(s))
i = [1,2,3]
name = set(i)
# print(name)
s.add(1)
s.add(1)
s.add(2)
s1=s.intersection({1,2,3,4,5})
s1.remove(2)
# print(s,s1)
print(s1)


# set contains uniques things only unlike lists
