import pygame

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

def iscrtaj_tablu(tabla, povrsina, pozadina, x_img, o_img):
	povrsina.blit(pozadina, (0, 0)) # postavljanje pozadine
	iscrtaj_znakove(tabla, povrsina, x_img, o_img) # iscrtaj sve znakove
	pygame.display.update() # azuriranje radne povrsine

def kraj_igre(tabla, znak):
	if je_pobedio(tabla, znak):
		print 'pobedio je '+znak
		return True
	if je_kraj(tabla):
		print 'nema pobednika'
		return True
	return False

def pozicija_na_tabli(koordinate):
	if koordinate[0]>=0 and koordinate[1]>=0 and koordinate[0]<=197 and koordinate[1]<=197:
		return 6
	if koordinate[0]>=200 and koordinate[1]>=0 and koordinate[0]<=397 and koordinate[1]<=197:
		return 7
	if koordinate[0]>=400 and koordinate[1]>=0 and koordinate[0]<=597 and koordinate[1]<=197:
		return 8
	if koordinate[0]>=0 and koordinate[1]>=200 and koordinate[0]<=197 and koordinate[1]<=397:
		return 3
	if koordinate[0]>=200 and koordinate[1]>=200 and koordinate[0]<=397 and koordinate[1]<=397:
		return 4
	if koordinate[0]>=400 and koordinate[1]>=200 and koordinate[0]<=597 and koordinate[1]<=397:
		return 5
	if koordinate[0]>=0 and koordinate[1]>=400 and koordinate[0]<=197 and koordinate[1]<=597:
		return 0
	if koordinate[0]>=200 and koordinate[1]>=400 and koordinate[0]<=397 and koordinate[1]<=597:
		return 1
	if koordinate[0]>=400 and koordinate[1]>=400 and koordinate[0]<=597 and koordinate[1]<=597:
		return 2

def koordinate_pozicije(pozicija):
	if(pozicija == 6):
		return (0,0)
	if(pozicija == 7):
		return (200,0)
	if(pozicija == 8):
		return (400,0)
	if(pozicija == 3):
		return (0,200)
	if(pozicija == 4):
		return (200,200)
	if(pozicija == 5):
		return (400,200)
	if(pozicija == 0):
		return (0,400)
	if(pozicija == 1):
		return (200,400)
	if(pozicija == 2):
		return (400,400)

def iscrtaj_znakove(tabla, povrsina, x_img, o_img):
	for i in range(len(tabla)):
		if tabla[i]=="x":
			povrsina.blit(x_img, koordinate_pozicije(i))
		if tabla[i]=="o":
			povrsina.blit(o_img, koordinate_pozicije(i))

def pygame_igra():
	pygame.init() # iniciranje pygame modula
	povrsina = pygame.display.set_mode([600,600]) # pravljenje radne povrsine 600px X 600px
 	pozadina = pygame.image.load("tabla.png") # ucitavanje pozadine 
 	x_img = pygame.image.load("x.png") # ucitavanje slike za X 
 	o_img = pygame.image.load("o.png") # ucitavanje slike za O 
 	pygame.display.set_caption("iks oks") # postavljanje naslova prozora
 	pygame.display.update() # azuriranje radne povrsine
 	
	tabla = inicijalizuj_tablu()
	kraj = False

	# prvo igra racunar 
	print 'igra '+'o'
	pozicija = odredi_poziciju(tabla, 'o')
	upisi_poziciju(tabla, pozicija, 'o')
	iscrtaj_tablu(tabla, povrsina, pozadina, x_img, o_img)					
	kraj = kraj_igre(tabla, 'o')

 	while not kraj:
		iscrtaj_tablu(tabla, povrsina, pozadina, x_img, o_img)					
 		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				print 'igra '+'x'
				koordinate = pygame.mouse.get_pos()
	 			pozicija = pozicija_na_tabli(koordinate)
	 			if je_slobodno_mesto(tabla,pozicija):
					upisi_poziciju(tabla, pozicija, 'x')
					iscrtaj_tablu(tabla, povrsina, pozadina, x_img, o_img)					
					kraj = kraj_igre(tabla, 'x')
					if kraj:
						break
					print 'igra '+'o'
					pozicija = odredi_poziciju(tabla, 'o')
					upisi_poziciju(tabla, pozicija, 'o')
					iscrtaj_tablu(tabla, povrsina, pozadina, x_img, o_img)					
					kraj = kraj_igre(tabla, 'o')
					if kraj:
						break

 	pygame.quit() # zavrsetak igre - ponistavanje inicijalizacija
 	quit() # gasenje programa

pygame_igra()

