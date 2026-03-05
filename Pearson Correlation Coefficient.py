class PCC:
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y
        self.x_average = 0
        self.y_average = 0
        self.ppc = 0
    def calculate(self):
        x_list = []
        y_list = []
        sum = 0   
        for i in self.x:
            self.x_average += i / len(self.x)
        for i in self.y:
            self.y_average += i / len(self.y)
        for i in self.x:
           x = i - self.x_average 
           x_list.append(x)
        for i in self.y:
            y = i - self.y_average
            y_list.append(y) 
        i = len(self.x) - 1
        j = len(self.y) - 1
        while i >= 0 and j >= 0:
            molecular += x_list[i] * y_list[j]
            i -= 1
            j -= 1
        for i in x_list:
            denominator_x += i * i
        for i in y_list:
            denominator_y += i * i
        denominator = (denominator_x * denominator_y) ** 0.5
        if denominator == 0:
            return 0
        self.ppc = molecular / denominator
        return self.ppc 