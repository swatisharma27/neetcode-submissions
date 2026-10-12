# class PrefixTree:
#     class TrieNode:
#         def __init__(self):
#             self.isEndFlag = False
#             self.children = [None] * 26

#     def __init__(self):
#         self.root = self.TrieNode()
        
#     def insert(self, word: str) -> None:
#         curr = self.root
#         for ch in word:
#             index = ord(ch) - ord('a')
#             if curr.children[index] is None:
#                 curr.children[index] = self.TrieNode()
#             curr = curr.children[index]
#         curr.isEndFlag = True

#     def search(self, word: str) -> bool:
#         curr = self.root
#         for ch in word:
#             index = ord(ch) - ord('a')
#             if curr.children[index] is None:
#                 return False
#             curr = curr.children[index]
#         return curr.isEndFlag
    
#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root
#         for ch in prefix:
#             index = ord(ch) - ord('a')
#             if curr.children[index] is None:
#                 return False
#             curr = curr.children[index]
#         return True
        


class TrieNode:
    def __init__(self):
        self.endFlag = False
        self.children = [None] * 26


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] is None:
               curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endFlag = True

    def search(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.endFlag

    def startsWith(self, prefix):

        curr = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
























        