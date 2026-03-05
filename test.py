from heap import heap_object

heap = heap_object()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(4)
print(heap.get_list())
print(heap.pop_out())
print(heap.get_list())