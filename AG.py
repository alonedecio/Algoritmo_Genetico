import random
from random import randint


class AlgoritmoGeneticoMochila():
    """
    Algoritmo genético para resolver o problema da mochila.
    """
    def __init__(self, pesos, valores, capacidade, tam_populacao, taxa_mutacao, taxa_crossover, num_geracoes, penalidade_por_excesso, metodo_selecao='torneio'):
        """
        Inicializa todos os atributos da instância.
        """
        self.pesos = pesos
        self.valores = valores
        self.capacidade = capacidade
        self.tam_populacao = tam_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.num_geracoes = num_geracoes
        self.num_bits = len(pesos)
        self.metodo_selecao = metodo_selecao
        self.penalidade_por_excesso = penalidade_por_excesso
        self._criar_populacao()

    def _criar_populacao(self):
        """
        Gera uma população inicial de soluções para o problema da mochila.
        """
        self.populacao = [[randint(0, 1) for _ in range(self.num_bits)] for _ in range(self.tam_populacao)]

    def _funcao_objetivo(self, individuo):
        """
        Calcula o valor total dos itens na mochila e penaliza soluções que excedem a capacidade.
        """
        peso = sum(p * i for p, i in zip(self.pesos, individuo))
        valor = sum(v * i for v, i in zip(self.valores, individuo))
        
        if peso > self.capacidade:
            # Aplica uma penalidade proporcional ao excesso de peso
            excesso = peso - self.capacidade
            return valor - (excesso * self.penalidade_por_excesso)  # penalidade_por_excesso é um valor que você deve definir
        else:
            return valor

    def avaliar(self):
        """
        Avalia a população atual, calculando a adequação de cada indivíduo.
        """
        self.avaliacao = [self._funcao_objetivo(individuo) for individuo in self.populacao]

    def selecionar(self):
        """
        Define qual metodo de seleção vamos usar.
        """
        if self.metodo_selecao == 'torneio':
            return self._selecionar_torneio()
        elif self.metodo_selecao == 'roleta':
            return self._selecionar_roleta()
        else:
            raise ValueError("Esse metodo de seleção não existe ou não foi encontrado.")

    def _selecionar_torneio(self):
        """
        Seleciona pais para reprodução usando o método de seleção por torneio.
        """
        torneio = [randint(0, self.tam_populacao - 1) for _ in range(2)]
        competidor1 = torneio[0]
        competidor2 = torneio[1]
        if self.avaliacao[competidor1] > self.avaliacao[competidor2]:
            return self.populacao[competidor1]
        else:
            return self.populacao[competidor2]
        
    def _selecionar_roleta(self):
        """
        Seleciona pais para reprodução usando o método de seleção por roleta.
        """
        # Calcula a aptidão total da população
        aptidao_total = sum(self.avaliacao)
        
        # Calcula a probabilidade de seleção para cada indivíduo baseada em sua aptidão
        probabilidade_selecao = [aptidao / aptidao_total for aptidao in self.avaliacao]
        
        # Seleciona um indivíduo baseado na probabilidade de seleção
        selecionado = random.choices(self.populacao, weights=probabilidade_selecao, k=1)[0]
        
        return selecionado

    def crossover(self, pai, mae):
        """
        Realiza o crossover entre dois pais para gerar dois filhos.
        """
        if random.random() < self.taxa_crossover:
            ponto_de_corte = randint(1, self.num_bits - 1)
            filho_1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
            filho_2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
        else:
            filho_1, filho_2 = pai[:], mae[:]
        return filho_1, filho_2

    def mutar(self, individuo):
        """
        Aplica uma mutação aleatória a um indivíduo.
        """
        for i in range(self.num_bits):
            if random.random() < self.taxa_mutacao:
                individuo[i] = 1 - individuo[i]

    def encontrar_melhor_solucao(self):
        """
        Identifica a melhor solução na população atual.
        """
        melhor_avaliacao = max(self.avaliacao)
        melhor_indice = self.avaliacao.index(melhor_avaliacao)
        return self.populacao[melhor_indice], melhor_avaliacao

    def executar(self):
        """
        Executa o algoritmo genético.
        """
        for _ in range(self.num_geracoes):
            nova_populacao = []
            self.avaliar()
            for _ in range(self.tam_populacao // 2):
                pai = self.selecionar()
                mae = self.selecionar()
                filho_1, filho_2 = self.crossover(pai, mae)
                self.mutar(filho_1)
                self.mutar(filho_2)
                nova_populacao.extend([filho_1, filho_2])
            self.populacao = nova_populacao
        
        melhor_solucao, melhor_avaliacao = self.encontrar_melhor_solucao()
        
        # Calcula o peso total da melhor solução
        peso_total_melhor_solucao = sum(peso * escolha for peso, escolha in zip(self.pesos, melhor_solucao))
        
        print("Melhor solução:", melhor_solucao)
        print("Valor:", melhor_avaliacao)
        # Adiciona um print para mostrar o peso total da melhor solução
        print("Peso Total na Mochila:", peso_total_melhor_solucao)
