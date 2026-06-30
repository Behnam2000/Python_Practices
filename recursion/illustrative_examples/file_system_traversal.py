import os

def list_directory(path, indent=0):
    """Recursively print all files and folders under path"""

    name = os.path.basename(path)
    print(" " * indent + ("📁 " if os.path.isdir(path) else "📄 ") + name)

    if os.path.isdir(path):
        for entry in sorted(os.listdir(path)):
            full = os.path.join(path, entry)
            list_directory(full, indent + 4)   # recursive call for each item

list_directory("/home/behnam/Python/Python_Practices/recursion/illustrative_examples/movies")



# -----------------------------------------------
# computing total directory size recursively:
# -----------------------------------------------

def dir_size(path):
    """Return total size in bytes of all files under path"""

    if os.path.isfile(path):                             # base case: it's a file
        return os.path.getsize(path) 
    
    total = 0 
    for entry in os.listdir(path):                       # recursive case: directory
        total += dir_size(os.path.join(path, entry))

    return total

print(dir_size("/home/behnam/Python/Python_Practices"))