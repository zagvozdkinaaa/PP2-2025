import os

data = []
n = int(input("Enter the number of items: "))
for i in range(n):
    item = input("Enter an item: ")
    data.append(item)

file_name = "output.txt"

if os.path.exists(file_name):
    print(f"File '{file_name}' already exists and will be overwritten.")
else:
    print(f"Creating new file '{file_name}'.")

with open(file_name, "w") as file:
    for item in data:
        file.write(item + "\n")

print(f"List has been written to {file_name}")
