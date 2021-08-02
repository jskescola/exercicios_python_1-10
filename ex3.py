#3. Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada.
nome = str(input('Qual é o seu nome?'))
diaNascimento = int(input('Que dia você nasceu?'))
mesNascimento = int(input('Que mês você nasceu?'))
anoNascimento = int(input('Em que ano você nasceu?'))
print('Olá {}, você nasceu no dia {}/{}/{}.'.format(nome,diaNascimento,mesNascimento,anoNascimento))