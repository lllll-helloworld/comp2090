from user import user
from product import PRODUCT, product_list_manager

class recommondation_system():
    def __init__(self,user):
        self._user = user
    def recommend(self):
        