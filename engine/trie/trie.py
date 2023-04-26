from typing import (
    List,
    Dict,
    TypeAlias,
    Optional
)


# PREFIX_COLOR = 'yellow'
# WORD_COLOR = 'blue'
# PREFIX_TYPE = 0
# WORD_TYPE = 1

# TYPE_COLOR = {
#     WORD_TYPE: WORD_COLOR,
#     PREFIX_TYPE: PREFIX_COLOR
# }


CharType: TypeAlias = str

class Node:
    """
    Node of the trie data structure.
    """
    
    def __init__(self, text='') -> None:
        self.text: str = text
        self.children: Dict[CharType, Node] = {}
        self.is_word: bool = False


class PrefixTree:
    def __init__(self):
        self.root: Node = Node()
        self.nodes: List[Node] = [self.root,]
    
    def insert(self, word: str) -> None:
        current: Node = self.root
        
        for i, char in enumerate(word):
            if char not in current.children:
                prefix: str = word[:i+1]
                new_node = Node(prefix)
                self.nodes.append(new_node)
                current.children[char] = new_node
            current: Node = current.children[char]
        current.is_word = True

    def find(self, word: str) -> Optional[Node]:
        current: Node = self.root

        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current if current.is_word else None

    def starts_with(self, prefix: str) -> List[str]:
        words = List[str]
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]
        
        self.__child_words_for(current, words)
        return words
    
    def __child_words_for(self, node: Node,
                          words: List[str]) -> None:
        if node.is_word:
            words.append(node.text)

        for letter in node.children:
            return self.__child_words_for(node.children[letter], words)

    def __str__(self) -> str:
        result: str = ''

        for node in self.nodes:
            result += f'{node.text}\n'
            if len(result) >= 100:
                break

        return result
