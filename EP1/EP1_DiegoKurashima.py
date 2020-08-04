"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :Diego Jun Sato Kurashima
  NUSP :10274231
  Turma:09
  Prof.:Denis Deratani Mauá

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""

# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()
    
    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols   = int(input('Número de colunas do tabuleiro: '))
    x0      = int(input('Posição x inicial da cobrinha : '))
    y0      = int(input('Posição y inicial da cobrinha : '))
    t       = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")
        
    else:

        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1: 
            d = d * 10 + 2
            i = i + 1
        
        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
            
            # lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))
            
            
            
            if direcao != 5:
                
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)
                

    print()        
    print("Tchau!")
    

# ======================================================================

def num_digitos(n):
    """ (int) -> int

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    dg = 0
    #variável do número de dígitos

    while n>0:
        # calculando o número de dígitos por meio de divisões por 10

        n = int(n/10)
        dg = dg + 1
    
    return dg
 
# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    
    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    dp = d
    xatual = x0                   
    yatual = y0
    #coordenadas em análise no teste, iniciando pela cabeça
    dt = 0
    #dígito em análise ( do "d")
    a = 0
    #contador para o teste da posição
    ocupa = False
    #booleano ( se ocupa ou não), por enquanto nao
    
    while a <= (num_digitos(d)) and ocupa == False :
        #teste deve ser feito para o d na entrada

        if x == xatual and y == yatual:
            ocupa = True
            
        
        else :
            dt = dp%10
            #descobrir o número do comando para a cabeça(fazendo a caminho inverso em d !!!)
            #verificando a posição da parte seguinte(seguindo o caminho contrário em d!!!)
            
            if  dt == 1:            
                xatual = xatual + 1
            elif dt == 2:
                xatual = xatual - 1
            elif dt == 3:
                yatual = yatual + 1
            elif dt == 4: 
                yatual = yatual - 1
                
        dp = int(dp/10)
        a = a + 1


    return ocupa
        
# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
         
    """

    # Escreva sua função a seguir
    
    x = 0
    y = 0
    #coordenadas no tabuleiro(inicialmente é (0;0))

    b = 0
    #contador do comando print nas linhas

    while b < (ncols+2):
        #imprimir a parede superior
        
        print("#", end="")
        b = b + 1
    print()

    #abaixo:imprimir o tabuleiro

    #variável (p) usado como variavel do print

    while y < (nlinhas):
        print("#", end="")
        x = 0
        while x < (ncols):
            if (pos_ocupada(nlinhas, ncols, x, y, x0, y0, d)) == False :
                p="."
            else:
                if(x == x0 and y == y0):
                    p="C"
                else:
                    p="*"
            print(p,end="")
            x = x + 1
        print("#")
        y = y + 1
        

    b = 0
    #reinicio do contador

    while b <(ncols+2):
        #imprimir a parede inferior
        
        print("#", end="")
        b = b + 1
    print()
        

# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO COM SI MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida
    
    """
    
    # Escreva sua função a seguir e corrija o valor devolvido no return

    

    xantigo = x0
    yantigo = y0
    
    
    #variáveis de passagem

    #abaixo: novos valores da cabeça
    if   direcao == 1:
            x0 = x0 - 1
    elif direcao == 2:
            x0 = x0 + 1
    elif direcao == 3:
            y0 = y0 - 1
    elif direcao == 4:
            y0 = y0 + 1

    

    if x0 >= ncols or x0 < 0 or y0 >= nlinhas or y0 < 0:
        
        print("COLISÃO COM A PAREDE")
        return xantigo, yantigo, d
    
    elif (pos_ocupada(nlinhas, ncols, x0, y0, xantigo, yantigo, d))==True:
        
        print("COLISÃO COM SI MESMA")
        return xantigo, yantigo, d
    
    else: #movimento valido!
          #calculando o novo d ( por manipulacao algebrica)
        
        c = 0
        pot = 1
        while c <(num_digitos(d)):
            pot = pot*10
            c = c + 1

        dnovo = int((d*10)%pot + direcao)

    

    return x0, y0, dnovo



# ======================================================================
main()     
