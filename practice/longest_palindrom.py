# https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution:
    def __init__(self):
        self.dynamic = {}
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1:
            return s
        st = ""
        max_len = 0
        for i in range(0, len(s)):
            k = 0
            for j in range(i,len(s)):
                if(k==0):
                    r = s[i:]
                else:
                    r = s[i:k]
                if(len(r)>0):
                    if self.is_palindrom(r):
                        if max_len < len(r):
                            max_len = len(r)
                            st = r
                else:
                    break
                k -= 1
        return st
                
    
    def is_palindrom(self, s):
        if len(s) == 1:
            return True
        if list(s)[0] == list(s)[-1]:
            if len(s) == 2:
                return True
            else:
                if s[1:-1] not in self.dynamic:
                    self.dynamic[s[1:-1]] = self.is_palindrom(s[1:-1])
                return True and self.dynamic[s[1:-1]]
        return False

s = Solution()
print(s.longestPalindrome("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"))