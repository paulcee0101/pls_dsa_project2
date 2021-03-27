import sys
from heapq import heapify, heappush, heappop

class LinkedListNode:
    def __init__(self, char=None, freq=None):
        # initialization of node with the following attributes
        self.character = char
        self.frequency = freq
        self.bit = None 
        self.counter = None # used for traversal of tree
        self.left = None
        self.right = None

    def get_character(self):
        return self.character

    def get_frequency(self):
        return self.frequency

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node
        
    def has_left_child(self):
        return self.get_left_child() is not None

    def has_right_child(self):
        return self.get_right_child() is not None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_counter(self):
        self.counter = 1

    def has_traversed(self):
        return self.counter == 1 

class PriorityQueue: # min-Heap construct using heapq
    def __init__(self, string):
        self.heap = list()
        self.size = 0
        self._freq_list = [] # list reserved for scenarios when frequency of certain unique characters are the same
        self.frequency_table = self._processing(string) # stores the unique characters and their respective frequencies in a dictionary 
        self._push(self.frequency_table) # initial _push function that populates the priority queue with the unique characters 

    def _processing(self, string):
        # preprocessing of string to generate character:frequency pair
        unique_chars_table = list()
        unique_chars = sorted(''.join(set(string))) # to retrieve unique characters within string and sorted in ascending order according to their respective ASCII value (capital letters come before their uncapitalized counterpart)
        for char in unique_chars:
            freq = string.count(char)
            new_node = LinkedListNode(char, freq)
            unique_chars_table.append(new_node)

        return unique_chars_table

    def push(self, node):
        # condition for secondary argument in cases where there is a duplicate in priority(frequency)
        if node.frequency in self._freq_list:
            heappush(self.heap, (node.frequency, 1 + self._freq_list.count(node.frequency), node)) # if any certain frequency is present within _freq_list, the incoming node to be pushed will get the next number in line in the Priority Queue
            self._freq_list.append(node.frequency) # to add the newly pushed frequency into _freq_list for considerations of possible later similar frequnecies
            self.size += 1

        else:
            heappush(self.heap, (node.frequency, 1, node))
            self._freq_list.append(node.frequency)
            self.size += 1

        self.sort() # sort the min-heap array 

        return None

    def _push(self, unique_chars_table):
        # initial push of preprocessed character:frequencies pair into the heap
        for node in unique_chars_table:
            self.push(node)

        return None
        
    def pop(self):
        popped = heappop(self.heap)
        self.size -= 1
        self.sort() # perform a sorting after an element has been popped from the heap

        return popped

    def sort(self):
        self.heap.sort()

class HuffmanTree:
    def __init__(self, heap):
        # initialization of a Huffman Tree by looping through the priority queue
        while heap.size > 1: 
            # popping out the first 2 elements from the heap
            node1 = heap.pop()[2]
            node2 = heap.pop()[2]
            # assigning the node with the appriopriate bit according to the order of popping from the heap
            node1.bit = str(0) 
            node2.bit = str(1)
            # computing the sum of node1 and node2 frequencies
            sum_freq = node1.frequency + node2.frequency
            # create an LinkedListNode instance using sum_freq
            new_node = LinkedListNode(freq=sum_freq)
            # assigning the left and right child accordingly
            new_node.set_left_child(node1)
            new_node.set_right_child(node2)
            # push the newly created node into the heap and sorted
            heap.push(new_node)
        # assigning the root node as the last element popped from the heap
        self.root = heap.pop()[2]

    def get_root(self):
        return self.root

    def huffman_encode(self, string):
        unique_chars = sorted(''.join(set(string)))
        self.huffman_dict = dict() # empty dictionary for the different huffman code of the unique characters
        huffman_code = '' # to be filled with the different bits corresponding the different nodes in the tree during traversion to the different leaf nodes from the root node

        def _huffman_encode_recursion(node, huffman_code):
            # recursive function to traverse from root to individual leaf nodes, where the respective unique characters are kept
            while len(self.huffman_dict) <= len(unique_chars): # exit condition
                
                # current node has left child and have not been traversed
                if node.has_left_child() and not node.get_left_child().has_traversed():
                    if node.bit is None:
                        pass
                    else:
                        if not node.has_traversed():
                            huffman_code += str(node.bit) # include code if current node has not been traversed
                    node.set_counter() # mark this node as traversed
                    _huffman_encode_recursion(node.get_left_child(), huffman_code)

                # current node has right child and have not been traversed
                elif node.has_right_child() and not node.get_right_child().has_traversed():
                    if node.bit is None:
                        pass
                    else:
                        if not node.has_traversed():
                            huffman_code += str(node.bit)
                    node.set_counter()
                    _huffman_encode_recursion(node.get_right_child(), huffman_code)

                else: # current node does not have left or right child - base condition
                    node.set_counter()
                    if node.character is not None:
                        huffman_code += str(node.bit)
                        self.huffman_dict[node.character] = (node.frequency, huffman_code) # add the character of the leaf node into huffman_dict with its correposning frequency and huffman_code
                    else:
                        pass
                    huffman_code = huffman_code[:-1] # remove the last bit from the huffman_code before returning to previous node
                    return
                
        _huffman_encode_recursion(self.get_root(), huffman_code)

        return None

    def huffman_decode(self, encoded):
        decoded = ''
        node = self.get_root() # get root node
        for bit in encoded:
            if bit == '0':
                node = node.get_left_child()
                if not node.has_left_child() and not node.has_right_child(): # if current node does not have any children
                    decoded += node.character # add current node's corresponding character into the decoded string
                    node = self.get_root() # initialize back to root node for next bit-guided traversal down the Huffman Tree

            else: # bit == '1'
                node = node.get_right_child()
                if not node.has_left_child() and not node.has_right_child():
                    decoded += node.character
                    node = self.get_root()

        return decoded

def huffman_encoding(string):
    if string is None:
        print(
"""
Please input valid String into the Huffman Tree..
Program will now Terminate...
"""
        )
        return
    # generation of priority queue
    heap = PriorityQueue(string)
    # generation of huffman tree
    tree = HuffmanTree(heap)
    # translation of the unique characters in terms of their binary counterpart
    tree.huffman_encode(string)
    # generation of encoded string
    encoded = ''
    for char in string:
        tmp_huffman_code = tree.huffman_dict[char][1]
        encoded += tmp_huffman_code

    return encoded, tree

def huffman_decoding(encoded, tree):
    return tree.huffman_decode(encoded)
    
    
if __name__ == "__main__":
    # Test Case 1
    print("-----------------------------------------TEST CASE 1-----------------------------------------")
    
    a_blank_sentence = None

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_blank_sentence)))
    print ("The content of the data is: {}\n".format(a_blank_sentence))

    huffman_encoding(a_blank_sentence)

    # Test Case 2
    print("-----------------------------------------TEST CASE 2-----------------------------------------")

    a_huge_sentence = """
Overview - Data Compression

In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.
    """

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_huge_sentence)))
    print ("The content of the data is: {}\n".format(a_huge_sentence))

    encoded_data, tree = huffman_encoding(a_huge_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Test Case 3
    print("-----------------------------------------TEST CASE 3-----------------------------------------")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))