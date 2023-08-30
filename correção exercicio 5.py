'''
Tendo como base o salário de um funcionário, faça o acréscimo de 20% sobre seu valor e exiba-o. DICA: para fazer o acréscimo, multiplique o valor do salário por 1,20.
'''

salario = float(input("Digite o valor do salário: "))

salario_acrescimo = salario * 1.20

print(f"O salário com acrescimo é {salario_acrescimo: 2.f}")
