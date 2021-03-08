#Jackson Eubank
#CS362
#HW7 - Leap Year

def parseYear(year):
    leapyear = 0;
    if (year % 4 == 0 and year % 100 != 0):
        leapyear = 1;
    elif (year % 4 == 0 and year % 100 == 0):
        leapyear = 0;
        
    return leapyear;
