class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # make a Linked List Node by adding a next node
        self.next = None
        # add a head node to add to head
        self.head = None

    # Insert the node into the head of the linked list
    def insert_head(self, node):
        # set new nodes next to self.head
        node.next = self.head
        # change the self.head to the new node
        self.head = node
    
    # Search for the node in the linked list
    def search(self, target):
        # set curren node to the head to start searching from the beginning
        cur_node = self.head
        # keep searching till the end of the list
        while cur_node is not None:
            # if the  value is the target, return noce
            if cur_node.value == target:
                return cur_node
            # else set current node to the next
            cur_node = cur_node.next
        # if you dont find it in the LL, return none
        return None

    def delete_node(self, target):
        # set current node to the head to start looking for the target
        cur_node = self.head
        # if the value of the current node is the target
        if cur_node.value == target:
            # set head to its next property
            self.head = self.head.next
            # return the current node
            return cur_node
        # set previous node to current node
        prev_node = cur_node
        # set current node to the next node
        cur_node = cur_node.next
        # loop through the list until the end
        while cur_node is not None:
            # if the current node is the target
            if cur_node.value == target:
                # set the prev node to the next node
                prev_node.next = cur_node.next
                # return the current node
                return cur_node
            else:
                # set previous node to the previous node next
                prev_node = prev_node.next
                # set the current node to the next node
                cur_node = cur_node.next
        # if it doesn't exist, print none
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        k = self.get_num_slots()
        n = self.count
        return n / k

    def fnv1(self, key, seed = 0):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        
        # Your code here
        fnvprime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis + seed
        for char in key:
            hash = hash * fnvprime
            hash = hash ^ ord(char)
        return hash




    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
            # hash &= 0xffffffff
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def get_index(self, key):
        key_index = self.fnv1(key)
        return key_index % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        key_index = self.get_index(key)
        cur_node = self.storage[key_index]
        done = False
        
        if cur_node == None:
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
            self.storage[key_index] = HashTableEntry(key, value)
            done = True
            self.count += 1

        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value
                done = True
                return
            cur_node = cur_node.next

        if done == False:
            self.storage[key_index].insert_head(HashTableEntry(key, value))
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None)
        self.count -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        key_index = self.get_index(key)
        cur_node = self.storage[key_index]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        bigHashTable = HashTable(new_capacity)
        for i in self.storage:
            if i is not None:
                bigHashTable.put(i.key, i.value)
        
        self.storage = bigHashTable.storage



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


{
    Hashed_index: [HashTableEntry(key, value)],
    Hashed_index: [HashTableEntry(key, value), HashTableEntry(key, value) ],
    Hashed_index: [HashTableEntry(key, value)],
    Hashed_index: [HashTableEntry(key, value)],
}