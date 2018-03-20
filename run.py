import corretor as crt

exercicio = "e1"
arq_csv = "nomes.csv"
crt.corretor(arq_csv, crt.get_arqs(exercicio, "entradas/"), crt.get_arqs(exercicio, "saidas/"), exercicio)