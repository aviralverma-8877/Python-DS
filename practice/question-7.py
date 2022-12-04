class Solution:
    def frequencySort(self, s: str) -> str:
        mapper = self.create_mapper(s)
        s = self.sort_mapper(mapper)
        return s
    def sort_mapper(self, mapper):
        m = 0
        char = ''
        s = ''
        for i in range(0, len(mapper)):
            for j in mapper:
                if m < mapper[j]:
                    m = mapper[j]
                    char = j
            del mapper[char]
            for k in range(0, m):
                s += char
        return k
    def create_mapper(self, s):
        mapper = {}
        for char in s:
            if char not in mapper:
                mapper[char] = 1
            else:
                mapper[char] += 1
        return mapper

s = Solution()
s.frequencySort('tree')