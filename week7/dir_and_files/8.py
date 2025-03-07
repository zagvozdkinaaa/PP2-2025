import os

#Deletes a file if it exists and has write access.
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' has been deleted.")
        else:
            print(f"No write access to delete '{path}'.")
    else:
        print(f"File '{path}' does not exist.")

file_to_delete = input("Enter the path of the file to delete: ")
delete_file(file_to_delete)