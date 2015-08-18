# Calculate function
def ecal(enumber):
	money = 0
	if enumber < 0:
		print("The electrical number cannot be negative!")
		return 0
	if enumber <= 50:
		money = enumber * 4
		return money
	if enumber <= 100:
		money = 50 * 4 + (enumber - 50) * 3
		return money
	else:
		money = 50 * 4 + 50 * 3 + (enumber - 100) * 2
		return money

print("Enter the electric number of first family:")
ef1 = float(input())
mf1 = ecal(ef1)

print("Enter the electric number of second family:")
ef2 = float(input())
mf2 = ecal(ef2)

print("Family \t| F1 \t\t| F2")
print("enumber | %f \t| %f"%(ef1,ef2))
print("money \t| %f \t| %f"%(mf1,mf2))
