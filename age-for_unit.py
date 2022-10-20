print("#" *100)
print(" U can enter first letter or full word of time unit ".center(100,'#'))
print("#" *100)
#_____________________________________________________________________________#
age = input("enter Ur age: ").strip()
unit = input("enter Ur unit[years,months,weeks,days]: ").strip().lower()
years = age
months = int(age) * 12
weeks = months * 4
days = int(age) * 365
#_______________________________________________________________________________#
if unit == 'years' or unit == 'y':
    print("Hi U choosed unit years")
    print(f"U lived for {years} years")

elif unit == 'months' or unit == 'm':
    print("Hi U choosed unit months")
    print(f"U lived for {months:,} months")

elif unit == 'weeks' or unit == 'w':
    print("Hi U choosed unit weeks")
    print(f"U lived for {weeks:,} weeks")

elif unit == 'days' or unit == 'd':
    print("Hi U choosed unit days")
    print(f"U lived for {days:,} days")
