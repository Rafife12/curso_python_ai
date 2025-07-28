def ordenar_lista(lista):
    '''Ordena uma lista de inteiros em ordem crescente.'''
    return sorted(lista)

# Testes
if __name__ == "__main__":
    exemplo = [9, 1, 5, 3]
    print("Original:", exemplo)
    print("Ordenada:", ordenar_lista(exemplo))