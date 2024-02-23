from collections import deque

ESTADO_OBJETIVO = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def encontrar_espacio_vacio(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j

def mover(estado, direccion):
    i, j = encontrar_espacio_vacio(estado)
    nuevo_estado = [list(fila) for fila in estado]
    
    if direccion == "derecha" and j < 2:
        nuevo_estado[i][j], nuevo_estado[i][j+1] = nuevo_estado[i][j+1], nuevo_estado[i][j]
    elif direccion == "izquierda" and j > 0:
        nuevo_estado[i][j], nuevo_estado[i][j-1] = nuevo_estado[i][j-1], nuevo_estado[i][j]
    elif direccion == "abajo" and i < 2:
        nuevo_estado[i][j], nuevo_estado[i+1][j] = nuevo_estado[i+1][j], nuevo_estado[i][j]
    elif direccion == "arriba" and i > 0:
        nuevo_estado[i][j], nuevo_estado[i-1][j] = nuevo_estado[i-1][j], nuevo_estado[i][j]
    else:
        return None

    return tuple(map(tuple, nuevo_estado))

def bfs(estado_inicial, estado_objetivo=ESTADO_OBJETIVO):
    visitados = set()
    cola = deque([(estado_inicial, [])])

    nodos_visitados = 0
    max_nodos_en_memoria = 0

    while cola:
        estado_actual, camino = cola.popleft()
        nodos_visitados += 1

        max_nodos_en_memoria = max(max_nodos_en_memoria, len(cola))

        if estado_actual == estado_objetivo:
            return camino + [estado_actual], nodos_visitados, max_nodos_en_memoria

        visitados.add(estado_actual)

        for direccion in ["derecha", "izquierda", "abajo", "arriba"]:
            proximo_estado = mover(estado_actual, direccion)
            
            if proximo_estado and proximo_estado not in visitados:
                cola.append((proximo_estado, camino + [estado_actual]))

    return None, nodos_visitados, max_nodos_en_memoria

def imprimir_camino(camino):
    for estado in camino:
        for fila in estado:
            print(' | '.join(str(celda) if celda != 0 else ' ' for celda in fila))
        print("------")

if __name__ == "__main__":
    inicial = ((1, 2, 4), (8, 3, 5), (7, 6, 0))
    
    camino_bfs, complejidad_tiempo_bfs, complejidad_espacio_bfs = bfs(inicial)
    print("Camino BFS:")
    imprimir_camino(camino_bfs)
    print(f"Complejidad en tiempo: {complejidad_tiempo_bfs}")
    print(f"Complejidad en espacio: {complejidad_espacio_bfs}")
