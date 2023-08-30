'''
Dado uma temperatura, verifique e mostre:
- temp <= 20: frio
- 20 < temp <= 26 : moderado
- temp > 26: quente
'''

temp = float(input("Informe o valor da temperatura: "))

if (temp <= 20):
    print("Fria")
elif (temp <= 26):
    print("Moderada")
else:
    print("Quente")

