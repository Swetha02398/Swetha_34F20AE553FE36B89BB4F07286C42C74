def check_leap(year): 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 

year = int(input("Enter a year: ")) 

print(f"{year} is leap year" if check_leap(year) else f"{year} is not leap year")