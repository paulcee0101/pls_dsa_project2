import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories

    Thre are no limit to the depth of the subdirectories

    Args:
        suffix(str): suffix of the file name to be found
        path(str): path of the file system

    Returns:
        a list of paths
    """
    # utilizing recursion to traverse all the directories within the inputted path and search for the desired suffix
    files = list()
    
    def _find_file(files, suffix, path):
        new_dir = list()
        for p in path:
            if os.path.isdir(p):
                new_dir += [os.path.join(p, f) for f in os.listdir(p)]
            else:
                if os.path.isfile(p):
                    if os.path.splitext(p)[1] == suffix:
                        files.append(p)

        if new_dir:
            _find_file(files, suffix, new_dir)
        else:
            return

    _find_file(files, suffix, path)

    return files

if __name__ == "__main__":
    # Test Case 1
    print("-----------------------------------------TEST CASE 1-----------------------------------------")
    
    files = find_files(".xyz", [r".\testdir"]) # please run the script at the same directory as "testdir" folder structure example
    print(files) # returns an empty list as there are no suffix with '.xyz'

    # Test Case 2
    print("-----------------------------------------TEST CASE 2-----------------------------------------")

    files = find_files(".h", [r".\testdir"])
    print(files) # returns 4 files with suffix ending '.h'

    # Test Case 3
    print("-----------------------------------------TEST CASE 3-----------------------------------------")

    files = find_files(".c", [r".\testdir"]) # please run the script at the same directory as "testdir" folder structure example
    print(files) # returns 4 files with suffix ending '.c'