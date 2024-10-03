# LIBRARIES
# Import the os module, which provides a way to interact with the operating system
import os


# FUNCTIONS
def is_hidden(path):
    # Return bool if path is hidden, (hidden paths start with '.')
    return os.path.basename(path).startswith('.')

def generate_tree(startpath, prefix=''):
    # Define a recursive function to generate a tree-like structure of directories
    # Check if the current path is hidden
    # If hidden, return immediately without printing anything
    if is_hidden(startpath):
        return
    
    # Print the current directory name
    # Add indentation to the prefix for nested directories
    print(f"{prefix}└── {os.path.basename(startpath)}/")
    if prefix != "":
        prefix += '│    '
    else:
        prefix += '     '
    
    for entry in sorted(os.scandir(startpath), key=lambda e: e.name):
        if is_hidden(entry.path):
            continue
        
        if entry.is_dir():
            generate_tree(entry.path, prefix)
        else:
            print(f"{prefix}└── {entry.name}")


# MAIN
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(".")
    generate_tree(current_dir)

if __name__ == "__main__":
    main()
