def f_xor(dados, *args):
    zero = False
    if sum(dados) % 2 != 0:
        return 1
    else:
        return 0


def f_nor(dados, *args):
    if sum(dados) == 0:
        return 1
    else:
        return 0


def f_or(dados, *args):
    if sum(dados) == 0:
        return 0
    else:
        return 1


def f_nand(dados, *args):
    tag = False
    for x in dados:
        if x == 0:
            tag = True
    if tag == True:
        return 1
    else:
        return 0


def f_and(dados, *args):
    zero = False
    for x in dados:
        if x == 0:
            zero = True
    if zero == True:
        return 0
    else:
        return 1


def f_not(dados, *args):
    if sum(dados) > 0:
        return 0
    else:
        return 1


arq = open('circuito1.txt', 'r')
topoTV = []
entrada = arq.readline()
entrada = entrada.split(',')
saida = arq.readline()
saida = saida.split(',')
gate = arq.readline()
gate = gate.split(',')
arq.close()
tabela = []
num_entradas = int(entrada[1])
num_saidas = int(saida[1])
num_gates = int(gate[1])
num_linhas = 2 ** num_entradas
comp_gate = []
entrada_saida=[]
for i in range(2,len(entrada)):
  entrada_saida.extend(entrada[i].rstrip('\n').rsplit(','))
for i in range(2,len(saida)):
  entrada_saida.extend(saida[i].rstrip('\n').rsplit(','))
print(entrada_saida)


def cria_topoTV():
    for i in range(2, len(entrada)):
        entrada[i] = entrada[i].rstrip('\n')
        topoTV.append(entrada[i])
    for i in range(2, len(gate)):
        gate[i] = gate[i].rstrip('\n')
        topoTV.append(gate[i])
    for i in range(2, len(saida)):
        saida[i] = saida[i].rstrip('\n')
        topoTV.append(saida[i])


def criar_matriz():
    for i in range(0, num_linhas):
        tabela.append([])
        for j in range(0, num_colunas):
            tabela[i].append('#')
    acres = 0
    repet = num_linhas / 2
    ct = 0;
    for j in range(0, num_entradas):
        for i in range(0, num_linhas):
            tabela[i][j] = acres
            ct += 1
            if ct == repet:
                if (acres == 0):
                    acres = 1
                elif (acres == 1):
                    acres = 0
                ct = 0
        repet = repet / 2
    ct = 0

def comp_gates():
    arq = open('circuito1.txt', 'r')
    linhas = arq.readlines()
    for i in range(3, num_gates + 3):
        comp_gate.append(linhas[i].rstrip('\n'))
    arq.close()
    print(comp_gate)


def copiar_topo():
    for i in range(0, len(topoTV) - 2):
        copia_topo.append(topoTV[i])

def f_retirar(lista,*args):
    for i in range(0,len(entrada_saida)):
        if copia_topo[i] not in entrada_saida:
            resultado = i
            print(resultado)
            copia_topo.pop(i)
            print(copia_topo)
            return resultado




def modificar_copia_topo():
    for i in range(0, num_gates):
        elemento = []
        elemento = elemento + (comp_gate[i].rsplit(','))
        procurar = elemento[0]
        modificar = elemento[2]
        for j in range(0, len(copia_topo)):
            if (copia_topo[j] == procurar):
                copia_topo[j] = modificar
    print(copia_topo)

def matriz_final():
  for i in range(0, num_linhas):
      tabela_final.append([])
      for j in range(0, num_colunas):
          tabela_final[i].append('#')
  for i in range(0,num_linhas):
      for j in range(0,num_colunas):
          tabela_final[i][j]=tabela[i][j]
  k=0
  valor_copia=len(copia_topo)
  lim= valor_copia - len(entrada_saida)
  while k < lim:
      retirar = f_retirar(copia_topo)
      for i in range(0,num_linhas):
        for j in range(0,len(copia_topo)):
          if j == retirar:
              tabela_final[i].pop(retirar)
      k=k+1


def enviar_dados():
  i = 0
  l = 0
  saida = 0
  tipo = 0
  j = 0
  for i in range(0,num_linhas):
    j = 0
    while '#' in tabela[i]:
            dados_separados= []
            dados_separados.extend(comp_gate[j].rsplit(','))
            saida = dados_separados[2]
            tipo = dados_separados[1]
            dados_separados.pop(0)
            dados_separados.pop(0)
            dados_separados.pop(0)
            while l < len(dados_separados):
                coluna=copia_topo.index(dados_separados[l])
                dados_separados[l] = tabela[i][coluna]
                l+=1
            l = 0
            resultado=0
            if '#' in dados_separados:
                j+=1
                if j == num_gates:
                  j=0
                  continue
                continue
            else:
                  if tipo == 'xor':
                    resultado = f_xor(dados_separados)
                  if tipo == 'and':
                    resultado = f_and(dados_separados)
                  if tipo == 'or':
                    resultado = f_or(dados_separados)
                  if tipo == 'nor':
                    resultado = f_nor(dados_separados)
                  if tipo == 'nand':
                    resultado = f_nand(dados_separados)
                  if tipo == 'not':
                    resultado = f_not(dados_separados)
                  tabela[i][copia_topo.index(saida)] = resultado
            j += 1
            if j == num_gates:
              j = 0




def mostrar_matriz():
    for i in range(0,num_linhas):
        print(tabela_final[i])


cria_topoTV()
comp_gate = []
copia_topo = []
tabela_final=[]
comp_gates()
copiar_topo()
modificar_copia_topo()
num_colunas = len(copia_topo)
criar_matriz()
enviar_dados()
matriz_final()
mostrar_matriz()
