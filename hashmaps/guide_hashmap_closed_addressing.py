# 'Any' is imported so we can type-hint keys and values as "any type",
# since a hashmap shouldn't care whether you store strings, ints, objects, etc.
from typing import Any


class SimpleHashMap:

    def __init__(self, size: int = 10):
        # 'size' controls how many buckets (slots) the hashmap has.
        # More buckets = fewer collisions, but more memory usage.
        # 10 is just a small default for demonstration purposes.
        self.size: int = size

        self.count: int = 0  # Tracks the total number of items in the hashmap

        # The internal storage is a flat list of fixed length.
        # Each slot (bucket) starts as None, meaning "empty".
        # When occupied, a slot holds a (key, value) tuple.
        # So the type of each element is either a tuple or None.

        # self.map: list[tuple[Any, Any] | None] = [None] * self.size

        # Separate Chaining: Each index in self.map now holds a list of tuples.
        # This prevents Pylance type errors and handles collisions seamlessly.
        self.map: list[list[tuple[Any, Any]]] = [[] for _ in range(self.size)]
        


    def _get_hash(self, key: Any) -> int:
        # This is the heart of any hashmap: the hash function.
        # Step 1 — hash(key): Python converts the key into a large integer
        #          (e.g., hash("name") might return 3713082716806266542).
        # Step 2 — % self.size: We clamp that integer into a valid list index
        #          in the range [0, size-1], so it always points to a real bucket.
        # ⚠️  Limitation: different keys can produce the same index — this is called
        #     a "collision". This simple implementation does NOT handle collisions;
        #     storing a new key at a colliding index will silently overwrite the old one.
        return hash(key) % self.size
    
    def _resize(self) -> None:
        """Doubles the capacity of the table and rehashes all existing keys."""
        old_map = self.map
        self.size *= 2
        # Initialize a new larger list of empty lists
        self.map = [[] for _ in range(self.size)]
        self.count = 0  # Reset count; put() will rebuild it during rehashing
        
        # Loop through every bucket, and rehash every item in each bucket
        for bucket in old_map:
            for key, value in bucket:
                self.put(key, value)


    def put(self, key: Any, value: Any) -> None:
        # Step 1 — Compute which bucket this key belongs to.
        index = self._get_hash(key)
        bucket = self.map[index]

        # Check if the key already exists in this bucket to update its value
        for i, item in enumerate(bucket):
            if item[0] == key:  
                bucket[i] = (key, value)
                return
            
        # If it's a completely new key, append it to the bucket list
        bucket.append((key, value))
        self.count += 1

         # Check load factor and resize if needed
        if self.count / self.size >= 0.7:
            self._resize()


        # Step 2 — Store the (key, value) pair as a tuple in that bucket.
        #          We keep the key alongside the value so we can verify it later
        #          (important for collision-safe lookups in more advanced implementations).
        # self.map[index] = (key, value)


    def get(self, key: Any) -> Any:
        # Step 1 — Find the bucket index for this key.
        index = self._get_hash(key)
        bucket = self.map[index]
                          
        # Search the bucket list for the matching key
        for item in bucket:
            if item[0] == key:
                return item[1]
            
        return None

        # # Step 2 — Read whatever is currently sitting in that bucket.
        # item = self.map[index]

        # # Step 3 — If the bucket is not empty, return the value (index [1] of the tuple).
        # #          We skip re-checking the key here because this simple implementation
        # #          assumes no collisions. A production hashmap would verify item[0] == key.
        # if item is not None:
        #     return item[1]   # item = (key, value), so item[1] is the value

        # # Step 4 — The bucket was empty, meaning the key was never stored.
        # return None


    def delete(self, key: Any) -> bool:
        # Step 1 — Locate the bucket for this key.
        index = self._get_hash(key)
        bucket = self.map[index]
        
        # Search for the key in the bucket and remove it
        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False
            
        # # Step 2 — Read the current occupant of that bucket.
        # item = self.map[index]

        # # Step 3 — Only delete if:
        # #          a) the bucket is actually occupied (item is not None), AND
        # #          b) the stored key matches what we want to delete (item[0] == key).
        # #          Checking the key prevents accidentally deleting a different key
        # #          that happened to hash to the same bucket (a collision scenario).
        # if item is not None and item[0] == key:
        #     self.map[index] = None   # Reset the bucket back to "empty"


    def contains(self, key: Any) -> bool:
        # Step 1 — Compute the bucket index for the key.
        index = self._get_hash(key)
        bucket = self.map[index]
        
        for item in bucket:
            if item[0] == key:
                return True
        return False

        # # Step 2 — Peek at what's in the bucket.
        # item = self.map[index]

        # # Step 3 — Return True only if:
        # #          a) the bucket is not empty, AND
        # #          b) the key stored there is exactly the one we're looking for.
        # #          Both conditions use Python's short-circuit evaluation:
        # #          if 'item is None', the second check is never even executed.
        # return item is not None and item[0] == key