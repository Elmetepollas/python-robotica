# Actividad 10 — El primero y el último

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 1 de noviembre de 2026, 23:59
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Una lista guarda los valores en orden. Cada uno tiene un número de posición, el índice. El primero es el 0. El último se puede pedir con `-1`.

## Objetivo

Leer la longitud de una lista y tres posiciones concretas.

## Lo que debes hacer

1. Crea `solucion/posiciones.py`.
2. Declara `ordenes = ["adelante", "izquierda", "adelante", "parar"]`.
3. Muestra cuántos elementos tiene con `len(ordenes)`.
4. Muestra, cada uno en su línea:
   - el primero, `ordenes[0]`;
   - el segundo, `ordenes[1]`;
   - el último, `ordenes[-1]`.
5. Añade un comentario que explique que el primer elemento es el índice 0.
6. Ejecuta el programa y guarda la salida en `solucion/posiciones-salida.txt`.

Cada posición se imprime con su propio `print()`.

## Entregable

- `solucion/posiciones.py`.
- `solucion/posiciones-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la longitud con `len()` | 25 % |
| Se muestran el índice 0, el índice 1 y el índice -1 | 40 % |
| Hay un comentario que explica que el primero es el 0 | 15 % |
| La salida está guardada en `posiciones-salida.txt` | 20 % |

## Pista de cara al futuro

`len()` te dice cuántos elementos hay. Las posiciones empiezan en 0 y el último se alcanza con `-1`.
