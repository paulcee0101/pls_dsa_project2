class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        cur_head = self.head
        new_node = Node(value)
        while cur_head.next is not None:
            cur_head = cur_head.next
        cur_head.next = new_node
        self.size += 1
        
    def get_size(self):
        return self.size

    def to_list(self):
        out_list = []
        node = self.head

        while node is not None:
            out_list.append(node.value)
            node = node.next

        return out_list

def union(list_1, list_2):
    """
    Function to find the union between 2 Linked List.
    Run Time Analysis: Presence of a single For Loops, indicating a Big-O of O(n)
    1. Iterating through each element in the union_set in order to be appended to a newly defined Linked List - O(n)
    """
    # computing a set of the union of 2 linked list
    ls1 = list_1.to_list()
    ls2 = list_2.to_list()

    union_set = set(ls1 + ls2)

    out = LinkedList()
    for element in union_set:
        out.append(element)

    return out

def intersection(list_1, list_2):
    """
    Function to find the intersection between 2 Linked List.
    Run Time Analysis: Presence of 2 For Loops, resulting in a Big-O of O(2n), which can simply be written as O(n)
    1. Iterating through each element within list_1 and cross checking with list_2 - O(n)
    2. Iterating through each element in the intersection_set in order to be appended to a newly defined Linked List - O(n)
    """
    # computing a set of the intersection of 2 linked list
    ls1 = list_1.to_list()
    ls2 = list_2.to_list()

    intersect_set = set([element for element in ls1 if element in ls2])

    out = LinkedList()
    for element in intersect_set:
        out.append(element)

    return out

if __name__ == "__main__":
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (f'Union: {union(linked_list_1,linked_list_2)}\n')
    print (f'Intersection: {intersection(linked_list_1,linked_list_2)}\n')

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (f'Union: {union(linked_list_3,linked_list_4)}\n')
    print (f'Intersection: {intersection(linked_list_3,linked_list_4)}\n')