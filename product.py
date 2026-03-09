class PRODUCT:
    def __init__(self,name):
        self.name = name
        self.price = 0
        self.score = 0
        self.sales = 0
        self.type = {}
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
    def set_price(self,price):
        self.price = price

class product_list_manager():
    def __init__(self):
        self._product_list = []
    def add_product(self,product):
        self._product_list.append(product)
    def get_product_list(self):
        return self._product_list
    def get_product_by_name(self,name):
        for product in self._product_list:
            if product.get_name() == name:
                return product
        return None
    def delete_product_by_name(self,name):
        for product in self._product_list:
            if product.get_name() == name:
                self._product_list.remove(product)
                return True
        return False