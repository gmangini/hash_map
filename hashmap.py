"""
Hashmap ADT

"""

class HashMap:
    '''creates a Hashmap using list'''
    INITIAL = 8

    def __init__(self):
        self.bucket = [None] * HashMap.INITIAL
        self.bucket_size = 0

    def _gethash(self, key):
        '''returns hash value for word'''
        hashval = 64
        for letter in key:
            hashval += abs(hash(letter))
        return hashval

    def get(self, key, default=None):
        '''return value for key if key is in dictionary, else default.'''
        bucket_capacity = self.capacity()
        hashval = self._gethash(key)
        index = hashval % bucket_capacity

        for i in range(bucket_capacity):
            if self.bucket[index] is None:
                return default
            if self.bucket[index][0] == key:
                return self.bucket[index][1]
            index += 1
            if index >= len(self.bucket):
                index = 0

    def set(self, key, value):
        '''add the (key,value) pair to the hashMap'''
        bucket_capacity = self.capacity()
        hashval = self._gethash(key)
        index = hashval % bucket_capacity

        for i in range(bucket_capacity):
            if self.bucket[index] is None:
                self.bucket[index] = (key, value)
                self.bucket_size += 1
                load_factor = self.bucket_size / len(self.bucket)
                if load_factor >= 0.80:
                    self.rehash()
                return
            if self.bucket[index][0] == key:
                self.bucket[index] = (key, value)
                return
            index += 1
            index %= len(self.bucket)

    def clear(self):
        '''empty HashMap'''
        self.bucket = 0

    def capacity(self):
        '''return current capacity--number of buckets--in map.'''
        return len(self.bucket)

    def size(self):
        '''return number of key value pairs in HashMap'''
        return self.bucket_size

    def rehash(self):
        '''rebuild the table to reduce the load factor.'''
        prev_bucket = self.bucket
        self.clear()
        self.bucket = [None] * len(prev_bucket) * 2
        self.bucket_size = 0
        for i in range(len(prev_bucket)):
            if prev_bucket[i] is not None:
                key, value = prev_bucket[i][0], prev_bucket[i][1]
                self.set(key, value)

    def keys(self):
        '''returns a list with keys'''
        keys = []
        for i in range(len(self.bucket)):
            if self.bucket[i] is not None:
                if self.bucket[i][0] not in keys:
                    keys.append(self.bucket[i][0])
        return keys
