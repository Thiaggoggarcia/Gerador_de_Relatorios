import datetime

## Intrução de uso
## Necessário ter um GDAT para entrada dos dados
## No GDAT deve conter os dados a partir do TREL

### Inicio do programa ###
print("""
###############################################################
###### PROGRAMA PARA GERAR GDAT NA CADÊNCIA DE 1 SEGUNDO ######
############################################################### """)

# Nome do arquivo de entrada e de saída
arquivo_entrada = input("Nome do arquivo base: ")
arquivo_saida = input("Nome do arquivo de saida: ")
veiculo = input("Numero do veiculo: ")

data = datetime.date.today()
arquivo_entrada = arquivo_entrada
arquivo_saida = arquivo_saida
# Verifica a quantidade de linhas do arquivo de entrada
contador_linhas = 0

cabecalho ="""
+---------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                           |
|                                           CLA - Centro de Lancamento de Alcantara                                         |
|                                                Relatorio Tempo Real Bruto                                                 |
|                                                                                                                           |
|                                                                                                                           |
|  Resultado: Atlas-CLA                   Operacao:{operacao:<40}           Data: {data}      |
|                                                                                                                           |
|  Veiculo:   {veiculo:<8}                    N.Ensaio:  1                                                             Alvo: 0  |
|                                                                                                                           |
+---------------------+------------+---------------------------------------------+--------+-----------------------------+---+
|                     |            |                                             |        |                             |   |
|     Sincronismo     |Estado Radar|              Referencial Radar              | Banda  |      Referencial Rampa      |   |
|                     |            |                                             |        |                             |   |
+------------+--------+-+-+-+-+-+--+--------+--------+---------+--------+--------+--+--+--+---------+---------+---------+---+
|            |        | | | | | |  |        |        |         |        |        |  |  |  |         |         |         |   |
|     TU     |   TR   | | | | | |  |   El   |   Az   |   Dt    |   El   |   Az   |El|Az|Az|    X    |    Y    |    Z    | M |
|            |        | | | | | |  |        |        |         | Aq-Ds  | Aq-Ds  |  |  |  |         |         |         |   |
|hh:mm:ss.zzz|ssss.zzz|E|A|D|R|T|SR|  grau  |  grau  |   Km    |  grau  |  grau  |  |  |  |   Km    |   Km    |   Km    | Ds|
+------------+--------+-+-+-+-+-+--+--------+--------+---------+--------+--------+--+--+--+---------+---------+---------+---+
""".format(operacao = arquivo_saida.strip(".txt"),veiculo=veiculo, data= data.strftime("%d/%m/%Y")).lstrip()


# Inicializa uma lista vazia para armazenar as linhas a serem impressas
linhas_a_imprimir = []
linhas_a_gravar = []

recebe_lista = ""

# Abre o arquivo de entrada para leitura
with open(arquivo_entrada, 'r') as arquivo:
    # Itera pelas linhas do arquivo de entrada
    for linha in arquivo:
        # Adiciona a linha à lista de linhas a serem impressas
        linhas_a_imprimir.append(linha)
    # Recebe o tamanho da lista linhas_a_imprimir
    contador_linhas = len(linhas_a_imprimir)
    with open(arquivo_saida, 'a') as arquivo:
        #arquivo.write(''.join(linhas_a_imprimir[0]))
        arquivo.write(cabecalho)
    # Percorre e printa os valores da lista a cada 20 vezes
    for i in range(1, contador_linhas, 20):
        # printa as linhas a seram gravadas no arquivo de saida
        #linhas_a_gravar.append(linhas_a_imprimir[i])
        recebe_lista = linhas_a_imprimir[i]
        recebe_lista = recebe_lista.split(",")
    
        for b in recebe_lista:
            linhas_a_gravar.append(b)
    
        trel = int(linhas_a_gravar[3])
        trel = trel / 1000
        
        print("""|{TU}|{TREL:4.3f}|{E}|{A}|{D}|{R}|{T}|{SR}|{EL}|{AZ}|{DT}| 0.00|  0.00|{B_EL}|{B_AZ}|{B_DT}|{X}|{Y}|{Z}|TJN|""".format(TU = linhas_a_gravar[1].strip(),TREL = trel, E = linhas_a_gravar[5].strip(), A = linhas_a_gravar[6].strip(), D = linhas_a_gravar[7].strip(), R = linhas_a_gravar[9].strip(), T = linhas_a_gravar[8].strip(), SR = linhas_a_gravar[13].strip(), EL = linhas_a_gravar[16], AZ = linhas_a_gravar[17], DT = linhas_a_gravar[18], B_EL = linhas_a_gravar[10], B_AZ = linhas_a_gravar[11], B_DT = linhas_a_gravar[12], X = linhas_a_gravar[25], Y = linhas_a_gravar[26], Z = linhas_a_gravar[27]))

#        print("""
#|{TU}|{TREL}|{E}|{A}|{D}|{R}|{T}|{SR}|{EL}|{AZ}|{DT}| 0.00|  0.00|{B_EL}|{B_AZ}|{B_DT}|{X}|{Y}|{Z}|TJN|
#""".format(TU = linhas_a_gravar[1].strip(),TREL = linhas_a_gravar[3], E = linhas_a_gravar[5].strip(), A = linhas_a_gravar[6].strip(), D = linhas_a_gravar[7].strip(), R = linhas_a_gravar[9].strip(), T = linhas_a_gravar[8].strip(), SR = linhas_a_gravar[13].strip(), EL = linhas_a_gravar[16], AZ = linhas_a_gravar[17], DT = linhas_a_gravar[18], B_EL = linhas_a_gravar[10], B_AZ = linhas_a_gravar[11], B_DT = linhas_a_gravar[12], X = linhas_a_gravar[25], Y = linhas_a_gravar[26], Z = linhas_a_gravar[27]))

    # Abre o arquivo de saída e escreve as linhas
        with open(arquivo_saida, 'a') as arquivo:
          #arquivo.write(''.join(linhas_a_imprimir[i]))
          arquivo.write("""|{TU}|{TREL:>8.3f}|{E}|{A}|{D}|{R}|{T}|{SR:>2}|{EL:>8}|{AZ:>9}|{DT:>8}|    0.00|    0.00|{B_EL:2}|{B_AZ:>2}|{B_DT:>2}|{X:>9}|{Y:>9}|{Z:>9}|TJN|\n""".format(TU = linhas_a_gravar[1].strip(),TREL = trel, E = linhas_a_gravar[5].strip(), A = linhas_a_gravar[6].strip(), D = linhas_a_gravar[7].strip(), R = linhas_a_gravar[9].strip(), T = linhas_a_gravar[8].strip(), SR = linhas_a_gravar[13].strip(), EL = linhas_a_gravar[16].strip(), AZ = linhas_a_gravar[17].strip(), DT = linhas_a_gravar[18].strip(), B_EL = linhas_a_gravar[10].strip(), B_AZ = linhas_a_gravar[11].strip(), B_DT = linhas_a_gravar[12].strip(), X = linhas_a_gravar[25].strip(), Y = linhas_a_gravar[26].strip(), Z = linhas_a_gravar[27].strip()))

        recebe_lista = ""
        linhas_a_gravar = []


print("""
###############################################################
########### ARQUIVO {arquivo} GERADO COM SUCESSO!!! ###########
############################################################### """.format(arquivo = arquivo_saida))