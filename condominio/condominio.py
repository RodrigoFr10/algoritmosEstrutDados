class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
    
    def cadastrar(self):
        #idAP=int(input("Digite o ID do novo apartamento: "))
        erroAPID=False
        APID=int(input("Digite o ID do apartamento: "))
        APnum=int(input("Digite o número do apartamento: "))
        for i in lista.lst:#verifica se já há algum apartamento com o mesmo ID ou numero da lista com vagas
            if i.id==APID or i.numero==APnum:
                print(f"Já há um apartamento com ID {APID} ou com número {APnum}")
                erroAPID=True
                break
                
            #else:
            #    print(f"{i.id} é diferente de {APID}")
        for i in fila.fila:#verifica se já há algum apartamento com o mesmo ID ou numero da fila
            if i.id==APID or i.numero==APnum:
                print(f"Já há um apartamento com ID {APID} ou com número {APnum}")
                erroAPID=True
                break
                
        if erroAPID==False:
            #print("Continuando execução. APID é ",erroAPID)
            if len(vagas)>0: #se a lista de vagas tiver alguma vaga, esta vaga é atribuida ao apartamento
                novoAP=Apartamento(APID,APnum,vagas[0],self)
                lista.adicionarAP(novoAP)
                vagas.pop(0)#remove a vaga da lista, pois não esta mais disponivel
            else: #se a lista de vagas estiver vazia, o AP é adicionado a fila
                print("Nenhuma vaga disponível")
                novoAP=Apartamento(APID,APnum,None,self)
                fila.adicionarAP(novoAP)
        else:
            print("INTERROMPIDO")
        #novoAP=Apartamento(idAP,idAP,None,self)
    

    def imprimir(self):
        txt=f"Torre {self.nome}"
        txt+=f"({self.id})\n"
        txt+=f"Endereço: {self.endereco}\n"
        return txt


class Apartamento:
    def __init__(self, idApartamento, numero, vaga, torre):
        self.id = idApartamento
        self.numero = numero
        self.vaga = vaga
        self.torre = torre  
    def cadastrar(self):
        print()
    def imprimir(self):
        txt=f"----Apartamento {self.id}----\n"
        txt+=f"Número {self.numero}\n"
        if self.vaga!=None:
            txt+=f"Vaga {self.vaga}\n"
        else:
            txt+="Sem vaga\n"
        txt+=f"Torre {self.torre.nome}\n"
        return txt

class Fila:
    def __init__(self,tamanho):
        self.tamanho=tamanho
        self.fila=[]

    def adicionarAP(self,ap):
        self.fila.append(ap)
        self.tamanho+=1 #aumenta o tamanho da fila em 1 ao adicionar um apartamento
        print("O seguinte apartamento foi adicionado à lista de espera\n")
        print(ap.imprimir())
        if len(vagas)>0:
            self.removerAP(vagas[0])
        
    
    def removerAP(self,v):
        if(len(self.fila)>0):
            print(f"O seguinte apartamento foi removido da fila, recebendo a vaga {v}:")
            print(self.fila[0].imprimir())
            self.fila[0].vaga=v

            self.tamanho-=1 #reduz o tamanho da fila em 1 ao remover um apartamento
            lista.adicionarAP(self.fila[0])
            self.fila.pop(0)
            vagas.pop(0)
        else:
            print("A fila está vazia")

    def imprimirFila(self):
        if(len(self.fila)>0):
            print(f"----FILA DE ESPERA({self.tamanho} em espera)----")
            for i in self.fila:
                print(i.imprimir())
        else:
            print("A lista de espera está vazia")

class Lista:
    def __init__(self,tamanho):
        self.tamanho=tamanho
        self.lst=[]

    def adicionarAP(self,ap):
        self.lst.append(ap)
        print("O seguinte apartamento foi adicionado à lista de apartamentos com vaga\n")
        print(ap.imprimir())
        self.tamanho+=1
        self.lst.sort(key=lambda apt:apt.vaga) #ordenando por vaga

    
    def removerAP(self,vaga):
        if(len(self.lst)>0): #antes de remover, verificar se a lista esta vazia
            vagas.append(i.vaga)
            print(vagas)
            i.vaga=None
            
            self.tamanho-=1
            self.lst.remove(vaga)
        else:
            print("A lista está vazia")

    def imprimirLista(self):

        if(len(self.lst)>0):
            print(f"----LISTA DE APARTAMENTOS({self.tamanho} com vaga)----")
            for i in self.lst:
                #print(f"Apartamento {i.numero}\nID: {i.id}\nTorre: {i.torre.imprimir()}")
                print(i.imprimir())
        else:
            print("A lista de apartamentos com vaga está vazia")

# Exemplo de uso das classes:
fila=Fila(0)
lista=Lista(0)
torres=[]
vagas=[1,2,3,4,5,6,7,8,9,10]
# Criando uma torre
torre1 = Torre(1, "A", "Rua Principal, 123")
torres.append(torre1)
torre2=Torre(2,"B","Rua Principal, 124")
torres.append(torre2)

ap1 = Apartamento(1, 101, None, torre1)
fila.adicionarAP(ap1)
ap2 = Apartamento(2, 201, None, torre2)
fila.adicionarAP(ap2)

ap3 = Apartamento(3, 202, None, torre2)
fila.adicionarAP(ap3)

ap4 = Apartamento(4, 203, None, torre2)
fila.adicionarAP(ap4)

ap5 = Apartamento(5, 1000, None, torre1)
fila.adicionarAP(ap5)

ap6 = Apartamento(6, 1006, None, torre1)
fila.adicionarAP(ap6)

ap7 = Apartamento(7, 107, None, torre1)
fila.adicionarAP(ap7)

ap8 = Apartamento(8, 208, None, torre2)
fila.adicionarAP(ap8)

ap9 = Apartamento(9, 209, None, torre2)
fila.adicionarAP(ap9)

rodando=True

while rodando:
    print("------MENU------\n1-Cadastrar apartamento\n2-Liberar vaga")
    print("3-Imprimir lista de apartamentos com vaga\n4-Imprimir fila de espera")

    esc=input("Escolha: ")
    
    if esc=="1":
        trr=int(input("Digite o ID da torre do novo apartamento: "))
        encontrado=False
        for i in torres:
            if i.id==trr:
                print(f"{i.id} é igual a {trr}")
                trr=i
                encontrado=True
                break
            else:
                print(f"{i.id} é diferente de {trr}") #print para testes e informação
        if(encontrado==True):
            print(f"Torre selecionada:")
            print(trr.imprimir())
            trr.cadastrar() #se uma torre com ID correspondente for encontrada, sua função de cadastrar é chamada
        else:
            print(f"Nenhuma torre com id {trr} foi encontrada")
        
    elif esc=="2":
        v=int(input("Digite a vaga que será liberada: "))
        for i in lista.lst: #verifica toda a lista por uma vaga que seja igual a digitada
            if i.vaga==v:
                lista.removerAP(i) #se a vaga for igual a digitada, o item é removido da lista
                fila.adicionarAP(i) #e adicionado a fila de espera
                print(f"Apartamento com a vaga {v} adicionado a fila")
                break
            else:
                print(f'{i.vaga} é diferente de {v}') #print para testes e informação
        
        
    elif esc=="3":
        lista.imprimirLista()
    elif esc=="4":
        fila.imprimirFila()
    else:
        print("Encerrando") #se o usuario digitar algo que não está no menu, ocorre o encerramento
        rodando=False


