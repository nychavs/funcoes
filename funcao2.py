def tabuada(n):
    tabu = []
    for i in range (1, 11):
        tabu.append(f"{n} x {i} = {i*n}")    
    return tabu
def printar(tabuada):
    for i in tabuada:
        print(f"{i}\n")

numero = int(input ("Digite o numero: "))
tab = tabuada(numero)
printar(tab)