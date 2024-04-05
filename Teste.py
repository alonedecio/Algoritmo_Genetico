# Importa a classe AlgoritmoGeneticoMochila do módulo AG
from AG import AlgoritmoGeneticoMochila

# Definindo os dados para o teste
pesos = [6, 3, 1, 7, 4, 2, 5]
valores = [2, 7, 3, 4, 5, 2, 6]
capacidade = 13
tamanho_populacao = 30
taxa_mutacao = 0.1
taxa_crossover = 0.9
num_geracoes = 400
penalidade_erro = 5

# Instanciando o algoritmo genético para o problema da mochila [ pesos, valores, capacidade, tamanho da população, ]
ag = AlgoritmoGeneticoMochila(pesos, valores, capacidade, tamanho_populacao, taxa_mutacao, taxa_crossover, num_geracoes, penalidade_erro, metodo_selecao='torneio')

# Executa o algoritmo genético
ag.executar()
