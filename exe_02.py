# TODO:Crie um programa que receba do usuário o nome, a massa e
# a altura, e calcule seu IMC (Índice de Massa Corporal).
# Após mostrar o IMC, o programa deve informar de acordo com o 
# valor do seu IMC:
# - IMC < 18.5: "Usuário está abaixo do peso"
# - IMC < 25: "Usuário está no peso ideal" 
# - IMC < 30: "Usuário está acima do peso"
# - IMC < 35: "Usuário está obeso"
# - IMC < 40: "Usuário está com obesidade nível 2"
# - Se não estiver em nenhum dos casos acima:
#  "Usuário está com obesidade mórbida"

nome = input("Informe o seu nome: ").strip().title()
massa = float(input("Informe a massa muscular: ").replace(",","."))
altura = float(input("Informe sua altura: ").replace(",","."))

imc = massa/(altura**2)

print(f"Seu IMC é: {imc}.")

if imc <18.5:
    print(f"Usuário está abaixo do peso.")
elif imc <25:
    print(f"Usuário está no peso ideal.")
elif imc <30:
    print(f"Usuário está acima do peso.")
elif imc <35:
    print(f"Usuário está obeso.")
elif imc<40:
    print(f"Usuário está com obesidade nível 2.")
else:
    print(f"Usuário está com obesidade mórbida.")

