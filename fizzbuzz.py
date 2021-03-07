#Jackson Eubank
#CS362
#HW7 - FizzBuzz Testing

def parseNumb(numb):
    if (numb % 3 != 0 and numb % 5 != 0):
        return str(numb);
    elif (numb % 3 == 0 and numb % 5 != 0):
        return "Fizz";
    elif (numb % 3 != 0 and numb % 5 == 0):
        return "Buzz";
