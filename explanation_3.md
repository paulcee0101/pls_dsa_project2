THis exercise can be segregated into 3 portions:
1. Building the Huffman Tree
2. Generating the Encoded Data
3. Decoding the Encoded Data

I. Building the Huffman Tree

A priority queue was created by utilizing a min heap data structure as the order of the elements within the container is important, and min heap provides a lower complextiy in sorting of its elements. The priority queue is important as it is the data structure to push the elements into the Huffman Tree 

A Tree Data Structure is chosen to be the basis of the Huffman Tree as it provides the perfect avenue for the creation of the bit codes for the different alphabets

Time Complexity:
Priority Queue has a time complexity of O(n) due to the presence of a for loop in the initialization of the priority queue, where n is the number of characters within the inputted string

As for the initialization of the Huffman Tree, each of the elements within the priority queue are accessed, summed, and re-entered into the Priority Queue until there is only 1 element left, resulting in a time complexity of O(n!)

Space Complexity:
Since the initialization process of the priority queue requires the creation of 3 lists(self.heap, self._freq_list & unique_chars_table) which is progressively filled in with a for loop looping through the string, this certain Class Initialization function has a Linear Space Complexity of O(n).

The Huffman Tree is initialized by looping through the priority queue until one remaining element, whilst at the same time constructing a tree with the summation of the first 2 elements within the priority queue, resulting in a n! nodes within the tree. As such, this will result in a overall space complexity of O(n!)


II. Generating the Encoded Data

A recursion is utilized in order to access each of the leaf nodes to get the combination of bits unique for each alphabets

Time Complexity:

The function requires the traversal down each of the nodes from the root node to each respective leaf nodes. As such, the time complexity for the generation of the encoded dictionary is O(2^n) as each nodes (except for leaf nodes) have 2 branches. 

Space Complexity:

A recursive function is deployed to generate the encoded data and as such, our space complexity which is dependant on the number of return statements will be O(n)

III. Decoding the Encoded Data

A For Loop is utilized to run through the entire encoded data one-by-one while simultaneously transitioning down the Huffman Tree created according to the bits in the encoded data

Time Complexity:

For loop is utilizing to run through each bit at a time resulting in an overall time complexity of O(n)

Space Complexity:

As the encoded data are decoded while traversing the strings of bits, it is also concatanated together as a string, resulting in a space complexity of O(n)