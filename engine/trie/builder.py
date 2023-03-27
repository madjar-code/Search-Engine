import pickle
from pathlib import Path
from trie import PrefixTree


class TrieBuilder:
    def __init__(self,
                 prefix_tree: PrefixTree = None,
                 source_path: str = '',
                 trie_path: str = '') -> None:
        self.trie: PrefixTree = PrefixTree()
        if prefix_tree:
            self.trie: PrefixTree = prefix_tree
        self.source_path: Path = Path(source_path)
        self.trie_path: Path = Path(trie_path)
        
    def add_words_to_tree(self) -> None:
        with self.source_path.open('r') as source_file:
            raw_content = source_file.readlines()
            word_list = [x.strip() for x in raw_content]

        for word in word_list:
            self.trie.insert(word)

    def save_tree(self) -> None:
        with self.trie_path.open('wb') as trie_file:
            pickle.dump(self.trie, trie_file)


def main() -> None:
    prefix_tree: PrefixTree = PrefixTree()
    builder = TrieBuilder(prefix_tree,
                          'engine/resources/word_list.txt',
                          'engine/resources/trie')
    builder.add_words_to_tree()
    builder.save_tree()

    with open('engine/resources/trie', 'rb') as trie_file:
        trie = pickle.load(trie_file)


if __name__ == '__main__':
    main()