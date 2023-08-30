'''
Sabendo o peso e a altura de uma pessoa, calcule o IMC (índice de massa corpórea) por meio da fórmula: IMC = peso/(altura x altura).
'''

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc= peso / (altura**2) # imc = peso / (altura * altura)

print(f"O valor do IMC é {imc:.2f}")


