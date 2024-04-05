# Algoritmo Genético para o Problema da Mochila

Este repositório contém a implementação de um algoritmo genético projetado para resolver o clássico Problema da Mochila. O objetivo é maximizar o valor total dos itens incluídos na mochila, sem exceder sua capacidade de peso.

## Características

- Implementação em Python.
- Suporte a dois métodos de seleção: Torneio e Roleta.
- Configurações personalizáveis, incluindo taxa de mutação, taxa de crossover, tamanho da população e número de gerações.
- Penalização para soluções que excedem a capacidade da mochila.

## Pré-requisitos

- Python 3.x

## Como Usar

1. Clone o repositório para sua máquina local.
2. Customize os parâmetros no script conforme necessário, incluindo os pesos e valores dos itens, a capacidade da mochila, e outros parâmetros do algoritmo genético.
3. Execute o script para ver a solução do algoritmo para o problema da mochila.

## Exemplo de Uso

```python
pesos = [6, 3, 1, 7, 4, 2, 5]
valores = [2, 7, 3, 4, 5, 2, 6]
capacidade = 13
tamanho_populacao = 30
taxa_mutacao = 0.1
taxa_crossover = 0.9
num_geracoes = 400
penalidade_erro = 5

ag = AlgoritmoGeneticoMochila(pesos, valores, capacidade, tamanho_populacao, taxa_mutacao, taxa_crossover, num_geracoes, penalidade_erro, metodo_selecao='torneio')
ag.executar()
