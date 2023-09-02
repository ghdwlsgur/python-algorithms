class HashTable:
    def __init__(self, size: int):
        self.nodes = {i: None for i in range(size)}
        self.size = size

    def hash(self, key: str) -> int:
        tot = 0
        for word in key:
            tot += ord(word)

        index = tot % self.size
        if index >= self.size:
            raise ValueError("Hash Table Is Full")
        return index

    def put(self, key: str, value: int):
        curr_node = self.hash(key)
        if self.nodes[curr_node] is None:
            self.nodes[curr_node] = (key, value)
            return

        i = 1
        next_node = (curr_node + i) % self.size
        while self.nodes[next_node] is not None:
            next_node = (next_node + i) % self.size
            i += 1
            if i >= self.size:
                raise ValueError("Hash Table Is Full")
        self.nodes[next_node] = (key, value)

    def get(self, key: str) -> int:
        curr_node = self.hash(key)
        if self.nodes[curr_node] is not None and self.nodes[curr_node][0] is key:
            return self.nodes[curr_node][1]

        i = 1
        next_node = (curr_node + i) % self.size
        while self.nodes[next_node] is not None:
            if self.nodes[next_node][0] == key:
                return self.nodes[next_node][1]
            next_node = (next_node + i) % self.size
            i += 1
            if i > self.size:
                return None


hash_table = HashTable(5)
test_case = ["강호동", "신짱구", "친구", "와우", "아나나"]
for idx, test in enumerate(test_case):
    hash_table.put(test, idx)

for test in test_case:
    print(hash_table.get(test), end=" ")

# print(hash_table.get("아나나"))
# print(hash_table.get("와우"))
# print(hash_table.get("신짱구"))
# print(hash_table.get("강호동"))
# print(hash_table.get("해"))
