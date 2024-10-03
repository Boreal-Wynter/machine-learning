''' RUN
python create_file_diagram.py
'''


# LIBRARIES
# Import the os module, which provides a way to interact with the operating system
import os


# FUNCTIONS
def is_hidden(path):
    # Return bool if path is hidden, (hidden paths start with '.')
    return os.path.basename(path).startswith('.')

def generate_diagram(startpath, prefix=''):
    # scan the repository and create a list of the folders and file.
    repo_list = [e for e in os.scandir(startpath) if not is_hidden(e.path)]
    # Go through repo_list, `enumerate` gets the element and index
    for i, entry in enumerate(repo_list):
        # Check if it the last element
        is_last = (i == len(repo_list) - 1)
        # Chekc if the entry is a directory
        if entry.is_dir():
            # Output directory
            print(f"{prefix}{'└──' if is_last else '├──'} /{entry.name}")
            # Recursively call function
            generate_diagram(entry.path, prefix + ('    ' if is_last else '│   '))
        else:
            # Output file
            print(f"{prefix}{'└──' if is_last else '├──'} {entry.name}")


# MAIN
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Root node
    print(".")
    # Generate file diagram
    generate_diagram(current_directory)

if __name__ == "__main__":
    main()
