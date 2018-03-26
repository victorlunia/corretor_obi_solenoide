import os
from random import randint
import corretor

def gera_entradas(num_exercise, qtd_entradas=None, qtd_testes=None, low=1, upr=100, arq_entradas=None):
	
	i = 0
	line = ""
	if arq_entradas == None:
		for i in range(qtd_testes):
			for j in range(qtd_entradas):
				var = randint(low, upr)
				line += str(var) + " "
			line += '\n'
			arq = open("entradas/entrada_e" + str(num_exercise) + "_" + str(i).zfill(2)+ ".txt", 'w')
			arq.write(line)
			arq.close()
			line = ""
			i += 1
	else:
		for line in arq_entradas:
			arq = open("entradas/entrada_e" + str(num_exercise) + "_" + str(i).zfill(2) + ".txt", 'w')
			arq.write(line)
			arq.close()
			i += 1

def gera_saidas(num_exercise, arq_entradas=None):

	arqs = corretor.get_arqs("e"+str(num_exercise), "entradas/")

	if arq_entradas == None:
		for i in range(len(arqs)):
			arq_saida = "saidas/saida_e" + str(num_exercise) + "_" + str(i).zfill(2) + ".txt"
			arq_entrada = "entradas/entrada_e" + str(num_exercise) + "_" + str(i).zfill(2) + ".txt"
			command = "codigo_fonte/./codigo_" + str(num_exercise) + " < " + arq_entrada + " > " + arq_saida
			os.system(command)