all_objects = set()


class Product:
    def __init__(self, name=None, type=None, size=None, gender=None, state=None, photo_url=None):
        all_objects.add(self)
        self.name = name
        self.type = type
        self.size = size
        self.gender = gender
        self.state = state
        self.photo_url = photo_url
