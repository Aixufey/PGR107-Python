"""
    Abstract: We want to map the key or K,V into our table perfectly
    accordingly as first element at index 0, second element at index 1
    But unfortunately this is not the case.

    RELATION: ONE-TO-ONE
    We have to use function to 'hash' the element that will be stored in the table
    hash(x) = x goes into table[i]

    Search: Suppose we want to search for key 2 in table
    hash(2) = 2
    key 2 is not present! return 0 or None

    keys:    T   i
    3      [ 0 ] 0
    0      [ 1 ] 1
    1      [   ] 2
    12     [ 3 ] 3
           [   ] 4
           [   ] 5
            ...
           [ 12 ] 12
    100?
    Drawback of this is waste of memory space, we only have 4 elements, but we need a size of 0 up to 12 with plenty of void in between
    What if we want to store 100 ?

    RELATION: MANY-TO-ONE
    Solution: We maintain the table size but implement a hashing algorithm.
    Logic in hash(x) = x % size of hash table
    e.g. x % 10 (hash table with size of 10)


         T    i
        [100] 0       suppose we want to store 15 in our table
        [] 1          15 % 10 = 5
        [] 2       Okay.. what about 25 ?
        [] 3          26 % 10 = 6
        [] 4       And.. 100?
        [ 15 ] 5     100 % 10 = 0
        [ 26 ] 6
        [] 7       Last try.. What about 25?
        [] 8          25 % 10 = 5
        [] 9       5 is occupied!

    Drawback: Collision of keys => when an index is occupied, how to map?
    Avoiding collision by Open Hashing and Closed Hashing

    Closed Hashing => utilize only the given table size not increasing
        * open addressing = on collisions store the key in any next free space. But where? We have 3 options
            * Linear probing
            * Quadratic probing
            * Double hashing

            Linear probing: h(x) = ( h(x) + f(i) ) % size
            suppose we have 45 and 25 as keys we hash them and get index 5 for both.
            If there is already existing key at 5
            We increment index until next open slot.


            19     [ 30 ] 0
            29     [ 29 ] 1   We can go cyclic for key 29 to store at empty space 1 because index 9 is occupied
            30     [    ] 2
            23     [ 23 ] 3
            26     [ 43 ] 4
            45     [ 25 ] 5
            25     [ 26 ] 6
            74     [ 74 ] 7
            40     [ 19 ] 9   we want to search for key 40, try for every index, if we meet null, then stop the search!

            Quadratic probing is the same as linear probing but storing with a space between probing with square root


            [  ]0    We can put Quadratic probing into test by inserting keys with same number endings.
            [  ]1    Given the keys: 23, 43, 13, 27
            [  ]2    h(x) = (h(x) + f(i)) % 10 where f(i)=i^2
            [23]3      23 => h(23) + f(0) % 10  (0^2 = 0)
            [43]4               3 + 0 % 10 = 3
            [  ]5      43 => h(43) + f(1) % 10 (1^2 = 1)
            [  ]6               3 + 1 % 10 = 4
            [13]7      13 => h(13) + f(4) % 10 (2^2 = 4)
            [27]8               3 + 4 % 10 = 7
            [  ]9      27 => h(27) + f(0) % 10 (0^1 = 0)
                                7 + 0 % 10 = 7  collision at 7
                                7 + 1 % 10 = 8


                  h1(x) = x % 10
                  h2(x) = R - (x % R)   =>    7 - (x % 7)
                  h3(x) = (h1(x) + i * h2(x) ) % 10
            [ ]0   keys: 5, 25, 15, 35, 95
            [15]1
            [35]2   The first key will just be regular hashing because i = 0, 0 * h2(x) = 0, i++ only when occupied!
            [ ]3     5 % 10 = 5
            [95]4     25 % 10 = 5 collision -> h3(5) = (h1(5) + 1 * h2(3)) % 10  = 8
            [5]5                                             7 - (25 % 7) = 3
            [ ]6
            [ ]7     15 % 10 = 5 collision -> h3(15) = (5 + 1 * 6) % 10 = 1
            [25]8                                           7 - (15 % 7) = 6
            [ ]9
                    35 % 10 = 5 collision -> h3(35) = (5 + 1 * 7) % 10 = 2
                                                            7 - (35 % 7) = 7

                    95 % 10 = 5 collosion -> h3(95) = (5 + 1 * 3) % 10 = 8 second collision i++
                                                            7 - (95 % 7) = 3
                                             h3(95) = (5 + 2 * 3) % 10 = 1 third collision i++
                                             h3(95) = (5 + 3 * 3) % 10 = 4

    Open Hashing => increase the table size
        * chaining
            We pass the key into hashing and the given index will initialize a Linked List with K,V and Node pointer
            The Linked List shall be sorted for efficient search!
            In essence, Hash table has a pointer to the Linked List.
              T    i
            [ *p ] 5 -> [15|Node.next]-> [25|Node.next] null

"""


class HashTable:
    # Struct for this class
    def __init__(this, size):
        this.size = size
        this.table = [None] * size

    # Simple hashing algorithm hash(x) = x mod size
    def hash(this, key):
        # Summarize values for each char in key in unicode
        hash_value_unicode = sum(ord(c) for c in key)
        return hash_value_unicode % this.size

    # Setter for k,v pair
    def set(this, key, value):
        hash_key = this.hash(key)
        i = hash_key % this.size

        # while table at given index != null
        while this.table[i] is not None:
            # If existing value equals to input, overwrite
            if this.table[i][0] == key:
                this.table[i] = (key, value)
                return
        this.table[i] = (key, value)

    # Return value
    def get(this, key):
        hash_key = this.hash(key)
        i = hash_key

        while this.table[i] is not None:
            if this.table[i][0] == key:
                # returning the key's value
                return this.table[i][1]
            # Linear probing checking next index
            i = (i + 1) % this.size
        return None

    # Return key
    def search(this, value):
        for item in this.table:
            if item is not None and item[1] == value:
                return item[0]

    # Delete key
    def delete(this, key):
        hash_value = this.hash(key)
        i = hash_value % this.size

        while this.table[i] is not None:
            if this.table[i][0] == key:
                # key assign to None
                this.table[i] = None
                return
            i = (i + 1) % this.size
        raise KeyError("Key not found")
    # Display Hash Table
    def display(this):
        for i in range(this.size):
            print(f"Index {i}: {this.table[i]}")


my_table = HashTable(10)
my_table.set("Windows", "7")
my_table.set("Linux", "Ubuntu")
my_table.set("Mac", "Big Sur")
my_table.delete("Mac")
my_table.display()
