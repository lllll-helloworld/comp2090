from heap import heap_object
from Pearson_Correlation_Coefficient import PCC
from k_top_calculator import calculator
heap = heap_object()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(4)
print(heap.get_list())
print(heap.pop_out())
print(heap.get_list())
pcc = PCC()
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
result = pcc.calculate(x, y)
print(result)
