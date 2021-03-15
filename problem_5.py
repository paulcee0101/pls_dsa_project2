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
        self.head = Block(timestamp, data, previous_hash) # creation of the genesis block (Block 0)
        self.size = 0

    def append(self, timestamp, data):
        block = self.head
        while block.next is not None:
            block = block.next
        new_block = Block(timestamp, data, block.get_hash())
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
    data = "Some Information"
    # defining blockchain and initializing with Genesis Block (Block 0)
    blockchain = Blockchain(str(datetime.datetime.utcnow()), data)
    # appending Block 1
    blockchain.append(str(datetime.datetime.utcnow()), ' '.join((data, '1')))
    # appending Block 2
    blockchain.append(str(datetime.datetime.utcnow()), ' '.join((data, '2')))

    print(blockchain)
