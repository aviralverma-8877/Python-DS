import dll

l = dll.Stacked_list()
# l.insert(dll.Node(1))
# l.insert(dll.Node(2))
# l.insert(dll.Node(3))
# l.insert(dll.Node(4))
# l.insert(dll.Node(5))
# l.insert(dll.Node(6))
# l.insert(dll.Node(7))

l.insert(dll.Node(1), 0)
l.insert(dll.Node(2), 1)
l.insert(dll.Node(3), 2)
l.insert(dll.Node(4), 3)
l.insert(dll.Node(5), 4)
l.insert(dll.Node(6), 5)
l.insert(dll.Node(7), 6)

l.display()

l.reverse()

l.display()