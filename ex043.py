matrícula=str(input('Digite o número de matrícula: '))
nome=str(input('Digite o nome do aluno/a: '))
n1=float(input('Digite nota 1: '))
n2=float(input('Digite nota 2: '))
n3=float(input('Digite nota 3: '))
media=n1+n2+n3
m=media/3
print('O/a aluno/a {} da matrícula {}, ficou com média {:.2f}.'.format(nome, matrícula, m))
if media >= 6: 
    print('Você passou!Parabéns.')
else:
    print('Infelizmente você foi reprovado.')