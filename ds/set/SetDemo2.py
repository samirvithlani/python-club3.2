user1= {"ram", "shyam", "hari", "gita"}
user2= {"hari", "sita", "rita", "gita"}


# Intersection
ans = user1.intersection(user2)
print(ans)
ans = user1 & user2
print(ans)

# Union
ans = user1.union(user2)
print(ans)

ans = user1 | user2
print(ans)

# Difference
ans = user1.difference(user2)
print(ans)

ans = user1 - user2
print(ans)

# Symmetric Difference
ans = user1.symmetric_difference(user2)
print(ans)


