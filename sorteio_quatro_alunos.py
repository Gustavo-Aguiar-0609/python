#importando biblioteca random
import random
#entrada dos nomes dos alunos
aluno1 = input("Digite o numero do 1 aluno -->")
aluno2 = input("Digite o numero do 2 aluno -->")
aluno3 = input("Digite o numero do 3 aluno -->")
aluno4 = input("Digite o numero do 4 aluno -->")
#lista com alunos
alunos = [aluno1,aluno2,aluno3,aluno4]
#sorteio
escolhido = random.choice(alunos)
#imprime o resultado
print("O Aluno escolhido foi -->", escolhido)