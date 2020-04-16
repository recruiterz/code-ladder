class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_str = ''
        min_length = float("inf") 
        for str in strs:
            if len(str) < min_length:
                min_str = str
                min_length = len(str)
        
        
        for i, s in enumerate(min_str):
            
            for str in strs:
                if s != str[i]:
                    return min_str[:i]
        
        return min_str
    
###############################################################################
## solve with trie
##########

class TrieNode:

    def __init__(self, key=None):
        self.children = dict()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
        
        root = TrieNode()
        first_word = min(strs, key=len)
        
        node = root
        for s in first_word:
            node.children[s] = TrieNode()
            node = node.children[s]
            
        prefix = ''
        for word in strs:
            
            node = root
            for i, s in enumerate(word):
                
                if s in node.children:
                    node = node.children[s]
                else:
                    node.children = {}
                    break
        
        if not root.children:
            return ''
        
        prefix = ''
        node = root
        while node.children:
            prefix += list(node.children.keys())[0]
            node = list(node.children.values())[0]
            
        return prefix

