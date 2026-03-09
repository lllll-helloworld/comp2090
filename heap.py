class heapk():
    def __init__(self):
        self.heap = []
    def left(self,i):
        pass
    def right(self,i):
        pass
    def parent(self,i):
        pass  
    def insert(self,data):
        pass
    def sift_up(self):
        pass
    def sift_down(self):
        pass
    def pop_out(self):
        pass




class heap_object(heapk):
    def __init__(self):
        self._heap = []
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def insert(self,data):
        self._heap.append(data)
        self.sift_up()
    def sift_up(self):
        i = len(self._heap)-1
        while True:
            if i == 0:
                break
            if self._heap[self.parent(i)] >= self._heap[i]:
                self._heap[i],self._heap[self.parent(i)] = self._heap[self.parent(i)],self._heap[i]
                i = self.parent(i)
            else:
                break

    def sift_down(self):
        n = len(self._heap)-1
        self._heap[0] = self._heap[n]
        self._heap.pop()
        i = 0
        while True:
            smallest = i
            left = self.left(i)
            right = self.right(i)
            if left < n and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < n and self._heap[self.right(i)] <= self._heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self._heap[i],self._heap[smallest] = self._heap[smallest],self._heap[i]
            i = smallest
           
    def pop_out(self):
        num = self._heap[0]
        self.sift_down()
        return num
    def get_list(self):
        return self._heap