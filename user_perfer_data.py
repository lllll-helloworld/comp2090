
class UPD:
    def __init__(self):
        self._upd_json1 = {}
        self._upd_json2 = {}
        self._upd_list1 = []
        self._upd_list2 = []
    def add_upd():
        pass
    def get_upd_list1():
        pass
    def get_upd_list2():
        pass
    def delete_upd():
        pass
    def check_upd():
        pass 
    def update_upd():
        pass

class user_perfer_data(UPD):
    def __init__(self):
        super().__init__()
    def add_upd(self,user_data1,user_data2):
        self._upd_json1.append(user_data1)
        self._upd_json2.append(user_data2)#这里有bug
    def get_upd_list1(self):
        return self._upd_json1
    def get_upd_list2(self):
        return self._upd_json2
    def delete_upd(self,product):
        if product in self._upd_json1:
            index = self._upd_json1.index(product)
            self._upd_json1.pop(index)
        if product in self._upd_json2:
            index = self._upd_json2.index(product)
            self._upd_json2.pop(index)
    def check_upd(self,user1,user2):
        if user1.get_username() == user2.get_username():
            return True
        else:
            return False
    def update_upd(self,user1,user2):
        user1_perfer_item = user1.score_of_perfer_item()
        user2_perfer_item = user2.score_of_perfer_item()
        for item in user1_perfer_item:
            item_score = user1_perfer_item[item]
            self._upd_list1.append(item_score)
        for item in user2_perfer_item:
            item_score = user2_perfer_item[item]
            self._upd_list2.append(item_score)
        