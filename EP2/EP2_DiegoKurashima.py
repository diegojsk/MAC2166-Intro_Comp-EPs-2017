"""
  AO PREENCHER ESSE CABEÃ‡ALHO COM O MEU NOME E O MEU NÃšMERO USP,
  DECLARO QUE SOU A ÃšNICA PESSOA AUTORA E RESPONSÃVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÃCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÃ‡Ã•ES
  DESSE EP E, PORTANTO, NÃƒO CONSTITUEM ATO DE DESONESTIDADE ACADÃŠMICA,
  FALTA DE Ã‰TICA OU PLÃGIO.
  DECLARO TAMBÃ‰M QUE SOU A PESSOA RESPONSÃVEL POR TODAS AS CÃ“PIAS
  DESSE PROGRAMA E QUE NÃƒO DISTRIBUÃ OU FACILITEI A
  SUA DISTRIBUIÃ‡ÃƒO. ESTOU CIENTE QUE OS CASOS DE PLÃGIO E
  DESONESTIDADE ACADÃŠMICA SERÃƒO TRATADOS SEGUNDO OS CRITÃ‰RIOS
  DIVULGADOS NA PÃGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃƒO SERÃƒO CORRIGIDOS E,
  AINDA ASSIM, PODERÃƒO SER PUNIDOS POR DESONESTIDADE ACADÃŠMICA.

  Nome : Diego Jun Sato Kurashima
  NUSP : 10274231
  Turma: Turma 9
  Prof.: Denis Deratani Mauá

  ReferÃªncias: Com exceÃ§Ã£o das rotinas fornecidas no enunciado
  e em sala de aula, caso vocÃª tenha utilizado alguma referÃªncia,
  liste-as abaixo para que o seu programa nÃ£o seja considerado
  plÃ¡gio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
#
#   FUNÃ‡Ã•ES FORNECIDAS: NÃƒO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta Ã© a funÃ§Ã£o principal do seu programa. Ela contÃ©m os comandos que
    obtÃªm os parÃ¢metros necessÃ¡rios para criaÃ§Ã£o do jogo (nÃºmero de linhas,
    colunas e cores), e executa o laÃ§o principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÃ‡ÃƒO NÃƒO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lÃª parÃ¢metros do jogo
    num_linhas = int(input("Digite o nÃºmero de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o nÃºmero de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o nÃºmero de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuraÃ§Ã£o inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laÃ§o principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos vÃ¡lidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores sÃ£o deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos entÃ£o deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** VocÃª destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento invÃ¡lido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("VocÃª destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando invÃ¡lido! Tente ajuda para receber uma lista de comandos vÃ¡lidos. ***")
            print ()
    print("*** Fim de Jogo: NÃ£o existem mais movimentos vÃ¡lidos! ***")
    print ("VocÃª destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaÃ§os vazios com novas gemas geradas aleatoriamente.

    As gemas sÃ£o representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]


# ======================================================================
#
#   FUNÃ‡Ã•ES A SEREM IMPLEMENTADAS POR VOCÃŠ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representaÃ§Ã£o do tabuleiro e a preenche com
    espaÃ§os vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(' ')
        matriz.append(linha)   
            
        
    return matriz

def exibir (tabuleiro):
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''

    # identificação das colunas
    for i in range(4):
        print(' ',end='')
    for x in range(len(tabuleiro[0])):
        print(x, end=' ')
    print('')

    # limite superior do tabuleiro
    print(' ', end=' ')
    print('+', end='')
    for x in range(2*len(tabuleiro[0]) + 1):
                   print('-',end='')
    print('+')

    # tabuleiro propriamante, com identificação das linhas
    for y in range(len(tabuleiro)):
        print(y,end=' ')
        print('|',end=' ')
        for x in range(len(tabuleiro[0])):
                       print(tabuleiro[y][x],end=' ')
        print('|')

    # limite inferior do tabuleiro
    print(' ', end=' ')
    print('+', end='')
    for x in range(2*len(tabuleiro[0]) + 1):
                   print('-',end='')
    print('+')





def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posiÃ§Ãµes (linha1, coluna1) e (linha2, coluna2) caso
    seja vÃ¡lida (isto Ã©, gemas sÃ£o adjacentes e geram cadeias), caso contrÃ¡rio
    nÃ£o altera o tabuleiro.

    Retorna `True` se permutaÃ§Ã£o Ã© vÃ¡lida e `False` caso contrÃ¡rio.
    '''
    # checando se são adjacentes lateralmente ou na vertical
    adj_lat=(linha1==linha2 and (coluna1-coluna2==1 or coluna1-coluna2==-1))
    adj_vert=(coluna1==coluna2 and ( linha1-linha2==1 or linha1-linha2==-1))

    # tabela/matriz provisoria para teste, realizando a troca de posições
    tbl_prov=[]
    for linha in (tabuleiro):
        tbl_prov.append(linha[:])
        
    p1=tbl_prov[linha1][coluna1]
    p2=tbl_prov[linha2][coluna2]
    tbl_prov[linha1][coluna1]=p2
    tbl_prov[linha2][coluna2]=p1

    


    # checando se geram cadeias, se são adjacentes
    if ( adj_lat) or( adj_vert):

        # (uso de funções criados pelo autor do programa)
        if identificar_cadeias_horizontais_mod(tbl_prov, linha1, coluna1) or identificar_cadeias_horizontais_mod(tbl_prov, linha2, coluna2) or identificar_cadeias_verticais_mod(tbl_prov, linha1, coluna1) or identificar_cadeias_verticais_mod(tbl_prov, linha2, coluna2):

            # se a tbl_prov for válida, ela será atribuida ao tabuleiro
            for i in range(len(tbl_prov)):
                tabuleiro[i]=tbl_prov[i][:]
                
            return True


    return False
 
    
                   
def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaÃ§os (' ').

    Retorna nÃºmero de gemas eliminadas.
    '''
    num_eliminados = 0

    # tabela/matriz provisoria para identificar as cadeias
    tbl_prov=[]
    for linha in (tabuleiro):
        tbl_prov.append(linha[:])


    # verificando existencia de cadeias e eliminando-as, se existirem
    if identificar_cadeias_horizontais(tbl_prov)!=[]:
        for cadeia in (identificar_cadeias_horizontais(tbl_prov)):
            eliminar_cadeia(tabuleiro,cadeia)
            

    if identificar_cadeias_verticais(tbl_prov)!=[]:
        for cadeia in (identificar_cadeias_verticais(tbl_prov)):
            eliminar_cadeia(tabuleiro,cadeia)
            

    # identificando gemas eliminadas/espaços vazios
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna]==" ":
                num_eliminados+=1

    
        
        
    return num_eliminados

def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia Ã©
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o nÃºmero da linha da cadeia
    - `coluna_i`: o nÃºmero da coluna da gema mais Ã  esquerda (menor) da cadeia
    - `coluna_f`: o nÃºmero da coluna da gema mais Ã  direita (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    cadeias = []
    #checando ,a cada linha, a presença de cadeias
    for linha in range(len(tabuleiro)):

        #variaveis de passagem
        anterior=' '
        coluna_i=-3
        coluna_f=-2
        coluna_i_nova=-1
        tam_seq=0
        tem_cad=False
        fim_seq=False
        
        # procurando cadeias na linha
        for col in range(len(tabuleiro[linha])):
            
            if tabuleiro[linha][col]!= anterior:
                fim_seq=True
                coluna_i=coluna_i_nova
                coluna_i_nova=col
                coluna_f=col-1
                tam_seq=1
            else:
                tam_seq+=1
                fim_seq=False
                if tam_seq >= 3:
                    tem_cad=True

            # caso seja o último termo da linha
            if col==len(tabuleiro[linha])-1:
                fim_seq=True

                # caso seja de cadeia, possivelmente
                if tabuleiro[linha][col]==anterior:
                    coluna_f=col
                    coluna_i=coluna_i_nova
                

            if (tem_cad and fim_seq):
                cadeias.append([linha,coluna_i,linha,coluna_f])
                tem_cad=False

            anterior=tabuleiro[linha][col]
            
                
    return cadeias

def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia Ã©
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o nÃºmero da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o nÃºmero da coluna das gemas da cadeia
    - `linha_f`: o nÃºmero da linha mais inferior (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    cadeias = []
    #checando ,a cada coluna, a presença de cadeias
    for col in range(len(tabuleiro[0])):

        #variaveis de passagem
        anterior=' '
        linha_i=-3
        linha_f=-2
        linha_i_nova=-1
        tam_seq=0
        tem_cad=False
        fim_seq=False
        
        # procurando cadeias na coluna
        for linha in range(len(tabuleiro)):
            
            if tabuleiro[linha][col]!= anterior:
                fim_seq=True
                linha_i=linha_i_nova
                linha_i_nova=linha
                linha_f=linha-1
                tam_seq=1
            else:
                tam_seq+=1
                fim_seq=False
                if tam_seq >= 3:
                    tem_cad=True

            # caso seja o último termo da coluna
            if linha==len(tabuleiro)-1:
                fim_seq=True

                # caso seja de uma possiel cadeia
                if tabuleiro[linha][col]==anterior:
                    linha_f=linha
                    linha_i=linha_i_nova
                

            if (tem_cad and fim_seq):
                cadeias.append([linha_i,col,linha_f,col])
                tem_cad=False

            anterior=tabuleiro[linha][col]
            
                
    
                
    return cadeias

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaÃ§o `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o nÃºmero da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o nÃºmero da coluna da gema mais Ã  esquerda (menor) da cadeia
    - `linha_f`: o nÃºmero da linha mais inferior (maior) da cadeia
    - `coluna_f`: o nÃºmero da coluna da gema mais Ã  direita (maior) da cadeia

    Retorna o nÃºmero de gemas eliminadas.
    '''
    num_eliminados = 0
    
    # para cadeias na horizontal
    if cadeia[0]==cadeia[2]:
        for coluna in range(cadeia[1], (cadeia[3]+1)):
            tabuleiro[cadeia[0]][coluna]=" "
            num_eliminados+=1
            

    
    # para cadeias verticais
    elif cadeia[1]==cadeia[3]:
        for linha in range(cadeia[0], (cadeia[2]+1)):
            tabuleiro[linha][cadeia[1]]=" "
            num_eliminados+=1

    

    return num_eliminados


def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaÃ§os vazios sem nenhuma gema acima.
    '''

    # verificando em cada coluna
    for i in range(len(tabuleiro[0])):
                   deslocar_coluna(tabuleiro,i)


def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaÃ§os vazios.
    '''

    gemas_acima=0
    vazios=0
    gemas_acima_bool=True

    # detectar a distancia de deslocamento
    for k in range(len(tabuleiro)):
        if tabuleiro[k][i]!=" " and gemas_acima_bool==True:
            gemas_acima+=1
        elif tabuleiro[k][i]==" ":
            gemas_acima_bool=False
            vazios+=1


    # deslocamento de fato
    linha=(gemas_acima-1)
    
    while linha>=0:
        tabuleiro[linha+vazios][i]=tabuleiro[linha][i]
        linha-=1

    linha=(vazios-1)
    while linha>=0:
        tabuleiro[linha][i]=" "
        linha-=1
        
        
    
            
        
    

                   
def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos vÃ¡lidos, False caso contrÃ¡rio.
    '''
    
    
    if  obter_dica(tabuleiro) == (-1,-1):
        return False

    
    return True


def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posiÃ§Ã£o (linha, coluna) de uma gema que faz parte de uma
    permutaÃ§Ã£o vÃ¡lida.

    Se nÃ£o houver permutaÃ§Ã£o vÃ¡lida, retorne -1,-1.
    '''
    linha = -1
    coluna = -1

    # tabela/matriz provisoria para teste
    tbl_prov=[]
    for linha in (tabuleiro):
        tbl_prov.append(linha[:])

    
    # testar ,para cada gema, se forma cadeias
    for i in range (len(tabuleiro)):
        for j in range (len(tabuleiro[i])):

            
            # testar posições para trocar
            for troca_i in range(len(tabuleiro)):
                for troca_j in range(len(tabuleiro[0])):

                    # checar se vale a troca/se formam cadeias e são adjacentes
                    if trocar_mod(i,j,troca_i,troca_j,tbl_prov)==True:
                        linha=i
                        coluna=j

                        return linha,coluna

                        

    return -1,-1

# ======================================================================
#
#   FUNÃ‡Ã•ES CRIADAS PELO ALUNO, FORA DO ESQUELETO ORIGINAL
#
# ======================================================================

def identificar_cadeias_horizontais_mod (tabuleiro, linha, coluna):
    ''' (matrix, int, int) -> Bool

    Essa função é uma modificação da função original 'identificar_cadeias_horizontais'

    Retorna um valor booleano True indicando se há cadeias horizontais de 3 ou mais gemas, em relação a uma gema especificado por linha e coluna.
    Cada cadeia Ã© representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o nÃºmero da linha da cadeia
    - `coluna_i`: o nÃºmero da coluna da gema mais Ã  esquerda (menor) da cadeia
    - `coluna_f`: o nÃºmero da coluna da gema mais Ã  direita (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    
    #checando a presença de cadeias
    
    #variaveis de passagem
    anterior=' '
    coluna_i=-3
    coluna_f=-2
    coluna_i_nova=-1
    tam_seq=0
    tem_cad=False
    fim_seq=False
    
        
    # procurando cadeias na linha
    for col in range(len(tabuleiro[linha])):
            
        if tabuleiro[linha][col]!= anterior:
                fim_seq=True
                coluna_i=coluna_i_nova
                coluna_i_nova=col
                coluna_f=col-1
                tam_seq=1
        else:
                tam_seq+=1
                fim_seq=False
                if tam_seq >= 3:
                    tem_cad=True
                    
        if col==(len(tabuleiro[linha])-1):
            coluna_f=col


        if ((tem_cad and (fim_seq or(col==len(tabuleiro[linha])-1)))):
            tem_cad=False
            #deve-se confirmar se seq esta relacionado a gema da entrada
            if(coluna<=coluna_f and coluna>=coluna_i):
                return True
                

        anterior=tabuleiro[linha][col]
            
                
    return False


def identificar_cadeias_verticais_mod (tabuleiro, linha, col):
    ''' (matrix, int, int) -> Bool

    Essa função é uma modificação da função original 'identificar_cadeias_verticais'

    Retorna um valor booleano True se há cadeias verticais de 3 ou mais gemas, em relação a uma gema especificada por linha e col.
    Cada cadeia Ã© representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o nÃºmero da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o nÃºmero da coluna das gemas da cadeia
    - `linha_f`: o nÃºmero da linha mais inferior (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    
    #checando  a presença de cadeias
    
    #variaveis de passagem
    anterior=' '
    linha_i=-3
    linha_f=-2
    linha_i_nova=-1
    tam_seq=0
    tem_cad=False
    fim_seq=False
    
    
    # procurando cadeias na coluna
    for lin in range(len(tabuleiro)):
            
            if tabuleiro[lin][col]!= anterior:
                fim_seq=True
                linha_i=linha_i_nova
                linha_i_nova=lin
                linha_f=lin-1
                tam_seq=1
            else:
                tam_seq+=1
                fim_seq=False
                if tam_seq >= 3:
                    tem_cad=True

            if lin==(len(tabuleiro)-1):
                linha_f=lin
                


            

            if (tem_cad and (fim_seq or lin==len(tabuleiro)-1 )):
                tem_cad=False
                # deve-se confirmar se a cadeia relaciona-se com a gema da entrada
                if (linha<=linha_f and linha>=linha_i):
                    return True
                
            anterior=tabuleiro[lin][col]
            
                
    
                
    return False

def trocar_mod (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Essa função é uma variação da função original "trocar"

    Verifica-se se pode permutar gemas das posiÃ§Ãµes (linha1, coluna1) e (linha2, coluna2) caso
    seja vÃ¡lida (isto Ã©, gemas sÃ£o adjacentes e geram cadeias) 

    NÃ£o altera o tabuleiro.

    Retorna `True` se permutaÃ§Ã£o Ã© vÃ¡lida e `False` caso contrÃ¡rio.
    '''
    # checando se são adjacentes lateralmente ou na vertical
    adj_lat=(linha1==linha2 and (coluna1-coluna2==1 or coluna1-coluna2==-1))
    adj_vert=(coluna1==coluna2 and ( linha1-linha2==1 or linha1-linha2==-1))

    # tabela/matriz provisoria para teste, realizando a troca de posições
    tbl_prov=[]
    for linha in (tabuleiro):
        tbl_prov.append(linha[:])
        
    p1=tbl_prov[linha1][coluna1]
    p2=tbl_prov[linha2][coluna2]
    tbl_prov[linha1][coluna1]=p2
    tbl_prov[linha2][coluna2]=p1

    


    # checando se geram cadeias, se são adjacentes
    if ( adj_lat) or( adj_vert):
        # (uso de funções criados pelo autor do programa)
        if identificar_cadeias_horizontais_mod(tbl_prov, linha1, coluna1) or identificar_cadeias_horizontais_mod(tbl_prov, linha2, coluna2) or identificar_cadeias_verticais_mod(tbl_prov, linha1, coluna1) or identificar_cadeias_verticais_mod(tbl_prov, linha2, coluna2):
            return True


    return False




main()
