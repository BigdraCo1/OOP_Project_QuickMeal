class Food:
    ID = 1

    def __init__(self, id: str, name: str, type: str, size: dict, price: int, current_size=None):
        if price < 0:
            raise ValueError('Price must be positive')
        if id == "auto":
            self.__id = f"F{Food.ID}"
            Food.ID += 1
        else:
            self.__id = id
        self.__name = name
        self.__type = type
        self.__size = size
        self.__price = price
        self.__current_size = current_size

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def size(self):
        return self.__size

    @property
    def price(self):
        return self.__price

    @property
    def current_size(self):
        return self.__current_size

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @type.setter
    def type(self, new_type: str):
        self.__type = new_type

    @size.setter
    def size(self, new_size: dict):
        self.__size = new_size

    @price.setter
    def price(self, new_price: int):
        if new_price < 0:
            raise ValueError("This value must be positive")
        self.__price = new_price

    @current_size.setter
    def current_size(self, new_current_size):
        self.__current_size = new_current_size
