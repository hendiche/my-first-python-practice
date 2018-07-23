friends = ["michael", "at", "afuk", "someone"]

print("loop with array")
for friend in friends:
    print(friend)

print("loop with array length")
for index in range(len(friends)):
    print(friends[index])

print("loop with range")
for index in range(10):
    print(index)  # will start print from 0 to 9, not include 10

print("loop with specific range")
for index in range(3, 10):
    print(index)  # will print start from 3 to 9, not include 10


print("loop with if")
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")
