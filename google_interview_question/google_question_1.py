# Given 2 lists as inputs first consists of list of charecters
# and second consists of list of words. Return the list of words
# which can be formed with the chars in first list and has 
# max length.
# Hint : Use Trie data structure to achive the result


# My Approach
class Solution1:
    def find_max_length_words(self, char_arr, word_arr):
        word_arr = self.sort_word_arr(word_arr)
        mapper = self.create_mapper(char_arr)
        l = self.get_longest_words(mapper, word_arr)
        return l
    
    def get_longest_words(self, mapper, word_arr):
        l = []
        word_len = 0
        for word in word_arr:
            if word_len == 0 or word_len == len(word):
                word_len = len(word)
            else:
                if len(l) > 0:
                    break
                word_len = len(word)
            m = mapper.copy()
            found = True
            for char in word:
                if char in m:
                    if m[char] > 0:
                        m[char] -= 1
                    else:
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                l.append(word)
        return l
    def create_mapper(self, char_arr):
        mapper = {}
        for char in char_arr:
            if char in mapper:
                mapper[char] += 1
            else:
                mapper[char] = 1
        return mapper

    def sort_word_arr(self, word_arr):
        l = []
        m = 0
        for i in word_arr:
            m = max(m, len(i))
        for i in range(m, 0, -1):
            for word in word_arr:
                if len(word) == i:
                    l.append(word)
        return l



# Trie Data structure approach
class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = {}
        self.in_charr_arr = False
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

############ Work in Progress #################################

class Solution2:
    def __init__(self) -> None:
        self.words = []
    def find_max_length_words(self, char_arr, word_arr):
        trie = self.create_trie_from_words(word_arr, char_arr)
        word = self.find_matching_words_in_trie(trie, word_arr)
        return word

    def find_matching_words_in_trie(self, root, word_arr):
        if len(root.children) == 0:
            return ([],root.isEndOfWord)
        for char in root.children:
            (value,isEndOfWord) = self.find_matching_words_in_trie(root.children[char], word_arr)
            if value != None:
                for i in range(0, len(value)):
                    value[i] = char + value[i] 
                if root.in_charr_arr == True:
                    if isEndOfWord:
                        value.append(char)
        for i in value:
            if i in word_arr:
               self.words.append(i)
        return (value, root.isEndOfWord)
    
    def create_trie_from_words(self, word_arr, char_arr):
        root = TrieNode()
        for word in word_arr:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                if char in char_arr:
                    node.in_charr_arr = True
                node = node.children[char]
            node.isEndOfWord = True
        return root

############ Work in Progress #################################
s = Solution2()
s.find_max_length_words(
    ['a','a','l','p','p','e','b','d','c'],
    ["bad","pineapple","app","appla","apple","cat",]
)
print(s.words)
# should return ['appla','apple']