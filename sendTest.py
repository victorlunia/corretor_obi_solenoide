import send_email as s

server = s.connectSmtp()
s.attempLogin(server)

assunto='TESTE 123'
texto='hello world'

s.send_email(server,assunto,texto,'clemilton.ufam@gmail.com')

server.quit()
