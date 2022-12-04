class Solution:
  def read_bit(self, i):
    l = []
    while i > 0:
      l.append(i%2)
      i = int(i/2)
    result = 0
    count = 0
    r = []
    for bit in enumerate(l):
      bit_digit = bit[0]
      ele = bit[1]
      if bit_digit>=17 and bit_digit<=22:
        if ele == 1:
          result += pow(2,count)
        r.append(ele)
        count += 1
    return result
  
s = Solution()
print(s.read_bit(1024*1024*5))