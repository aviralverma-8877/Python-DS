edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

class Solution:
    def generate_adjency_list(self, edges):
        adjency_list = {}
        for edge in edges:
            src = edge[0]
            des = edge[1]
            if src in adjency_list:
                adjency_list[src].append(des)
            else:
                adjency_list[src] = [des]
            if des not in adjency_list:
                adjency_list[des] = []
        return adjency_list

    def count_components(self, adjency_list):
        visited = []
        def explore_size(node, adjency_list):
            if node in visited:
                return 0
            size = 1
            visited.append(node)
            for neighbour in adjency_list[node]:
                size += explore_size(neighbour, adjency_list)
            return size
        max_size = 0
        for node in adjency_list:
            max_size = max(max_size, explore_size(node, adjency_list))
        return max_size
s = Solution()
adjency_list = s.generate_adjency_list(edges)
print(s.count_components(adjency_list))