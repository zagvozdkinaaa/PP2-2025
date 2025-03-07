import os

def count_lines(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return
    if os.path.isdir(path):
        print("The specified path is a directory, not a file.")
        return
    counter=0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            counter+=1
    print(f"Number of lines in the file: {counter}")

path=input("Enter the file path: ")
count_lines(path)