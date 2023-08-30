''' Verificar se um número está entre 1 e 10. Caso ele esteja, adicione 5 ao seu valor; caso contrário, dobre o seu valor.
'''

num_x = int(input("Digite um número inteiro: "))

if (num_x >=1 and num_x <10):
    num_x = num_x + 5
else:
    num_x = num_x * 2

print(f"O novo valor de x é {num_x}")
