For this problem set, a recursion approach was utilized as we are required to enter each of the directories and their associated subdirectories to search for any files that satisfy the suffix inputted as argument to the function call.

Time Complexity:
This function has a time complexity of O(n) as the function access each of the subdirectories and within the path inputted

Space Complexity:
The function traverses the directory and calls itself once with every traversal until the base condition have been met (a file has been reached). As such, all the directories and their associated sub-directories are visited at least once, resulting in a linear space complexity of O(n) 