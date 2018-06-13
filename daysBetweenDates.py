daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_before(y, m, d):
    nub_days = 0
    k = m - 1
    while k > 0:
        if k == 2 and isLeapYear(y) is True:
            nub_days += 29
        else:
            nub_days += daysOfMonths[k - 1]
        k -= 1
    nub_days += d - 1
    return nub_days

def days_after(y, m, d):
    nub_days = 0
    if m == 2 and isLeapYear(y) is True:
        nub_days += 29 - d
    else:
        nub_days += daysOfMonths[m - 1] - d

    k = m + 1
    while k <= 12:
        if k == 2 and isLeapYear(y) is True:
            nub_days += 29
        else:
            nub_days += daysOfMonths[k - 1]
        k += 1
    return nub_days

def extractNLeapYears(yf, yl):
    n = yl - yf + 1
    i = yf
    num_yleap = 0
    while i <= yl:
        
        if isLeapYear(i) is True:
            num_yleap += 1
        i += 1    
        

    num_days = n * 365
    num_days += num_yleap

    return num_days - 1

def testDayFeb(y, m, day):
    if day == 29 and m == 2 and isLeapYear(y) is False:
        return False
    else:
        return True

def dateIsBefore(y1, m1, d1, y2, m2, d2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            return d1 <= d2
    return False        

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    
    # program defensively! Add an assertion if date1 > date2
    assert not dateIsBefore(y2, m2, d2, y1, m1, d1)
    days = 0
    if testDayFeb(y1, m1, d1) and testDayFeb(y2, m2, d2):
        days_years = extractNLeapYears(y1, y2)
        d_before = days_before(y1, m1, d1)
        d_after = days_after(y2, m2, d2)

        days = days_years - d_before - d_after 
    else:
        days = 'undefined'

    return days
    return nub_days


def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
