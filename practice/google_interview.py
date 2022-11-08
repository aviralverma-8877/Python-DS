Blocks = [
    {
        "gym":False,
        "school":True,
        "store":False
    },
    {
        "gym":True,
        "school":False,
        "store":False
    },
    {
        "gym":True,
        "school":True,
        "store":False
    },
    {
        "gym":False,
        "school":True,
        "store":False
    },
    {
        "gym":False,
        "school":True,
        "store":True,
    },    
]

Reqs = ["gym", "school", "store",]

class Solution:
    def find_best_apt(self):
        def_Dist = {}
        for build in Reqs:
            def_Dist[build] = len(Blocks)
        target_block_count = 0
        min_block = -1
        max_dist = len(Blocks)-1

#counting every block
        for target_blk in Blocks:
            Dist = def_Dist.copy()
            comp_blk_count = 0

#comparing with every other block
            for comp_blk in Blocks:
                for build in Reqs:
                    if comp_blk[build]:
                        Dist[build] = min(Dist[build],abs(target_block_count - comp_blk_count))
                comp_blk_count += 1
            m = -1
            for build in Reqs:
                if Dist[build] < len(Blocks):
                    m = max(Dist[build], m)
            if m < max_dist and m != -1:
                min_block = target_block_count
                max_dist = min(max_dist, m)
            target_block_count += 1
        return min_block

class Solution2:
    def find_best_apt(self):
        fac = {}
        for req in Reqs:
            fac[req] = []
        block_number = 0
        for block in Blocks:
            for req in Reqs:
                if block[req]:
                    fac[req].append(block_number)
            block_number += 1
        block_number = 0
        dist = len(Blocks)
        for block in Blocks:
            for d in fac:
                pass
                


s = Solution2()
s.find_best_apt()
print(s.find_best_apt())