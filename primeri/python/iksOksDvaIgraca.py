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

def potez(tabla, znak):
	print 'igra '+znak
	pozicija = preuzmi_poziciju()
	while not je_slobodno_mesto(tabla,pozicija):
		pozicija = preuzmi_poziciju()
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
		kraj = potez(tabla,'x')
		if kraj:
			break
		kraj = potez(tabla,'o')
		if kraj:
			break
	print 'kraj'

igra()
