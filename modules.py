class basic:
    def __init__(self, basic_name,basic_size):
        self.basic_name = basic_name
        self.basic_size = basic_size
        self.basetime = 10

    def getComodity_Name(self):#封装
        return self.basic_name
    def calculate_time(self):
        return self.basetime
    def set_vip(self):
        self.vip = True
    def get_vip(self):
        return self.vip
class Comodity(basic):#继承
    def __init__(self,name,size,topping = None):
        super().__init__(name,size)
        self.topping = topping or []
    def calculate_time(self): #重写父类方法,这里表现多态
        extral_time = len(self.topping) * 2
        return self.basetime + extral_time + 15

class Order:
    def __init__(self,Order_ID,Comodity,is_vip = False,quantity = 1):
        self.Order_ID = Order_ID
        self.Comodity = Comodity
        self.is_vip = is_vip
        self.quantity = quantity
        self.basic_score = 2000
        self.priority_score = self.caculate_priority()
    def caculate_priority(self):#计算优先级
        basic_score = self.basic_score
        if self.is_vip:
            basic_score -= 1000
            basic_score += self.Comodity.calculate_time()
        return basic_score
    def __lt__(self, other):
        return self.priority_score < other.priority_score
        

    