class user():
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self.perfer_item = []
    def get_username(self):
        return self._username
    def get_password(self):
        return self._password
    def get_perfer_item(self):
        return self.perfer_item