# Write your solution here
user_year=int(input('Year: '))
leap_year=[]
not_leap_year=[]
essais=0

while essais<10:
	if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
		leap_year.append(user_year)
	else:
		not_leap_year.append(user_year)
	user_year += 1
	essais+=1

# print(f"leap year {leap_year} - {leap_year[0]} - {leap_year[1]}")
if user_year < leap_year[0]:
	print(f"Leap year : {leap_year[0]}")
#	if leap_year[0] == user_year:
#		print(f"The next leap year after {user_year} is {leap_year[1]}")
