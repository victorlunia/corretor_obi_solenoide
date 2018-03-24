import corretor as crt
import time
exercicio = ["e1", "e2"]
arq_csv = "nomes.csv"

while(True):
	print("executando")
	for e in exercicio:
		crt.corretor(arq_csv, crt.get_arqs(e, "entradas/"), crt.get_arqs(e, "saidas/"), e)
		time.sleep(5)
	time.sleep(60)