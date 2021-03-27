A Doubly Linked List utilizng Doubly nodes (Nodes with information of previous node and next node) is utilized for the problem set in order to reduce runtime (improve time complexity)

Union is scripted to accept 2 linked lists as arguments which are then converted into lists. The lists are then appended together and a "Set" object is utilized to retrieve the unique elements within the resulting list. The set is then converted back into a Linked List

Intersection takes in 2 linked lists and converts them to list through a scripted method termed as "to_list" for the class "LinkedList". Each elements within the first list are checked for duplication within the second list. A set is then created using the resulting list as input to return unique elements within the 2 lists. The set is then converted back into a LinkedList

Time Complexity:
Union ->    Overall, time complexity of the function call is O(n) which is mainly from the conversion of the Linked List into a list and the conversion of the list back to the Linked List

Intersection ->     Much Similar to Union, however with the exception of an additional "for" loop required to assess each elements within first list against the second list. Overall, this function call carries a runtime analysis of O(n)


Space Complexity:
Union ->    As each of the elements are kept within 4 separate containers (ls1, ls2, union_set and output), the space complexity for union increases linearly O(n) with increasing size of inputs to the function call

Intersection ->     Much like Union, elements within the DoublyLinkedList inputted as argument to the function call are kept within 3 separate containers (ls1, ls2, intersect_set and output). As such, the space complexity for intersection can be defined as linear O(n) as the complexity increases linearly with increasing size in inputs