import os

def get_files_starting_with_deep(path):
    """
    This function takes a path as input and returns a list of filenames in that path
    that start with the string 'deep'.

    Args:
        path (str): The path to search for files starting with 'deep'.

    Returns:
        deep_files (list): A list of filenames in the given path that start with 'deep'.
    """
    deep_files = []
    for filename in os.listdir(path):
        if filename.startswith("deep"):
            deep_files.append(filename)
    return deep_files


if __name__ == "__main__":
    path = "Enter_your_path"
    deep_files = get_files_starting_with_deep(path)
    print("Files starting with 'deep':")
    for file in deep_files:
        print(file)
