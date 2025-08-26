import datetime

a = datetime.datetime.now()
print(a)

print(a.year)
print(a.strftime("%A"))

# creating date object
b = datetime.datetime(2025 , 8 , 25)

print(b.strftime("%B"))



#  we are using 
"""
%a for 	Weekday, short version
%A for 	Weekday, full version
%w	Weekday as a number 0-6, 0 is Sunday
%d	Day of month 01-
%b	Month name, short version
%B	Month name, full version
%m	Month as a number 01-12
%y	Year, short version, without century
%Y	Year, full version
%H	Hour 00-23
%I	Hour 00-12
%p	AM/PM

"""