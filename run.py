import corretor as crt
import time
import csv


arq_csv = "nomes.csv"

while(True):
	print("executando")
	exercicio = open("exercicio.csv", 'r')
	for e in exercicio:
		crt.corretor(arq_csv, crt.get_arqs(e, "entradas/"), crt.get_arqs(e, "saidas/"), e)
		time.sleep(5)
	exercicio.close()
	time.sleep(60)