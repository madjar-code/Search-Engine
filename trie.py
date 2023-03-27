from typing import List
import networkx as nx


PREFIX_COLOR = 'yellow'
WORD_COLOR = 'blue'
PREFIX_TYPE = 0
WORD_TYPE = 1

TYPE_COLOR = {
    WORD_TYPE: WORD_COLOR,
    PREFIX_TYPE: PREFIX_COLOR
}

class Node:
    """
    Node of the trie data structure.
    """
    
    def __init__(self, text='') -> None:
        self.text = text
        self.children = dict()
        self.is_word = False


class PrefixTree:
    def __init__(self):
        self.root = Node()
        self.visual_graph = nx.DiGraph()
        self.nodes = [self.root,]
    
    def insert(self, word: str) -> None:
        current = self.root
        
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[: i+1]
                new_node = Node(prefix)
                current.children[char] = new_node
                self.nodes.append(new_node)
            current = current.children[char]
        current.is_word = True

    def find(self, word: str) -> Node:
        current = self.root
        
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current if current.is_word else None

    def starts_with(self, prefix: str) -> List[str]:
        words = list()
        current = self.root
        
        for i, char in enumerate(prefix):
            if char not in current.children:
                return list()
            current = current.children[char]
        
        self.__child_words_for(current, words)
        return words
    
    def __child_words_for(self, node, words) -> None:
        if node.is_word:
            words.append(node.text)

        for letter in node.children:
            return self.__child_words_for(node.children[letter], words)


def main():
    main_tree = PrefixTree()


if __name__ == '__main__':
    main()