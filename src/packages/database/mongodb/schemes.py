class Users:

    def __init__(self, user_id, chat_id, first_name, last_name, username, name_module, date):
        self.user_id = user_id
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.name_module = name_module
        self.date = date

    def get_data(self):
        data = {
            "user_id": self.user_id,
            "chat_id": self.chat_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "name_module": self.name_module,
            "date": self.date,
        }
        return data
