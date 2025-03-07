import os

# Copy contents of one file to another
def copy_file(source, destination):
    if os.path.exists(source):
        with open(source, "r") as src, open(destination, "w") as dest:
            dest.write(src.read())
        print(f"Copied contents from {source} to {destination}")
    else:
        print(f"Source file {source} does not exist.")

file1=input("Enter the name of the file1: ")
file2=input("Enter the name of the file2: ")
copy_file(file1, file2)