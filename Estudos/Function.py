def calcular_salario(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <=40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = (40 * taxa) + (h_excd * 1.5 * taxa)
    return salario

str_horas = input("Digite a quantidade de horas trabalhadas: ")
str_taxa = input("Digite a taxa: ")
salario_calculado = calcular_salario(str_horas,str_taxa)
print('O salário calculado é: R$', salario_calculado)