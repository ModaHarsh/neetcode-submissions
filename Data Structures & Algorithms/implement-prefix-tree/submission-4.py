class PrefixTree:
    
    def __init__(self):
        self.words = set()
        self.prefixes = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(1, len(word) + 1):
            self.prefixes.add(word[0:i])

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        else: 
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes:
            return True
        else:
            return False
    
    ## what about using a set
    ## and for every inserted word
    ## insert all possible prefixes of it

    ## just have two sets one with prefixes 
    ## other with the exact words aswell