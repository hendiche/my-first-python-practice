file = open("employees.txt", "r")
print(file.readable())  # check if the file is readable or not

# print(file.readline())  # read one line
# print(file.read())  # read all

# print(file.readlines()) #read all line and return a array

for item in file.readlines():
    print(item)


file.close()

file = open("employees.txt", "a")
file.write("\ntoby - human resources")

file.close()

file = open("employees.txt", 'w')

file.write("\nkelly - customer services")

file.close()
