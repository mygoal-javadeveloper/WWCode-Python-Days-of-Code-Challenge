# Create a program that checks if a year is a leap year.

# According to Wikipedia:
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are
# That means
# any_year % 4 == 0 But Not any_year % 100 == 0
# Or any_year % 400 == 0

def findleapyear():
  yr = input('Enter the year to check if it is a leap year or not: \n')
  if yr.isdigit():
    if (int(yr)%400 == 0) or (int(yr)%4 == 0 and int(yr)%100 != 0):
      print('Entered year', yr, 'is a leap year.')
    else:
      print('Entered year', yr, 'is not a leap year.')
  else:
    print('Invalid Entry')

findleapyear()