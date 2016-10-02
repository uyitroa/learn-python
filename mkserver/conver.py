def converplus(x):
	x = str(x)
	x = x.split('+')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] + x[1]
	return result
def converminus(x):
	x = str(x)
	x = x.split('-')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] - x[1]
	return result
def convermul(x):
	x = str(x)
	x = x.split('*')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] * x[1]
	return result
def converdiv(x):
	x = str(x)
	x = x.split('/')
	x[0] = float(x[0])
	x[1] = float(x[1])
	result = x[0] / x[1]
	return result
