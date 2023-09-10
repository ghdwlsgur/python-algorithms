#
# class Trie(object):
#     class TrieNode(object):
#         def __init__(self):
#             # 알파벳 개수만큼 빈 배열 생성
#             self.arr = [None] * 26
#             # 해당 노드가 문자열의 끝을 의미하는지 확인
#             self.end = False
#
#     def __init__(self):
#         self.root = self.TrieNode()
#
#     def insert(self, word: str) -> None:
#         """
#         :type word: str
#         :rtype: None
#         """
#         curr = self.root
#         for c in word:
#             idx = ord(c) - ord('a')
#             if curr.arr[idx] is None:
#                 curr.arr[idx] = self.TrieNode()
#             curr = curr.arr[idx]
#         curr.end = True
#
#     def search(self, word: str) -> bool:
#         """
#         :type word: str
#         :rtype: bool
#         """
#         curr = self.root
#         for c in word:
#             idx = ord(c) - ord('a')
#             if curr.arr[idx] is None:
#                 return False
#             curr = curr.arr[idx]
#         return curr.end
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         :type prefix: str
#         :rtype: bool
#         """
#         curr = self.root
#         for c in prefix:
#             idx = ord(c) - ord('a')
#             if curr.arr[idx] is None:
#                 return False
#             curr = curr.arr[idx]
#         return curr.end
#
#     def display(self):
#         def dfs(node, path):
#             if node.end:
#                 print(''.join(path))
#             for i, child in enumerate(node.arr):
#                 if child:
#                     dfs(child, path + [chr(i + ord('a'))])
#
#         dfs(self.root, [])

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.display()
param_2 = obj.search("apple")
print(obj.startsWith('apple'))
# param_3 = obj.startsWith(prefix)