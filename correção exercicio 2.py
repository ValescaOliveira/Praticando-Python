'''
Calcule e mostre a média aritmética tendo como base 4 avaliações (AV1, AV2, AV3 E AV4).
'''

AV1 = float(input("Digite a nota da AV1 "))
AV2 = float(input("Digite a nota da AV2 "))
AV3 = float(input("Digite a nota da AV3 "))
AV4 = float(input("Digite a nota da AV4 "))

media = ( AV1 + AV2 + AV3 + AV4)/4

print(f"A média das avaliações é {media:1f}")
