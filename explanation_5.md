For this problem, a linked list (made out of individual nodes named as Block in the solution) was utilized in order to create the blockchain object, where the reference to consequetive blocks are incorporated in each node/block.

A hash is also calculated by using the unique combination of the timestamp, data and previous hash for a certain block. This was done in order to retrieve a unique hash for each block

In terms of time complexity:
Overall solution has a time complexity of O(n) due to the "append" method in the class "Blockchain" as it loops through each of the blocks within a "Blockchain" object until it reaches the end

In terms of space complexity:
The space complexity of this solution is regarded as linear O(n) as the increase in space complexity increases linearly with increasing input size. This is the case as blocks are created and inputted into the "Blockchain" object