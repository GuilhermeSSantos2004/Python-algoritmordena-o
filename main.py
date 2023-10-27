'''def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        candidato = lista[i]
        menor = candidato
        indice_menor = i
    return indice_menor

def selection_sort_pior(lista):
    ordenada = []

    while lista:
        indice_menor = acha_menor(lista)
        menor = lista.pop(indice_menor)
        ordenada.append(menor)
    return ordenada

def selection_sort(lista):
    for i in range(len(lista)):
        indice_dalay = acha_menor(lista[i:])
        indice_real = indice[indice_real]
        lista[indice_real] = aux
    return lista

lista = [4,2,6,1,7,0,3]
lista = selection_sort_pior(lista)
print(lista)
#comportamento acientodico
lista = selection_sort(lista)
print(lista)




lista = [4,2,6,1,7,0,3]

#ordem
#======================
#    bubble sort (n^2)
#======================

def
    for j in range(len(lista)):
        n_trocas = 0
        print(f"{j+1}° passo: ")
        for i in range(len(lista) -j-1):
            print(lista[i],lista[i+1])

            if lista[i] > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
                print(lista)
                print()
                n_trocas += 1
        if n_trocas == 0:
            print(lista)
            break


# 2^3 = 8 3 = log 2/8


def sqrt_ruinzasso(num,precisao):
    delta = precisao
    i = 0
    valores = []
    while i <= num:
        valores.append(i)
        i+=delta
    menor = valores[0]

    for valor in valores:
        if (valor**2 - num) < abs(menor**2 - num):
            menor = valor
    return menor
raiz = sqrt_ruinzasso(10,0.001)
print(raiz,raiz**2, abs(raiz**2-10))



chute = 25
while True:

        aux = chute / 2

        if aux ** 2 == chute:
                print(aux)
        print(aux)

def raiz_binaria(num,precisao):
        inicio = 0
        fim = num
        chute = (inicio+fim)/2
        while abs(chute**2-num) > precisao:
                if chute**2 > num:
                        fim = chute
                else:
                        inicio = chute
                chute = (inicio)


lista = [1,2,3,4,5,6,7]

chute = 7


while True:
    inicio = lista[len(lista/2)]
    fim = 0
    if  inicio < chute:
        inicio =



lista = [1,2,3,4,5,6,7]
lista_menor = []
pivo = lista[0]
for elem in lista:
    if elem<pivo:
        lista_menor.append(elem)
'''
# a = adiciona no final do arquivo
#
string = "oi eu me chamo dan"
f = open("teste.txt","a")
f.write(string)
f.close()
