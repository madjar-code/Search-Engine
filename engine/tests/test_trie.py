import unittest
from unittest import TestCase
from engine.trie.trie import PrefixTree


class TrieTest(TestCase):
    def setUp(self) -> None:
        self.trie: PrefixTree = PrefixTree()

    def test_prefix_not_found_as_whole_word(self) -> None:
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.assertEqual(self.trie.find('app'), None)
        
    def test_prefix_is_also_whole_word(self) -> None:
        word_list: tuple = (
            'apple',
            'appreciate',
            'app',
        )
        for word in word_list:
            self.trie.insert(word)

        self.assertEqual(self.trie.find('app').is_word, True)

    def test_starts_with(self) -> None:
        word_list: tuple = (
            'apple',
            'appreciate',
            'aposematic',
            'apoplectic',
            'appendix',
        )
        for word in word_list:
            self.trie.insert(word)

        self.assertEqual(self.trie.starts_with('app'),
                         ['apple', 'appreciate', 'appendix'])

    def test_starts_with_self(self) -> None:
        self.trie.insert('app')
        self.assertEqual(self.trie.starts_with('app'), ['app'])

    def test_starts_with_empty_and_no_words(self) -> None:
        self.assertEqual(self.trie.starts_with(''), [])

    def test_starts_with_empty_returns_all_words(self) -> None:
        word_list = (
            'bad',
            'bat',
            'cat',
            'cage',
        )
        self.assertEqual(self.trie.starts_with(''), list(word_list))

if __name__ == '__main__':
    unittest.main()