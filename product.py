class PRODUCT:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.score = 0
        self.sales = 0
        self.type = 0
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_score(self):
        return self.score
    def get_sales(self):
        return self.sales
    def get_type(self):
        return self.type
    def set_score(self,score):
        self.score = score
    def set_sales(self,sales):
        self.sales = sales
    def set_type(self,type):
        self.type = type