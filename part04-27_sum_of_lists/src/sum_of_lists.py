# Write your solution here

def list_sum(lista, listb):
    listc = []

    for index in range(len(lista)):
        total = lista[index] + listb[index]
        listc.append(total)
    
    return listc

if __name__ == "__main__":
    lista = [1, 2, 3]
    listb = [7, 8, 9]

    print(list_sum(lista, listb))