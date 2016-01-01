def pogadjanje():
	print "Zamislite broj izmedju 0 i 100"
	pocetak=0
	kraj=100
	broj_koraka=1
	while pocetak <= kraj :
		pokusaj = (pocetak + kraj)/2
		odgovor = raw_input("da li ste zamislili "+str(pokusaj)+"?")
		if odgovor == "da":
			print "broj koraka je "+str(broj_koraka)
			break
		else:
			odgovor = raw_input("da li je zamisljeni broj veci od "+str(pokusaj)+"?")
			if odgovor == "da":
				pocetak = pokusaj+1
			else:
				kraj = pokusaj-1
			if pocetak > kraj:
				print "zamisljeni broj nije u zadatom opsegu"
				print "broj koraka je "+str(broj_koraka)
			broj_koraka = broj_koraka+1
	print "dovidjenja"

pogadjanje()