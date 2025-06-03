class TreeNode:
    def __init__(self):
        self.childrend={}
        self.isEndNode=False
class Trie:

    def __init__(self):
        self.root= TreeNode()
        

    def insert(self, word: str) -> None:
        node= self.root
        for ch in word:
            if ch not in node.childrend:
                node.childrend[ch]=TreeNode()
            node = node.childrend[ch]
        node.isEndNode=True


    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node.childrend:
                return False
            node=node.childrend[ch]
        return node.isEndNode

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if ch not in node.childrend:
                return False
            node=node.childrend[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)