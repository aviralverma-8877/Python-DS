import linklist

l = linklist.StackedList()
l.add_node_sorted(12)
l.add_node_sorted(5)
l.add_node_sorted(6)
l.add_node_sorted(10)
l.add_node_sorted(12)
l.add_node_sorted(5)
l.add_node_sorted(6)
l.add_node_sorted(10)
l.add_node_sorted(12)
l.add_node_sorted(5)
l.add_node_sorted(6)
l.add_node_sorted(10)

l.list_print()
l.list_reverse()
l.list_print()
l.list_reverse_rec(None,l.head)
l.list_print()
# print(l.list_count())
# print(l.list_count_rec(l.head))

# l.delete_node(2)

# l.list_print()

# l.list_print_rec(l.head)

print("")
# print(l.list_count())
# print(l.list_count_rec(l.head))