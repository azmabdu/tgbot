all_objects = set()


class Product:
    def __init__(self, name: str, type: str, size: int, sex: str, state: str, photo_url: str):
        all_objects.add(self)
        self.name = name
        self.type = type
        self.size = size
        self.sex = sex
        self.state = state
        self.photo_url = photo_url

    def __str__(self) -> str:
        return self.name + ' ' + self.type


p = Product('Azimjon', 'Jeans', 10, 'male', 'b/u', 'dawd')
p2 = Product('Azizjon', 'Jacket', 10, 'male', 'b/u', 'ooo')
