from user import user
from product import PRODUCT, product_list_manager
from Pearson_Correlation_Coefficient import PCC

class recommondation_system():
    def __init__(self,user):
        self._user = user
    def recommend(self,user1,user2):
        pcc = PCC()
        user1_perfer_item = user1.get_perfer_item()
        user2_perfer_item = user2.get_perfer_item()
        result = pcc.calculate(user1_perfer_item,user2_perfer_item)
        if result > 0:
            return True
        else:
            return False