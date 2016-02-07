import time
import math
import calendar
again = 'yes'
#search in a string where is the number
def findnumber(nower):
	for b in range(len(nower)):
		if nower[b].isdigit():
			break
	return b
#calcul the total of year
def calculyear():
	global now,tm
	nower = now[0]
	born = tm[0]
	b = findnumber(nower)
	moment = nower[b:]
	#print(moment)
	moment = int(moment)
	born = int(born)
	year = moment - born
	b = findnumber(now[1])
	moment = now[1]
	moment = moment[b:]
	if int(moment) < int(tm[1]):
		year = year - 1
	return year
#calcul the total of month
def calculmonth():
	global now,tm,year
	b = findnumber(now[1])
	moment = now[1]
	moment = moment[b:]
	if not int(moment) < int(tm[1]):
		#debug
		#print("Moment not < tm[1]")
		#print("Year: ",year)
		#print("Month +: ",12 * (year -1))
		month = 12 * (year - 1)
		#debug
		#print("Month after: ",month)
		month = month + int(moment) - int(tm[1])
		#debug
		#print("Month after after: ",month)
	elif int(moment) < int(tm[1]):
		#debug
		#print("Month < tm[1]")
		#print("Month + ",12 * (year -2))
		month = 12 * (year - 2)
		#debug
		#print("MOnth after: ",month)
		month = month + int(moment) + 12 - int(tm[1])
		#debug
		#print("MOnth after after: ",month)
		month = month - 1
	b = findnumber(now[2])
	moment = now[2]
	moment = moment[b:]
	if int(moment) > int(tm[2]):
		month = month - 1
	return month
def dayofmonth(d):
	if d == 0:
		da = 31
	elif d == 1:
		da = 31
	elif d == 2:
		da = 31 + 28
	elif d == 3:
		da = 31 + 28 + 31
	elif d == 4:
		da = 31 + 28 + 31 + 30
	elif d == 5:
		da = 31 + 28 + 31 + 30 + 31
	elif d == 6:
		da = 31 + 28 + 31 + 30 + 31 + 30
	elif d == 7:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31
	elif d == 8:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
	elif d == 9:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
	elif d == 10:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
	elif d == 11:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
	elif d == 12:
		da = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
	return da
def rest(d):
	if d == 1:
		dam = 31
	elif d == 2:
		dam = 31 + 30
	elif d == 3:
		dam = 31 + 30 + 31
	elif d == 4:
		dam = 31 + 30 + 31 + 30
	elif d == 5:
		dam = 31 + 30 + 31 + 30 + 31
	elif d == 6:
		dam = 31 + 30 + 31 + 30 + 31 + 31
	elif d == 7:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30
	elif d == 8:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
	elif d == 9:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
	elif d == 10:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
	elif d == 11:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28
	elif d == 12:
		dam = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
	return dam
def calendiar():
	global tm
	calend = calendar.month(int(tm[0]),int(tm[1]),2,1)
	calend = calend.split(" ")
	calend = calend[len(calend) - 1]
	b = findnumber(calend)
	calend = calend[b:b+2]
	calend = int(calend)
	if calend == 27:
		calend = 28
	return calend
def calculday():
	global now,tm,year,month
	b = findnumber(now[2])
	moment = now[2]
	moment = moment[b:]
	calend = calendiar()
	daypiu = calend - int(tm[2]) + 1
	mois = tm[1]
	day = 11 - int(tm[1])
	day = rest(day)
	nower = now[1]
	b = findnumber(now[1])
	dayof = dayofmonth(int(nower[b:]))
	day = day + dayof
	day = day + (365 * (year - 1)) + round((year - 1) / 4)
	day = day + daypiu + int(moment)
	return day
def play():
	global now,tm,year,month
	now = time.localtime(time.time())
	now = str(now)
	now = now.split(",")
	#print(now)
	birt = input("When were you born? ")
	tm = birt.split("-")
	tm.reverse()
	year = calculyear()
	print("Year: ",year)
	month = calculmonth()
	print("Month: ",month)
	day = calculday()
	print("Day: ",day)
if __name__ == "__main__":
	play()
