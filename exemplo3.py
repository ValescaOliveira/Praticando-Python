'''
Verificar e mostrar se um número inteiro é positivo, negativo ou neutro.
'''

# 3 ou mais situações: if...elif...else

num = int(input("Digite um número inteiro: "))

if (num > 0):
    print("O número é positivo")
elif (num < 0):
    print("O número é negativo")
else:
    print("O número é neutro")
