#Create three sets from the lists you created before
#s1 = all ints between 1 and 20 inclusive
s1 = set(list(range(1, 21)))
print(s1)

#s2 = all even ints between 1 and 20 inclusive
s2 = set(list(range(2, 21, 2)))
print(s2)

#s3 = all ints divisible by 3 between 1 and 20 inclusive
s3 = set(list(range(3, 21, 3)))
print(s3)

#Save to a new set s4 all items in s1 not in s2
s4 = s1.difference(s2)
print(s4)


#Save to a new set s5 all items in both s1 and s3
s5 = s1.union(s3)
print(s5)


#Print out all items in both s2 and s3
print(s2.intersection(s3))
