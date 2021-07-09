# Para melhor experiência, recomeda-se utilizar o IDLE em modo janela (com 80
# caracteres de largura).

# Bool.py é um quiz sobre Python, onde o jogador deve responder à 10 perguntas
# e acertar pelo menos 60% para avançar de nível.

# PARTICIPANTES: André Cunha Quintiliano de Camargo      TIA: 32073801
#                André Philipe Andriotti de Moraes            32013965
#                Gabriel Kazuiti Aiura                        32047231

import random
from time import sleep

#EASY DATABASE
easyQuest = ['''>>> Qual é o resultado da operação:
        	18 / 3 ** 2
a) 2
b) 6
c) 12
d) 24
e) 36''',
'''>>> O que está faltando no código a seguir:
        if nota >= 7.5
            print(“Aprovado”)
        else:
            print(“Reprovado”)
a) Indentação
b) Aspas
c) Condição
d) Parênteses
e) Dois pontos''',
'''>>> Python, Java e C++ são exemplos de:
a) Aplicativos
b) Linguagens de programação
c) Estruturas condicionais
d) Algoritmos
e) Operadores lógicos''',
'''>>> São exemplos de estrutura de repetição:
a) if, elif e else
b) and, or e not
c) for e while
d) print e input
e) sort e reverse''',
'''>>> Para efetuar questões matemáticas complexas no Python, é comum utilizar a
biblioteca:
a) random
b) math
c) statistics
d) re
e) pygame''',
'''>>> Descubra o erro no código a seguir:
        Idade = int(input(‘Digite sua idade: ’))
        if idade < 18:
            print(‘Você não está elegível para se alistar.’)
        else: print(‘Para continuar com o alistamento, conclua o reCaptcha...’)
a) Indentação
b) O comando “print” está na mesma linha do comando “else”
c) Parênteses
d) “idade” não definido
e) Sintaxe''',
'''>>> Para definir uma função utilizamos o comando:
a) def
b) while
c) list
d) print
e) for''',
'''>>> O comando utilizado para a entrada de dados é:
a) for
b) while
c) if / else
d) print
e) input''',
'''>>> O comando utilizado para a saída de dados é:
a) for
b) while
c) if / else
d) print
e) input''',
'''>>> Encontre o comando equivalente ao código a seguir:
        num1 = num1 - 1
a) num1 += 1
b) num1 = -1
c) num2 -= 1
d) num1 -= 1
e) num1 = num1/-1''',
'''>>> Qual operador atribui um valor a uma variável?
a) >=
b) <=
c) +=
d) ==
e) =''',
'''>>> Qual a função dessa parte do programa a seguir:
        if numX == 100:
            print(‘True’)
a) Verificar se numX é menor que 100
b) Verificar se numX é maior que 100
c) Atribuir ao numX o valor 100
d) Verificar se numX é equivalente a 100
e) Imprimir “True” ao somar 100 ao numX''',
'''>>> Qual comando deve ser utilizado para adicionar um item no final da lista 
“listaX”? 
a) listaX.append()
b) listaX.index()
c) listaX.reverse()
d) listaX.pop()
e) listaX.sort()''',
'''>>> Qual operador verifica se duas variáveis possuem o mesmo valor?
a) >=
b) <=
c) +=
d) ==
e) =''',
'''>>> Qual a finalidade do código:
        import random
        randomizer = random.randint(1,10)
a) Atribuir o valor 10 à variável “randomizer”
b) Atribuir o valor 1 à variável “randomizer”
c) Imprimir todos os valores entre 1 e 10
d) Atribuir um valor aleatório entre 1 e 10 à variável “randomizer”
e) Efetuar a média aritmética entre 1 e 10''']

easyResp = ['''Primeiro, deve-se calcular a potência (3**2 = 9) e então, a divisão (18/9 = 2).''',
'''Após o “if”, é necessário separá-lo da condição por meio de dois pontos.''',
'''Python, Java e C++ são linguagens de programação.''',
'''For e While, ambos são estruturas que, dada suas condições, repetem o mesmo 
comando até que sejam satisfeitas.''',
'''A biblioteca math traz uma diversidade de funções matemáticas possíveis a se 
fazer.''',
'''A variável definida como int é “Idade”, não “idade”. Note que o modo como a 
variável é nomeada pode acarretar em problemas futuros, portanto, lembre-se 
dos mínimos detalhes, até mesmo se a letra é maiúscula ou minúscula.''',
'''O comando def é utilizado para definir funções, geralmente utilizados no início
do código.''',
'''O comando input serve para realizar a entrada de dados pelo usuário.''',
'''O comando print serve para o programador exibir informações do programa ao
usuário.''',
'''É possível simplificar a operação em questão ao utilizar o sinal de menos
seguido do igual.''',
'''Para atribuir um valor a uma variável utilizamos o comando “=”, pois este
atribuirá o valor digitado à variável.''',
'''Ao utilizarmos o comando “==”, este compara o valor da variável ao valor
digitado, assim, podemos afirmar que a finalidade deste código é verificar
se numX é equivalente a 100.''',
'''O comando “.append()” é programado para adicionar itens ainda não inclusos no
final da lista.''',
'''Ao utilizar dois sinais de igual juntos, a operação deixa de ser uma atribuição
de valores e passa a ser comparação de valores.''',
'''Ao importar a biblioteca random, você consegue randomizar um valor de um
intervalo a uma variável por meio do comando “randint()”. ''']

#MEDIUM DATABASE
mediumQuest = ['''>>> AND, OR e NOT são exemplos de:
a) Linguagens de programação
b) Operadores lógicos
c) Operadores relacionais
d) Tipos de variável
e) Estruturas de repetição''',
'''>>> ==, != e >= são exemplos de:
a) Linguagens de programação
b) Operadores lógicos
c) Operadores relacionais
d) Tipos de variável
e) Estruturas de repetição''',
'''>>> Utilizando o módulo “math”, calcule 4**3.
a) math.sin(4)
b) math.cos(3)
c) math.pow(3, 4)
d) math.pow(4, 3)
e) math.floor(4)''',
'''>>> O que a função matemática “math.ceil()” faz?
a) Exclui tudo a partir do ponto flutuante
b) Calcula a raiz quadrada
c) Calcula o seno do valor
d) Arredonda para baixo
e) Arredonda para cima''',
'''>>> Para gerar números aleatórios no Python, é comum utilizar a biblioteca:
a) random
b) math
c) statistics
d) re
e) pygame''',
'''>>> O que a função matemática “math.trunc()” faz?
a) Exclui tudo a partir do ponto flutuante
b) Calcula a raiz quadrada
c) Calcula o seno do valor
d) Arredonda para baixo
e) Arredonda para cima''',
'''>>> Qual a principal função do código a seguir:
        num1 = int(input(‘Digite um número’)
        while num1 < 100:
            num1 += 1	
            print(num1)
a) Receber o valor de num1
b) Printar o num1
c) Somar 1 a números abaixo de 100
d) Subtrair 1 do número digitado pelo usuário
e) Igualar o num1 à 1''',
'''>>> Marque a alternativa inválida:
a) idade = 18
b) 18idade = 18
c) idade18 = 18
d) _idade = 18
e) i_da_de = 18''',
'''>>> Qual a linguagem usada em um Arduino?
a) C
b) C++
c) Python
d) Javascript
e) C#''',
'''>>> Para utilizar uma variável definida em uma função em outra parte do código,
utiliza-se o comando:
a) def
b) random.randint
c) global
d) for
e) import''',
'''>>> MESES_DO_ANO = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    Esta parte de código é um exemplo de:
a) Tupla
b) Dicionário
c) Laço
d) Lista
e) Condição''',
'''>>> O comando “break” é utilizado para:
a) Interromper uma estrutura de repetição
b) Encerrar o programa
c) Imprime um valor
d) Parar de imprimir valores
e) Desligar o computador''',
'''>>> Na lista: num = [1,2,3,4,5], o número que ocupa o índice um é o:
a) 1
b) 2
c) 3
d) 4
e) 5''',
'''>>> Qual a finalidade do código a seguir:
        numX = int(random.randrange(1,5))
        numY = int(random.randrange(1,5))
        if (numX + numY)%2 == 0
            print(‘True’)
a) Descobrir se a divisão dos números é um número ímpar
b) Multiplicar a soma dos números por 2
c) Dividir a soma dos números por 2
d) Descobrir se a soma dos números é um número par
e) Descobrir quanto é 2% da soma dos números''',
'''>>> Para calcular a quantidade de elementos de uma lista, pode-se usar a função:
a) len()
b) count()
c) index()
d) append()
e) pop()''',]

mediumResp = ['''AND, OR e NOT são considerados operadores lógicos, diferentemente de operadores
relacionais como == e !=.''',
'''== verifica a igualdade do valor de duas variáveis, != compara se o valor de 
duas variáveis são diferentes e >= compara se uma variável é maior ou igual a
outra.''',
'''O comando “math.pow()” foi programado para que o primeiro número digitado seja a
base e o segundo número, o expoente, sendo assim, este é o comando adequado para
tal questão.''',
'''O comando “math.ceil” foi programado para que números decimais sejam aproximados
a números maiores para se tornarem números inteiros.''',
'''A biblioteca random possibilita a geração de números aleatórios, dentre outras
funções de aleatoriedade.''',
'''A função math.trunc() retorna a parte inteira de x como valor inteiro.''',
'''O comando “num1 += 1” está sendo repetido até que a condição da estrutura while 
esteja satisfeita, tal condição faz com que qualquer número digitado que esteja
abaixo de 100, eventualmente se torne 100, após ser somado a 1 consecutivamente.''',
'''Quando vamos dar nomes a variáveis, nunca podemos começar com números.''',
'''O Arduino utiliza a linguagem C++, com pequenas alterações.''',
'''O comando global torna uma variável definida em uma função (variável local)
acessível em outra parte do código (variável global).''',
'''A estrutura Nome_da_lista = [] representa uma lista e atribui elementos à ela,
no caso, os meses do ano.''',
'''O comando break serve para interromper uma estrutura de repetição (como while e
for) para não ficarmos presos em um loop infinito, por exemplo.''',
'''Nas listas, o primeiro elemento recebe o índice = 0, o segundo, índice = 1 e
assim por diante, ou seja, nessa lista o número um ocupa o índice 0 até chegar
no cinco, que ocupa o índice 4.''',
'''Ao utilizar o operador de módulo (%), obtemos o resto da divisão, assim, ao 
dividirmos por 2 e comparar o resultado com 0, é possível verificar se o número
é par ou não.''',
'''A função len() calcula a quantidade de elementos em uma lista.''',]

#HARD DATABASE
hardQuest = ['''>>> O que é uma variável local?
a) Uma variável sem tipo definido
b) Uma variável do tipo booleana
c) Uma variável criada dentro de uma função
d) Uma variável criada dentro de um laço
e) Uma variável acumuladora''',
'''>>> Para remover o último elemento da lista “compras”, deve-se utilizar o
seguinte comando:
a) compras.append()
b) compras.index()
c) compras.reverse()
d) compras.pop()
e) compras.sort()''',
'''>>> Quem é o criador da linguagem Python?
a) Guido Van Rossum
b) Alan Turing
c) Andrew Kazuiti Aiura
d) Philipe Quintiliano
e) Christian B. Python''',
'''>>> O nome “Python”, em sua origem, teve por referência:
a) Uma cidade
b) Um sobrenome
c) Um famoso canadense
d) Uma joia rara
e) Um programa de TV''',
'''>>> A linguagem de programação Python teve sua estréia em que ano?
a)1992
b)2001 
c)1989
d)1985
e)1999''',
'''>>> A linguagem Python é considerada uma:
a) Linguagem antiga
b) Linguagem de alto nível
c) Linguagem de baixo nível
d) Linguagem de máquina
e) Linguagem pobre''',
'''>>> Existem quantos tipos de bibliotecas em python?
a) Em torno de 1000
b) Em torno de 5000
c) Em torno de 20000
d) Em torno de 70000
e) Em torno de 125000''',
'''>>> O que está errado no código a seguir?
        def valor1():
        while True:
        c = int(input('Primeiro Valor: '))
        return c
        print('Inválido!')
a) Indentação
b) Comando def não existe
c) Falta de parênteses no 'inválido'
d) Em def valor 1(), os parênteses não podem estar vazios
e) O código está correto''',
'''>>> O que significa a sigla IDLE no Python?
a) Interactive Development and Learning Environment
b) Integrated Development and Loading Environment
c) Interactive Development and Loading Environment
d) Integrated Development and Learning Environment
e) Interpreted Development and Learning Environment''',
'''>>> Qual a diferença entre listas e tuplas?
a) Listas são variáveis compostas - tuplas são variáveis simples
b) Listas são representadas por () - tuplas são representadas por []
c) Listas são mutáveis - tuplas são imutáveis
d) Listas aceitam vários tipos de variáveis - tuplas aceitam apenas um
e) Não há diferença entre listas e tuplas''', 
'''>>> A estrutura representada por {} e que possui índices literais
personalizáveis é:
a) Laço
b) Dicionário
c) Lista
d) Tupla
e) Variável''',
'''>>> Uma biblioteca geralmente utilizada para desenvolver jogos no Python é:
a) pygame
b) random
c) pillow
d) devGames
e) math''',
'''>>> Qual a função do comando strip() no seguinte programa:
	      nome = input('Nome: ').strip()
a) Divide a string em palavras e forma uma lista
b) Transformar todos os caracteres em letra maiúscula
c) Transformar todos os caracteres em letra minúscula
d) Transformar o primeiro caracter da frase em maiúscula
e) Remover os espaços do começo e final da string''',
'''>>> Qual comando deve ser utilizado para atribuir “Regiane” à variável “nome”:
	      fato = “Regiane melhor professora”
	      nome = ____________
a) fato[1:6]
b) fato[0:6]
c) fato[0:7]
d) fato[1:7]
e) fato[1:8]''',
'''>>> Qual a função do comando split() no seguinte programa:
	      nome = input('Nome: ').split()
a) Divide a string em palavras e forma uma lista
b) Transformar todos os caracteres em letra maiúscula
c) Transformar todos os caracteres em letra minúscula
d) Transformar o primeiro caracter da frase em maiúscula
e) Remover os espaços do começo e final da string''',]

hardResp = ['''Uma variável local é definida em uma função, mas não poderá ser acessada por
outras partes do código a não ser que seja definida como uma variável global.''',
'''O comando “.pop()”, em listas, foi programado para excluir o último item da
lista se os colchetes estiverem vazios.''',
'''O matemático e programador Guido Van Rossum é o criador da linguagem Python.''',
'''O nome “Python” faz referência a um programa de comédia chamado Monty Python´s
Flying Circus.''',
'''Python é uma linguagem de programação desenvolvida no Centro de Matemática e
Tecnologia da Informação, na Holanda, em 1989.''',
'''Python é uma linguagem considerada de alto nível e utilizada em muitos sites
famosos e aplicativos, como Youtube e Spotify.''',
'''Em Python, existem aproximadamente 125000 bibliotecas.''',
'''Ao utilizar a estrutura while, deve-se tomar cuidado com a indentação para que
o programa saiba o que está dentro do while.''',
'''A sigla IDLE significa Integrated Development and Learning Environment, que
traduzido é o Ambiente Integrado de Desenvolvimento e Aprendizagem.''',
'''A diferença entre listas e tuplas deve-se ao fato de que listas podem ser
modificadas, por exemplo, utilizando o comando “.sort()”, já as tuplas não.''',
'''A estrutura representada por {} e que possui índices literais personalizáveis
se chama dicionário.''',
'''A biblioteca “pygame” possui comandos específicos para facilitar o processo de
desenvolvimento de jogos.''',
'''O comando “.strip()” remove qualquer espaço antes e depois de uma variável.''',
'''Para atribuir parte de uma string a uma variável, deve ser feito um fatiamento
onde o intervalo se dá por [x, y], os quais x = primeiro índice e y = último
índice - 1.''',
'''A função split() divide a string em palavras, formando uma lista, onde cada
palavra equivale a um elemento.''']

finalGab = [['a','e','b','c','b','d','a','e','d','d','e','d','a','d','d'],
            ['b','c','d','e','a','a','c','b','b','c','d','a','b','d','a'],
            ['c','d','a','e','c','b','e','a','d','c','b','a','e','c','a']]
userGab = [[], [], []]

#MENU
def menu():

  sleep(1)
  print('=' * 80)
  sleep(1)
  print('''
                                    Welcome to                
         _______     ________    ________    ___        
        |   _   |   |        |  |        |  |   |        
        |  |_|  |   |   __   |  |   __   |  |   |        
        |       |   |  |  |  |  |  |  |  |  |   |        
        |   __   |  |  |  |  |  |  |  |  |  |   |             ____   _   _
        |  |__|  |  |  |__|  |  |  |__|  |  |   |____        |    | | | | |
        |        |  |        |  |        |  |        |   _   | [] | | |_| |
        |________|  |________|  |________|  |________|  |_|  |  __| |___  |
                                                             | |     ___| |
                                                             |_|    |_____|
  ''')
  sleep(2)
  global user
  user = input('>>> Digite seu nome: ')
  sleep(1)
  print('''\n>>> REGRAS:
  - Para passar de nível, alcance 60% das questões.
  - Escolha apenas uma alternativa por vez.
  - Não envie respostas vazias.
  - Divirta-se!''')
  sleep(4)

ordem = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
random.shuffle(ordem)
ordem = ordem[0:10]

#EXIBIR PERGUNTA
def exibirQuest(listQuest, dif, listResp):
  
  global acertos, ptDif
  acertos = 0
  for o in ordem:
    sleep(1)
    print()
    print('=' * 80)
    sleep(1)
    if ordem.index(o) == 0:
        if dif == 0:
          print(f'\n{"EASY":^80}')
          ptDif = 10
        elif dif == 1:
          print(f'\n{"MEDIUM":^80}')
          ptDif = 30
        else:
          print(f'\n{"HARD":^80}')
          ptDif = 50
    print()
    print(listQuest[o])
    resp = input('\n>>> R: ').strip().lower()
    while resp not in 'abcde':
      resp = input('>>> R: ').strip().lower()
    userGab[dif].append(resp)
    print()
    print('=' * 80)
    sleep(1)

    if resp == finalGab[dif][o]:
      acertos += 1
      print(f'''
                     ________   ______    __   __   ______  
                    |__    __| |      |  |  | |  | |   ___|
                       |  |    |  [] _|  |  | |  | |  |__
                       |  |    |  __ \   |  | |  | |   __| 
                       |  |    | |  \ \  |  |_|  | |  |___
                       |__|    |_|   \_\ |_______| |______|
                                                            +{ptDif} pts''')
    else:
      print('''  
                  _______   _______   __       ______   ______
                 |   ____| |       | |  |     |   ___| |   ___|
                 |  |___   |  [ ]  | |  |     |  |___  |  |__
                 |   ___|  |   _   | |  |     |___   | |   __|
                 |  |      |  | |  | |  |___   ___|  | |  |___
                 |__|      |__| |__| |______| |______| |______|
      ''')
      print(f'{f"Resposta correta: {finalGab[dif][o]}":^80}\n')
      print(listResp[o])


#MAIN
def main():

  dif = 0
  ptFinal = 0
  menu()

  while dif <= 2:
    if dif == 0:
      exibirQuest(easyQuest, dif, easyResp)
    elif dif == 1:
      exibirQuest(mediumQuest, dif, mediumResp)
    elif dif == 2:
      exibirQuest(hardQuest, dif, hardResp)

    ptFinal += (acertos * ptDif)
    print()
    print('=' * 80)
    sleep(2)
    
    if acertos >= 6 and dif != 2:
      print(f'\nParabéns, {user}! Você desbloqueou o próximo nível!')
      r = input('Deseja continuar? [S/N] ').strip().lower()
      while r not in 'sn':
        r = input('Deseja continuar? [S/N] ').strip().lower()
      if r == 's':
        dif += 1
      else:
        print('\nOk! Encerrando...')
        break
    
    elif acertos >= 6 and dif == 2:
      print('''
          __   __   __   ______   ________   _______   ______    __   __
         |  | |  | |  | |   ___| |__    __| |   _   | |      |  |  | |  |
         |  | |  | |  | |  |        |  |    |  | |  | |  [] _|  |  |_|  |
         |  |_|  | |  | |  |        |  |    |  | |  | |  __ \   |____   |
         |       | |  | |  |___     |  |    |  |_|  | | |  \ \   ____|  |
          \_____/  |__| |______|    |__|    |_______| |_|   \_\ |_______|
      ''')
      porcent = (ptFinal/900) * 100
      sleep(1)
      print(f'\n{f"Desempenho: {porcent:.1f}%":^80}')
      sleep(1)
      if 60 <= porcent < 75:
        print('''\nCONGRATS! Você conseguiu concluir o quiz, todavia seus conhecimentos a respeito
de Python podem ser aprimorados.''')
      elif 75 <= porcent < 90:
        print('''\nGOOD JOB! Você conseguiu concluir o quiz, apesar de você possuir um conhecimento
claro a respeito de Python, há alguns aspectos a serem melhorados.''')
      else:
        print('''\nAMAZING! Você conseguiu concluir o quiz com E X C E L Ê N C I A, você foi capaz
de superar nosso jogo com precisão e diligência! Nós o nomeamos GOD.py''') 
      
      sleep(2)
      break
    
    else:
      print('''
            ______     ______   _______   ______   _______   ________
           |  __  \   |   ___| |   ____| |   ___| |       | |__    __|
           | |  \  |  |  |__   |  |___   |  |__   |  [ ]  |    |  |
           | |   | |  |   __|  |   __/   |   __|  |   _   |    |  |
           | |__/  |  |  |___  |  |      |  |___  |  | |  |    |  |
           |______/   |______| |__|      |______| |__| |__|    |__|
''')
      sleep(1)
      print(f'\nYOU LOSE, {user}! Você não atingiu 60% das questões...')
      sleep(1)
      print("DON'T GIVE UP, tente novamente!")
      sleep(2)
      break

main()
