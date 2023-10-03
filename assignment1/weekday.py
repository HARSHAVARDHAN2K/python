def weekday(day,month,year):
    yeardigit = year%100
    yearcode = (yeardigit+(yeardigit//4))%7

    monthcode = (0,3,3,6,1,4,6,2,5,0,3,5)

    centurycode = (18 - (year // 100)) % 7

    dateNumber = day
    total = yearcode+monthcode[month]+centurycode+day-1-leapyear(year)
    return total%7

def leapyear(year):
    if year%4==0 and (year%400==0 or year%100!=0):
        return 1
    return 0
                
day,month,year = (input("enter the day month and year :")).split()

wekday = weekday(int(day),int(month),int(year))
print(wekday)