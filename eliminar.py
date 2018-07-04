import sys
def eliminarRepetidos(file):
	f = open(file,"r")
	columnNames = f.readline()
	listaChida = list(set(f))
	f2 = open(file,"w")
	f2.write(columnNames)
	for elemento in listaChida:
		f2.write(elemento)
	f.close()
	f2.close()

def main():
	try:
		file = sys.argv[1]
		eliminarRepetidos(file)
	except IndexError:
		print("no introduciste un archivo")
		

#main()