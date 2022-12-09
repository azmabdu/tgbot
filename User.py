users = {}  # Dictionary of users - user: chat_id


class User:
    def __init__(self, name, chat_id):
        self.name = name
        self.chat_id = chat_id
        users[self] = chat_id

    def __str__(self):
        return f'User: {self.name}'
