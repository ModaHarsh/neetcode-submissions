class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnding = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            else: curr = curr.children[c]
        curr.isEnding = True

    def search(self, word: str) -> bool:
        curr = self.root    

        def dfs(i, curr):
            if i == len(word) - 1:
                
                if word[i] == ".":
                    for v in curr.children.values():
                        if v.isEnding:
                            return True
                    return False

                if word[i] in curr.children:
                    
                    curr = curr.children[word[i]]
                    if curr.isEnding:
                        return True
                    return False
                
                else: return False
            
            if word[i] == ".":
                for k,v in curr.children.items():
                    curr = v
                    if dfs(i + 1, curr):
                        return True
            
            if word[i] not in curr.children:
                return False
            
            return dfs(i + 1, curr.children[word[i]])
        
        res = dfs(0, curr)
        return res