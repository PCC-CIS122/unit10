class Flower:
    __type__ = ""
    __color__ = ""

    def __init__(self, t, c):
        self.__type__ = t
        self.__color__ = c

    def get_type(self):
        return self.__type__

    def get_color(self):
        return self.__color__

    def set_type(self, t):
        self.__type__ = t

    def set_color(self, c):
        self.__color__ = c


def main():
    red_rose = Flower("rose", "red")
    pink_rose = Flower("rose", "pink")
    tulip = Flower("tulip", "yellow")

    print(red_rose)
    print(pink_rose)
    print(tulip)


main()