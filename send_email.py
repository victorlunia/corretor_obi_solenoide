import smtplib

import config
import socket

def connectSmtp():
    while True:
        try:   
            print("Conectando ao servidor smtp"); 
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            print("Conectado!!")

            
            return smtp;  
        except:
            print("Erro. Tentando novamente");

def attempLogin(server):
	while True:
		try:
			print('Tentanto o login')
			server.login(config.EMAIL_ADDRESS,config.PASSWORD)
			print('Logado!!')
			break;
		except:
			print('Erro Tentando logar novamente!')

def send_email(server,subject,text,email):
	try:
		

		print('Sending email to '+email)
		de='From: '+config.EMAIL_ADDRESS+'\n'
		para='To: '+email+'\n'
		assunto='Subject: '+subject+'\n\n'

		msg=de+para+assunto+text
		server.sendmail(config.EMAIL_ADDRESS,[email],msg)
		print("Sucess Email sent to "+email)
	except:
		print("Email failed to send to "+email)




