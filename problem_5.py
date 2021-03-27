import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(timestamp, data, previous_hash)
        self.next = None

    def calc_hash(self, timestamp, data, previous_hash):
        # initializie hash - sha256
        sha = hashlib.sha256()

        # proceeding to hash the information such as transaction time, data and previous_hash as indicated by problem
        hash_str = ' '.join((str(timestamp), str(data), str(previous_hash))).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

class Blockchain:

    def __init__(self, timestamp, data, previous_hash=0):
        if timestamp is None or data is None:
            print(
"""
Please input valid Timestamp or Data
Note: No Data have been added..
"""
            )
            return

        self.head = Block(timestamp, data, previous_hash) # creation of the genesis block (Block 0)
        self.size = 0

    def append(self, timestamp, data):
        if timestamp is None or data is None:
            print(
"""
Please input valid Timestamp or Data
Note: No Data have been added..
"""
            )
            return

        block = self.head
        while block.next is not None:
            block = block.next

        new_block = Block(timestamp, data, block.get_hash())
        if new_block is None:
            return

        block.next = new_block
        self.size += 1

    def __repr__(self):
        repr_out = []
        block = self.head
        while len(repr_out) <= self.size:
            repr_out.append((block.timestamp, block.data, block.previous_hash, block.hash))
            block = block.next
        return str(repr_out)

if __name__ == "__main__":
    # Test Case 1
    print("-----------------------------------------TEST CASE 1-----------------------------------------")
    null_data = None
    valid_data = "Some_Non_NULL"

    # Testing Initializing Blockchain with NULL Value
    blockchain = Blockchain(str(datetime.datetime.utcnow()), null_data) # returns None

    # Testing Appending Null Value
    blockchain = Blockchain(str(datetime.datetime.utcnow()), valid_data)
    # appending Block 1
    blockchain.append(str(datetime.datetime.utcnow()), null_data)

    print(blockchain) # returns blockchain with valid_data

    # Test Case 2
    print("-----------------------------------------TEST CASE 2-----------------------------------------")
    big_data = "BIG_DATA"

    blockchain = Blockchain(str(datetime.datetime.utcnow()), big_data)

    for idx in range(500):
        blockchain.append(str(datetime.datetime.utcnow()), ' '.join((big_data, str(idx))))

    print(blockchain) # returns Blockchain with 500 blocks
    
    # Test Case 3
    print("-----------------------------------------TEST CASE 3-----------------------------------------")

    data = "Some Information"
    # defining blockchain and initializing with Genesis Block (Block 0)
    blockchain = Blockchain(str(datetime.datetime.utcnow()), data)
    # appending Block 1
    blockchain.append(str(datetime.datetime.utcnow()), ' '.join((data, '1')))
    # appending Block 2
    blockchain.append(str(datetime.datetime.utcnow()), ' '.join((data, '2')))

    print(blockchain)
