import random

def guess_number(): #definir a função def e criar o bloco com o código...
    print("\nWelcome! Aqui iremos sortear teu número!!\n")
    numbrs = int(input("Qual a quantidade de números a serem sorteados?")) #criando a variável
    numero_sorteado = random.randint(1, numbrs) #vai escolher o num de 1 até o num que o usuário definir
    print(f"\nO número sorteado foi:{numero_sorteado}, parabéns ao vencedor!!") #frase que virá com o número sortedo

guess_number() #tem que chamar a função no final do código, para que seja executada!

