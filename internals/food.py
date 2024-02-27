class Food():
    def __init__(self, name: str, type: str, size: dict, price: int):
        self.__name = name
        self.__type = type
        self.__size = size
        self.__price = price

    @property
    def name(self):
        return self.__name