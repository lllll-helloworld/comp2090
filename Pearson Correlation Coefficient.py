class PCC:
    def __init__(self, x = [], y = []):
        self.ppc = 0
    def calculate(self,x,y):
        x_average = 0
        y_average = 0
        x_list = []
        y_list = []
        sum = 0   
        for i in x:
            x_average += i / len(x)
        for i in y:
            y_average += i / len(y)
        for i in x:
           x = i - x_average 
           x_list.append(x)
        for i in y:
            y = i - y_average
            y_list.append(y) 
        i = len(x) - 1
        j = len(y) - 1
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