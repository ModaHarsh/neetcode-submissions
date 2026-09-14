class PrefixNode:
    def __init__(self):
        self.children = {}
        self.isEnding = False   ##by default it at False
        ## take care of edge case if no element/never called condition

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixNode()
                curr = curr.children[c]
            else:
                curr = curr.children[c]
        curr.isEnding = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr.isEnding


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

        
    ## so basically every node will have at max 26 children
