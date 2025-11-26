class TrieNode:
    def __init__(self):
        self.children = {}      
        self.is_end_of_word = False 
        
class Trie:
    def __init__(self):
        self.root = TrieNode() 
        
    def insert(self, word):
        node = self.root  
        for char in word:  
            if char not in node.children:  
                node.children[char] = TrieNode()  
            node = node.children[char]  

        node.is_end_of_word = True  

    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:  
                return False
            node = node.children[char] 

        return node.is_end_of_word  

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:  
            if char not in node.children:
                return []  
            node = node.children[char]

        result = []
        self._collect_words(node, prefix, result)
        return result

    def _collect_words(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)

        for char, next_node in node.children.items():
            self._collect_words(next_node, prefix + char, result)

trie = Trie()
trie.insert("car")
trie.insert("cat")
trie.insert("care")
trie.insert("dog")

print(trie.search("car"))    
print(trie.search("car"))    
print(trie.starts_with("ca")) 

print(trie.starts_with("d"))
