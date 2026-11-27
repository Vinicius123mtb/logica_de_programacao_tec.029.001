# entrada de dados
nome = input("Informe o nome: ").strip().title()
nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))

# processamento de dados
media = (nota1+nota2)/2

#  saída de dados
print(f"Média: {media}")

#  estrutura de decisão
if media >= 7:
    print(f"{nome} está aprovado.")
elif media >=5:
    print(f"{nome} está de recuperação.")
else:
    print(f"{nome} está reprovado.")