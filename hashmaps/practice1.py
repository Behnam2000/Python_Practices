from typing import Any

class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.map: list[tuple[Any, Any] | None] = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._get_hash(key)
        self.map[index] = (key, value)

    def get(self, key):
        index = self._get_hash(key)
        item = self.map[index]

        if item is not None:
            return item[1]
        return None
    
    def delete(self, key: Any):
        index = self._get_hash(key)
        item = self.map[index]

        if item is not None and item[0] == key:
            self.map[index] = None