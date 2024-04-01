file = open("cheese.txt", "r")

file_text = file.read()
print(file_text)

lines = file.readlines()
print(lines)

for line in file:
    print(line)

file.close()




# Create a file numbers.txt that has a few lines of numbers.
# Multipy all the number together and print the result.
# file = open("numbers.txt", "r")

# total = 1
# for line in file:
#     total *= int(line)
    
# print(total)

# file.close()