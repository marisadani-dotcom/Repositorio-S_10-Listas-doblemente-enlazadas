def buscar(dato):
    global cabeza, cola
    
    izq = cabeza
    der = cola
    
    # Buscamos mientras los punteros sean válidos y no se hayan cruzado
    while izq is not None and der is not None:
        # Verificar si alguno encontró el dato
        if izq['dato'] == dato or der['dato'] == dato:
            return True
        
        # Si se cruzan o se encuentran en el mismo nodo, ya buscamos en toda la lista
        if izq == der or izq['anterior'] == der:
            break
            
        # Avanzar el de la izquierda y retroceder el de la derecha
        izq = izq['siguiente']
        der = der['anterior']
        
    return False