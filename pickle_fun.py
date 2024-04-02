import pickle

age = [23, 523, 5, 324, 632, 5, 35]

file = open("test.txt", "wb")
pickle.dump(age, file)
file.close()

file = open("test.txt", "rb")
new_age = pickle.load(file)
file.close()

print(new_age)
