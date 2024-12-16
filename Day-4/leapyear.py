#python program to checked a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Test the function
year = 2024
print(f"Is {year} a leap year?", is_leap_year(year))
