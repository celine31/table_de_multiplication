continuer='o'
while continuer=='o':
	nombre=input('entrez un nombre: ')

	for i in range(1,11):
		#print(i*nombre)
		 print('{0}*{1}={2}'.format(i,nombre,i*nombre))

	continuer = raw_input('voulez vous continuer ? : o/n ')
print('fin des multiplications')