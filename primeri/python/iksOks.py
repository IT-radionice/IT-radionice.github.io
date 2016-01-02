def inicijalizuj_tablu():
	return [' ']*9

def preuzmi_poziciju():
	ret_val = ""
	while not ret_val in "0 1 2 3 4 5 6 7 8".split(' '):
		ret_val = raw_input("pozicija: ")
	return int(ret_val)

def je_slobodno_mesto(tabla,pozicija):
	return tabla[pozicija]==' '

def upisi_poziciju(tabla, pozicija, karakter):
	tabla[pozicija]=karakter

def je_kraj(tabla):
	for pozicija in range(9):
		if je_slobodno_mesto(tabla,pozicija):
			return False
	return True

def je_pobedio(tabla, znak):
	return ((tabla[6] == znak and tabla[7] == znak and tabla[8] == znak) or # gornja horizontala
		(tabla[3] == znak and tabla[4] == znak and tabla[5] == znak) or # srednja horizontala
		(tabla[0] == znak and tabla[1] == znak and tabla[2] == znak) or # donja horizontala
		(tabla[6] == znak and tabla[3] == znak and tabla[0] == znak) or # znakva vertikala
		(tabla[7] == znak and tabla[4] == znak and tabla[1] == znak) or # srednja vertikala
		(tabla[8] == znak and tabla[5] == znak and tabla[2] == znak) or # desna vertikala
		(tabla[6] == znak and tabla[4] == znak and tabla[2] == znak) or # dijagonala
		(tabla[8] == znak and tabla[4] == znak and tabla[0] == znak)) # dijagonala

def prikazi_tablu(tabla):
	print '   |   |'
	print ' ' + tabla[6] + ' | ' + tabla[7] + ' | ' + tabla[8]
	print '   |   |'
	print '-----------'
	print '   |   |'
	print ' ' + tabla[3] + ' | ' + tabla[4] + ' | ' + tabla[5]
	print '   |   |'
	print '-----------'
	print '   |   |'
	print ' ' + tabla[0] + ' | ' + tabla[1] + ' | ' + tabla[2]
	print '   |   |'
	print ''

def kopiraj_tablu(tabla):
	nova_tabla = []
	for e in tabla:
		nova_tabla.append(e)
	return nova_tabla

def odredi_poziciju(tabla, znak):
	if znak == "x":
		protivnicki_znak = "o"
	else:
		protivnicki_znak = "x"

	# 1. Pobeda
	for i in range(9):
		if je_slobodno_mesto(tabla,i):
			kopija = kopiraj_tablu(tabla)
			upisi_poziciju(kopija,i, znak)
			if je_pobedio(kopija, znak):
				return i

	# 2. Blokiranje
	for i in range(9):
		if je_slobodno_mesto(tabla,i):
			kopija = kopiraj_tablu(tabla)
			upisi_poziciju(kopija,i, protivnicki_znak)
			if je_pobedio(kopija, protivnicki_znak):
				return i

	# 3. Uglovi
	for i in [0,2,6,8]:
		if je_slobodno_mesto(tabla,i):
			return i

	# 4. Centar
	if je_slobodno_mesto(tabla,4):
		return 4

	# 5. Stranice
	for i in [1,3,5,7]:
		if je_slobodno_mesto(tabla,i):
			return i


def potez(tabla, znak, racunar):
	print 'igra '+znak
	
	if racunar == False:
		pozicija = preuzmi_poziciju()
		while not je_slobodno_mesto(tabla,pozicija):
			pozicija = preuzmi_poziciju()
	else:
		pozicija = odredi_poziciju(tabla, znak)
	
	upisi_poziciju(tabla, pozicija, znak)
	prikazi_tablu(tabla)
	if je_pobedio(tabla, znak):
		print 'pobedio je '+znak
		return True
	if je_kraj(tabla):
		print 'nema pobednika'
		return True
	return False

def igra():
	tabla = inicijalizuj_tablu()
	prikazi_tablu(tabla)
	while True:
		kraj = potez(tabla,'x',False)
		if kraj:
			break
		kraj = potez(tabla,'o',True)
		if kraj:
			break
	print 'kraj'

igra()
