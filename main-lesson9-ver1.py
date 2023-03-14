import valid as v

class Trip:
    def __init__(self, miles, gallons):
        self.__miles = miles
        self.__gallons = gallons
        self.__mpg = miles/gallons

    def get_miles(self):
        return self.__miles

    def get_gallons(self):
        return self.__gallons

    def get_mpg(self):
        return self.__mpg

    def set_miles(self, miles):
        self.__miles = miles

    def set_gallons(self, gallons):
        self.__gallons = gallons

    def calc_mpg(self):
        self.__mpg = self.__miles/self.__gallons


def main():
    miles = 0.0
    gallons = 0.0
    mpg = 0.0

    print("Welcome to the MPG Calculator!\n")

    miles = v.get_real("Enter the number of miles driven: ")
    gallons = v.get_real("Enter the number of gallons of gas used: ")

    #mpg = calc_mpg(miles, gallons)

    message = mpg_message(mpg)

    output_result(mpg, message)


def welcome():
    print("Welcome to the MPG Calculator!\n")

def calc_mpg(miles, gallons):
    mpg = 0.0
    mpg = miles / gallons
    return mpg

def output_result(mpg, message):
    print("\nYour car gets", format(mpg, ".1f"), "miles per gallon!")
    print(message)

def mpg_message(mpg):
    message = ""
    if mpg >= 30:
        message = "That's pretty good gas mileage."
    elif mpg >= 20:
        message = "You might want a new car."
    else:
        message = "Your mileage isn't looking so good."
    return message

main()