from heap import heap_object

class TopKCalculator:
    def __init__(self,k):
        self._k = k
        self._heap_object = heap_object()
    def insert(self,data):
        pass


class calculator(TopKCalculator):
    def __init__(self,k):
        super().__init__(k)
    def caculate_if_insert_KTOP(self,data):
        data = -data
        if len(self._heap_object.get_list()) < self._k:
            self._heap_object.insert(data)
        else:
            if data > self._heap_object.get_list()[0]:
                self._heap_object.pop_out()
                self._heap_object.insert(data)
    def get_KTOP(self):
        return [i for i in self._heap_object.get_list()]