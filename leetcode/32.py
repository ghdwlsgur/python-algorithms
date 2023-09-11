
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            return False
        return dfs(self.root, 0)

obj = WordDictionary()
obj.addWord("word")
print(obj.search("word"))