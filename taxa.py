valor_custo = float(input('Digite o valor do custo do sue produto: \n')) # Entrar com valor de custo
valor_taxa = float(valor_custo * 0.6) # Calcular taxa
print('VALOR DA TAXA: ',valor_taxa , '\n')
valor_composto = float(valor_custo) + float(valor_taxa) # Somar os valores
print('O seu produto custará: ', valor_composto)
