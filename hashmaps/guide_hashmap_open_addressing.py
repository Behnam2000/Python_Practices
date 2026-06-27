from typing import Any

class HashMap:
    def __init__(self, size: int = 10):
        self.size: int = size
        self.count: int = 0
        
        # Flat list: each slot is either None or holds exactly one (key, value) tuple.
        self.map: list[tuple[Any, Any] | None] = [None] * self.size
        
        # A special "Tombstone" marker to safely handle deletions without breaking search chains.
        self._TOMBSTONE: tuple[Any, Any] = ("__TOMBSTONE__", None)

    def _get_hash(self, key: Any) -> int:
        return hash(key) % self.size
    
    def _resize(self) -> None:
        """Doubles the capacity of the table and rehashes all active keys, cleaning up tombstones."""
        old_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        self.count = 0  # Rebuild count during rehashing

        for item in old_map:
            # Rehash only active elements (skip empty slots and tombstones)
            if item is not None and item != self._TOMBSTONE:
                self.put(item[0], item[1])

    def put(self, key: Any, value: Any) -> None:
        # Prevent using our internal tombstone string as a key
        if key == "__TOMBSTONE__":
            raise ValueError("Reserved key name")

        # Check load factor first. Open Addressing degrades severely if load factor >= 0.7
        if (self.count + 1) / self.size >= 0.7:
            self._resize()

        index = self._get_hash(key)
        first_deleted_idx = -1

        # Probe up to self.size times to avoid an infinite loop in a full table
        for _ in range(self.size):
            item = self.map[index]

            if item is None:
                # Found an empty slot! If we encountered a tombstone earlier, reuse it.
                insert_idx = first_deleted_idx if first_deleted_idx != -1 else index
                self.map[insert_idx] = (key, value)
                self.count += 1
                return

            if item == self._TOMBSTONE:
                # Remember this index to reuse it if we don't find our key later in the chain
                if first_deleted_idx == -1:
                    first_deleted_idx = index
            elif item[0] == key:
                # Key already exists: overwrite the value
                self.map[index] = (key, value)
                return

            # Linear Probing step: move to the next index, wrapping around
            index = (index + 1) % self.size

    def get(self, key: Any) -> Any:
        index = self._get_hash(key)

        for _ in range(self.size):
            item = self.map[index]

            if item is None:
                return None  # Hit an empty slot; key definitely isn't in the table

            # Ignore tombstones and check if the keys match
            if item != self._TOMBSTONE and item[0] == key:
                return item[1]

            index = (index + 1) % self.size

        return None
    
    def delete(self, key: Any) -> bool:
        index = self._get_hash(key)

        for _ in range(self.size):
            item = self.map[index]

            if item is None:
                return False  # Key not found

            # If the key matches, mark it with a tombstone and decrement count
            if item != self._TOMBSTONE and item[0] == key:
                self.map[index] = self._TOMBSTONE
                self.count -= 1
                return True

            index = (index + 1) % self.size

        return False

    def contains(self, key: Any) -> bool:
        index = self._get_hash(key)

        for _ in range(self.size):
            item = self.map[index]

            if item is None:
                return False

            if item != self._TOMBSTONE and item[0] == key:
                return True

            index = (index + 1) % self.size

        return False
    
    def display(self) -> list[tuple[Any, Any] | None]:
        return self.map
    

# --- Test Cases ---
myHash = HashMap()

myHash.put('Behnam', 8000)
myHash.put('Amir', 6000)
myHash.put('Ali', 7000)
myHash.put('Alireza', 10000)
myHash.put('Bahar', 5000)
myHash.put('Behzad', 3000)
myHash.put('Akram', 4000)

print("Initial Map (Notice how elements are spread linearly):")
print(myHash.display())

print("\nOperations:")
print(f"Delete 'Alireza': {myHash.delete('Alireza')}")
# This will show a '__TOMBSTONE__' in Alireza's old slot if printed!
print("Map after deletion:")
print(myHash.display())

print(f"\nContains 'Alireza'? (Should skip tombstone and return False): {myHash.contains('Alireza')}")
print(f"Get 'Bahar': {myHash.get('Bahar')}")
print(f"Contains 'Behnam'?: {myHash.contains('Behnam')}")