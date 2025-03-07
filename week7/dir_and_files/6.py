import os

# Generate 26 text files named A.txt to Z.txt
for i in range(26):
    file_name = f"{chr(65 + i)}.txt"  # Generate file name from ASCII codes
    with open(file_name, "w") as file:
        file.write(f"This is file {file_name}\n")
    print(f"Created {file_name}")
