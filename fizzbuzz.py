#Jackson Eubank
#CS362
#HW7 - FizzBuzz

def parseNumb(numb):
    if (numb % 3 != 0 and numb % 5 != 0):
        return str(numb);
    elif (numb % 3 == 0 and numb % 5 != 0):
        return "Fizz";
    elif (numb % 3 != 0 and numb % 5 == 0):
        return "Buzz";
    elif (numb % 3 == 0 and numb % 5 == 0):
        return "FizzBuzz";

for x in range(1,101):
    print(parseNumb(x));
