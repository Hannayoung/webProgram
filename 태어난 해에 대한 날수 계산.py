print("Enter today")

yearOfToday = int(input("Year : "))
monthOfToday = int(input("Month : "))
dayOfToday = int(input("Day : "))

yearOfBirthday = int(input("Year : "))
monthOfBirthday = int(input("Month : "))
dayOfBirthday = int(input("Day : "))


print(yearOfToday)
print(monthOfToday)
print(dayOfToday)

print(yearOfBirthday)
print(monthOfBirthday)
print(dayOfBirthday)

days = 0
currentMonth = 0

if (monthOfBirthday == 1 ):
       days = days + 31
elif (monthOfBirthday == 2 ):
       days = days + 28
       if (yearOfBirthday % 4 == 0 and yearOfBirthday % 100 != 0 or yearOfBirthday % 400 == 0 ):
            days = days + 1
elif (currentMonth == 3 ):
       days = days + 31
elif (currentMonth == 4 ):
       days = days + 30
elif (currentMonth == 5 ):
       days = days + 31
elif (currentMonth == 6 ):
       days = days + 30
elif (currentMonth == 7 ):
       days = days + 31
elif (currentMonth == 8 ):
       days = days + 31
elif (currentMonth == 9 ):
       days = days + 30
elif (currentMonth == 10 ):
       days = days + 31
elif (currentMonth == 11 ):
       days = days + 30
else: # is 12
       days = days + 31
       
days -= dayOfBirthday + 1
# days = days -  dayOfBirthday + 1

print(days)

currentMonth = monthOfBirthday + 1
while (currentMonth <= 12) :
   if (currentMonth == 1 ):
       days = days + 31
   elif (currentMonth == 2 ):
       days = days + 28
       if (yearOfBirthday % 4 == 0 and yearOfBirthday % 100 != 0 or yearOfBirthday % 400 == 0 ):
            days = days + 1
   elif (currentMonth == 3 ):
       days = days + 31
   elif (currentMonth == 4 ):
       days = days + 30
   elif (currentMonth == 5 ):
       days = days + 31
   elif (currentMonth == 6 ):
       days = days + 30
   elif (currentMonth == 7 ):
       days = days + 31
   elif (currentMonth == 8 ):
       days = days + 31
   elif (currentMonth == 9 ):
       days = days + 30
   elif (currentMonth == 10 ):
       days = days + 31
   elif (currentMonth == 11 ):
       days = days + 30
   else: # is 12
       days = days + 31
   currentMonth+=1


print(days)   


