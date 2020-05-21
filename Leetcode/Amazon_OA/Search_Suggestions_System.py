# https://leetcode.com/problems/search-suggestions-system/
"""
Discription of question in above link
"""
from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # Use a dict to construct trie
        self.trie = {}
        for product in products:
            self.insert(product)
        
        # Searching
        type_in_result = []
        node = self.trie
        self.result = []
        for i in range(len(searchWord)):
            self.search_prefix(node, searchWord[:i + 1])
            type_in_result.append(self.result)
            
        return type_in_result

    def insert(self, word):
        """
        Insert product into trie
        """
        node = self.trie
        for letter in word:
            node = node.setdefault(letter, {})
        node['END'] = node.setdefault('END', {})
    
    def search_prefix(self, node, prefix):
        """
        Find if prefix exsits in trie, then collect three lexicographically minimums products
        """
        # Keep valid previous searched result
        self.result = [word for word in self.result if word.startswith(prefix)]
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else: 
                return
        self.dfs(node, prefix)
        
    def dfs(self, node, prefix):
        # Sorts on nodes so that DFS can start lexicographically
        next_nodes = []
        for next_node in node:
            if next_node == 'END' and prefix not in self.result:
                self.result.append(prefix)
            else:
                next_nodes.append(next_node)
        next_nodes.sort()
        
        for next_node in next_nodes:
            if len(self.result) < 3:
                self.dfs(node[next_node], prefix + next_node)
            else: break

def main():
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    sol = Solution()
    print(sol.suggestedProducts(products, searchWord))


if __name__ == "__main__":
    main()
