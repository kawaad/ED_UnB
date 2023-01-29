'''
aBSTada!
Magá era uma cã feliz, gostava de passear no parque e brincar com árvores binárias. Era tanta alegria ao lidar com esta estrutura de dados que ela até se perdia nas operações. Isso causava desgosto à Conja, que tinha convicção da diligência de Magá ao lidar com suas obrigações. Ajude Magá a ser feliz! Crie um programa que implementa uma Árvore Binária de Busca e aceita os comandos da Conja.

São 5 comandos simples:
n: insere o valor inteiro 𝑛
 na árvore;
in: apresenta os elementos inseridos na forma infixa;
pre: apresenta os elementos inseridos na forma prefixa;
pos: apresenta os elementos inseridos na forma pósfixa; e
quack: interrompe o processamento (hora do banho de banheira).
Entrada
A entrada contém uma quantidade indefinida de comandos a serem executados sobre sua árvore (inicialmente vazia). O final da entrada é sempre definido pelo comando quack.

Saída
Para cada comando de apresentar os elementos, liste-os em uma linha, na ordem definida e separados por espaço.

Exemplos de entrada:
4
2
1
3
6
7
5
in
pre
pos
quack

Gera a saída:
1 2 3 4 5 6 7
4 2 1 3 6 5 7
1 3 2 5 7 6 4

A entrada:
1
7
2
8
9
3
0
4
5
6
in
in
in
pos
pre
in
in
quack

Gera a saída:
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 6 5 4 3 2 9 8 7 1
1 0 7 2 3 4 5 6 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        novo_no = No(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if valor < atual.valor:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                    else:
                        atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    else:
                        atual = atual.direita
    
    def infixa(self, no):
        if no is not None:
            self.infixa(no.esquerda)
            print(no.valor, end=' ')
            self.infixa(no.direita)
    
    def prefixa(self, no):
        if no is not None:
            print(no.valor, end=' ')
            self.prefixa(no.esquerda)
            self.prefixa(no.direita)
    
    def posfixa(self, no):
        if no is not None:
            self.posfixa(no.esquerda)
            self.posfixa(no.direita)
            print(no.valor, end=' ')

arvore = ArvoreBinaria()
while True:
    entrada = input()
    if entrada == 'quack':
        break
    try:
        entrada = int(entrada)
        arvore.inserir(entrada)
    except ValueError:
        if entrada == 'in':
            arvore.infixa(arvore.raiz)
            print()
        elif entrada == 'pre':
            arvore.prefixa(arvore.raiz)
            print()
        elif entrada == 'pos':
            arvore.posfixa(arvore.raiz)
            print()
