import csv
import os
from subprocess import call

# as pastas "codigos", "entradas" e "saidas", já devem estar criadas.

# tempo de execução máximo
second_limit = 2

def make_dir():
	# pasta de saida dos arquivos compilados
	if os.path.isdir("out"):
		pass
	else:
		os.mkdir("out")
	
	# pasta de saida dos arquivos executados
	if os.path.isdir("cout"):
		pass
	else:
		os.mkdir("cout")

def count_lines(output_correct):
	# conta a qtd de linhas para mostrar a porcentagem de acerto
	count = 0
	with open("saidas/" + output_correct, 'r') as file:
		for line in file:
			count += 1
	return count

def search_file(file_name):
	# busca o nome do aluno no arquivo e verifica na pasta de codigos
	name = os.listdir("codigos/")

	for file in name:
		if(file == file_name):
			return True

	return False

def compile(file_name, output):
	"""Funcao que compila o codigo da pessoa"""
	if(call(["g++", "codigos/" + file_name, "-o", "out/" + output]) == 0):
		return True
	else:
		return False

def execute(output, cin, file_output):
	"""Executa o codigo da pessoa e guarda a saida em um arquivo"""
	if(os.system("timeout " + str(second_limit) + "s out/./" + output + " < " + "entradas/" + cin + " > " + "cout/" + file_output) == 0):
		return True
	else:
		return False

def correct(output_correct, file_output):

	file_ok = open("saidas/" + output_correct, 'r')
	file_correct = open("cout/" + file_output, 'r')

	# numero da linha incorreta, linha incorreta
	incorrect_rows = []

	count_line = 0

	# qtd linhas
	qtd_lines_file_ok = count_lines(output_correct)

	# qtd erros
	correct = 0

	line_student = file_correct.readline()

	# compara as saidas
	for line in file_ok:

		# numero da linha no arquivo
		count_line += 1

		if(line == line_student):
			correct += 1
		else:
			incorrect_rows.append( (count_line, line_student) )

		line_student = file_correct.readline()

	return ((correct/qtd_lines_file_ok)*100, incorrect_rows)

def corretor(arq_csv, arq_entradas, arq_saidas, exercicio):
	"""
	Responsável por compilar, executar e verificar as respostas

	arq_csv = nome do arquivo csv, por padrão será "nomes.csv".
	arq_entradas = lista de arquivos de entradas, com os respectivos nomes.
	arq_saidas = lista de arquivos de saida, usado para comparar com as respostas do aluno.
	exercicio = string com o nome do exercicio.
	"""

	make_dir()

	with open(arq_csv, 'r') as file_name:
		reader = csv.reader(file_name)
		for row in reader:
			# nome do arquivo fonte
			name = row[0]+ "_" + exercicio + ".cpp"
			
			# nome do arquivo binario de saida
			name_output_bin = row[0] + "_" + exercicio + ".out"

			# nome do arquivo de saidas do executavel
			name_output_cout = row[0] + "_" + exercicio + ".txt"

			if(search_file(name)):
				# compila o codigo
				if(compile(name, name_output_bin)):
					# testa as entradas
					print("nome:", row[1])
					for i, cin in enumerate(arq_entradas):
						# executa
						if(execute(name_output_bin, cin, name_output_cout)):
							# verifica corretude
							print("arquivo", i+1, correct(arq_saida[i], name_output_cout)[0], "% correto")
						else:
							print("entrou em loop")
				else:
					print("erro de compilação meu chapa!")

arq_csv = "nomes.csv"
arq_entradas = ["entrada_e1_1.txt","entrada_e1_2.txt"]
arq_saida = ["saida_e1_1.txt", "saida_e1_2.txt"]

corretor(arq_csv, arq_entradas, arq_saida, 'e1')