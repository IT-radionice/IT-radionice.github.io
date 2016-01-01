def kalkulator():
	while True:
		x = raw_input("prvi broj: ")
		if x == "":
			break
		else:
			x = float(x)
		znak = raw_input("znak: ")
		if znak == "":
			break
		y = raw_input("drugi broj: ")
		if y == "":
			break
		else:
			y = float(y)
		rezultat = izracunaj(x,znak,y)
		if rezultat==None:
			print "Greska!"
		else:
			prikazi(x,znak,y,rezultat)
	print "dovidjenja!"

def izracunaj(x, znak, y):
	if znak=="+":
		return x+y
	elif znak=="-":
		return x-y
	elif znak=="*":
		return x*y
	elif znak=="/":
		return x+y
	else:
		return None

def prikazi(x, znak, y, rezultat):
	print str(x)+znak+str(y)+"="+str(rezultat)

kalkulator()
