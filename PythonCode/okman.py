import time
import math
again = 'yes'
while again == 'yes':
	now = input("Time current: ")
	
	now = str(now)

	now = now.split("-")

	now.reverse()

	#print(now)

	birt = input("When were you born? ")

	tm = birt.split("-")

	tm.reverse()

	#print(tm)

	nower = now[0]

	born = tm[0]

	for b in range(len(nower)):

		if nower[b].isdigit():

			break

	moment = nower[b:]

	#print(moment)

	moment = int(moment)

	born = int(born)

	year = moment - born

	dayplus = math.floor(year / 4)

	print("year: ",year)

	print("dayplus: ",dayplus)

	nower = now[2]

	for b in range(len(nower)):

		if nower[b].isdigit():

			break

	dayp = int(nower[b:]) - int(tm[2])

	print(dayp)

	day = (year * 365)

	print("day: ",day)
	day = day + dayplus

	day = day + dayp

	nower = now[1]

	for b in range(len(nower)):

		if nower[b].isdigit():

			break

	monthplus = int(nower[b:]) - int(tm[1])

	month = (year * 12) + monthplus

	print("Time: ",day," day, ",month," month, ",year," year.")

	again = input("Again(yes): ")
