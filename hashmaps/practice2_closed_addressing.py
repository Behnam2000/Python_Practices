from typing import Any

class HashMap:
    def __init__(self, size: int = 10):
        self.size = size
        self.count = int = 0
        self.map: list[list[tuple[Any, Any]]] = [[] for _ in range(self.size)]

    def _get_hash(self, key: Any)-> int:
        return hash(key) % self.size
    
    def _resize(self)-> None:
        old_map = self.map
        self.size *= 2
        self.map = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_map:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key: Any, value: Any)-> None:
        index = self._get_hash(key)
        bucket = self.map[index]

        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value))
        self.count += 1

        if self.count / self.size >= 0.7:
            self._resize()

    def get(self, key: Any) -> Any:
        index = self._get_hash(key)
        bucket = self.map[index]

        for i, item in enumerate(bucket):
            if item[0] == key:
                return item[1]
            
        return None
    
    def delete(self, key: Any)-> None:
        index = self._get_hash(key)
        bucket = self.map[index]

        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket.pop(i)
                self.count -= 1
                return

    def contains(self, key: Any) -> bool:
        index = self._get_hash(key)
        bucket = self.map[index]
        
        for item in bucket:
            if item[0] == key:
                return True
        return False
    
    def display(self) -> list[list[tuple[Any, Any]]]:
        return self.map
    

myHash = HashMap()

myHash.put('Behnam', 8000)
myHash.put('Amir', 6000)
myHash.put('Ali', 7000)
myHash.put('Alireza', 10000)
myHash.put('Bahar', 5000)
myHash.put('Behzad', 3000)
myHash.put('Akram', 4000)

print(myHash.display())

myHash.delete('Alireza')
print(myHash.contains('Alireza'))
print(myHash.get('Bahar'))
print(myHash.contains('Behnam'))




            
        