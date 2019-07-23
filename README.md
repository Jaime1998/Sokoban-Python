# Sokoban-Python

Introduccion a la Inteligencia Artificial

Sokoban

Integrantes:
 
Jaime Cuartas Granada: 1632664

Emily E Carvajal C.: 1630436

Luis Restrepo: 1427086

Para todos los algoritmos de busqueda se implementó una estructura de datos nombrada Taboo sobreescribiendo la función hash de la clase estado, siento Taboo una estructura de datos que representa un conjunto en el que se almacenan los estados revisados por cada algoritmo y prohibiendolos para futuras busquedas evitando expansiones (La elección de la estructura set en python se realizó debido a que la complejidad temporal en promedio para las consultas es constante).

##BFS:

Para el algoritmo bfs, se realiza una busqueda expandiendo por anchura cada nivel del arbol sin limite.

#DFS:

Para el algoritmo dfs, se realiza la busqueda por profundidad expandiendo nodos en el orden Up, Down, Right y Left, sin limite, de esta manera siempre se encuentra la solución si la hay, más a la izquierda en el arbol. De esta manera no se garantiza retornar la solución más corta, pero si en la menor cantidad de tiempo posible.

##IDS:

Para el algoritmo ids, se realiza una busqueda con limite en 10, se realiza la busqueda por profundidad hasta alcanzar este limite y una vez se alcance este y no se encuentre solución se inrementa dicho limite 3 niveles y se continua on la busqueda por profundidad.
