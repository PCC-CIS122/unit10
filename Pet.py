class Pet:
    __name = ""
    __age = 0

    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def __str__(self):
        return self.__name + " is " + str(self.__age) + " years old."

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, n):
        self.__name = n

    def set_age(self, a):
        self.__age = a


def main():
    pet_list = []
    pet_list.append(Pet("Fluffy", 10))
    pet_list.append(Pet("Billy", 4))
    pet_list.append(Pet("Chance", 14))

    print("Iterating through list by Pet object")
    for pet in pet_list:
        print(pet)

    print("\nIterating through the list by index")
    for index in range(len(pet_list)):
        print(index, pet_list[index])


main()
