# custom_structures.py
import heapq

class OrderPriorityQueue:
    def __init__(self):
        self._heap = []
    def is_empty(self):
        return len(self._heap) == 0
    def push_order(self, order):
        heapq.heappush(self._heap, order)
        print(f"系统: 订单 {order.order_ID} 已加入队列。")
    def pop_order(self):
        """
        时间复杂度: O(log N)
        """
        if self.is_empty():
            return None
        return heapq.heappop(self._heap)
    
    def peek_order(self):
        """查看下一个要做的订单"""
        if self.is_empty():
            return None
        return self._heap[0]
        
    def size(self):
        return len(self._heap)