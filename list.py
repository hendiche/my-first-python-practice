friends = ['michael', 'AT', 'afuk', "yolaa"]
nums = [10, 4, 8, 15, 16, 23, 42]

print(friends[2:])
print(friends[1:3])

friends.extend(nums)  # concat 2 arrays into 1 array
print(friends)
friends.append("true")
print(friends)
friends.insert(1, "CKOH")
print(friends)
friends.remove("CKOH")
print(friends)
# friends.clear() #remove all the value
# print(friends)
friends.pop()
print(friends)

print(friends.index("michael"))
friends.append('AT')
print(friends.count("AT"))
nums.sort()
print(nums)
nums.reverse()
print(nums)

copy = friends.copy()
print(copy)
