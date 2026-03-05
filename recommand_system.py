from user import user


class recommondation_system():
    def __init__(self,user):
        self._user = user
    def recommend(self):
        perfer_item = self._user.get_perfer_item()
        recommend_list = []
        for item in perfer_item:
            recommend_list.append(item)
        return recommend_list