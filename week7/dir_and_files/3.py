import os

def check_path(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return
    
    print("Directory exists")
    print("filename: ", os.path.basename(path))
    print("Directory portion: ", os.path.dirname(path))

path=input("Enter the directory path: ")
check_path(path)