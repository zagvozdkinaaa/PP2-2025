import os

def list_contents(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return
    
    only_dirs=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    only_files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all=os.listdir(path)

    print(only_dirs)
    print(only_files)
    print(all)

path=input("Enter the directory path: ")

list_contents(path)