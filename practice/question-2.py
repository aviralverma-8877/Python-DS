#https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/
class Solution:
    def generate_binary_string(self,s):
        # Code here
        self._print(list(s), 0)
        
    def _print(self, s, index):
        if index ==len(s):
            print("".join(s))
            return
        if s[index] == '?':
            
            s[index] = '0'
            self._print(s, index+1)
            
            s[index] = '1'
            self._print(s, index+1)

            s[index] = '?'
        else:
            self._print(s, index+1)

s=Solution()
s.generate_binary_string("1??0?101")