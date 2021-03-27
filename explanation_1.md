An Ordered Dictionary is utilized for this problem due to the restriction of developing a solution with all of its operation taking only O(1) in terms of time complexity. 

As such, a map data structure was chosen for its efficiency in extracting value by using a key as input. 

An Ordered dictionary is prefered than a conventional dictionary due to the importance of the position of each key-value pair within the dictionary. With an ordered dictionary, the position of the key-value pairs can be manipulated at ease. For example, after getting a value from its respective key, we can easily push the key-value pair to the end of the dictionary as it has been recently utilized, making it the last item to be removed when setting new key-value pair to the dictionary that has reached its size limit. 

Time Complexity:
As an ordered dictionary is utilized, all operations, from pushing values in, getting values from dictionary an d sorting take a constant time (O(1))

Space Complexity:
All operations has a constant space complexity O(1), which is limited by the capacity of the LRU Cache as specified by users during initialization