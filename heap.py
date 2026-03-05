class heap_object:
    def __init__(self):
        self._heap = []
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def insert(self,data):
        self.heap.append(data)
        self.sift_up()
    def sift_up(self):
        i = len(self.heap)-1
        while True:
            if i == 0:
                break
            if self.heap[self.parent(i)] <= self.heap[i]:
                self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]
                i = self.parent(i)
            else:
                break

    def sift_down(self):
        n = len(self.heap)-1
        self.heap[0] = self.heap[n]
        self.heap.pop()
        i = 0
        while True:
            largest = i
            left = self.left(i)
            right = self.right(i)
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[self.right(i)] >= self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
           
    def pop_out(self):
        num = self.heap[0]
        self.sift_down()
        return num
    def get_list(self):
        return self.heap