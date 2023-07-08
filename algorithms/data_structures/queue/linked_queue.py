
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedQueue:
    def __init__(self) -> None:
        self.front: Node = None
        self.rear: Node = None

    def __iter__(self):
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __str__(self) -> str:
        return " <- ".join(str(item) for item in self)

    def is_empty(self) -> bool:
