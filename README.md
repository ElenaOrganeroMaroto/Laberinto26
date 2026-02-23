# **Proyecto Laberinto - Diseño de Software**
Este proyecto forma parte de la asignatura de Diseño de Software y consiste en implementar un laberinto el cuál está formado por habitaciones que están conectadas entre sí por puertas y separadas por paredes. En su desarrollo se han incorporado diferentes patrones de diseño para mejorar la estructura y flexibilidad del código.

## Descripción
Los componentes principales que forman el laberinto son los siguientes:
- Elemento Mapa: Es la interfaz comun de los elementos.
- Pared: Es un elemento del mapa que no se puede atravesar.
- Puerta: Es un elemento del mapa que une dos habitaciones.

## Diagrama inicial



## Factory Method
Define una interface para crear un objeto, pero deja que las subclases decidan qué clase
instanciar. El Factory Method permite que una clase posponga la instanciación a las subclases.

<p align="center">
<img width="100%" alt="Factory Method" src="https://github.com/user-attachments/assets/c6e439e3-0c11-4a38-b5fc-029d194d27e4" />
</p>

---

## Decorator
Asigna dinámicamente responsabilidades adicionales a un objeto. Los decoradores
proporcionan una alternativa flexible a la subclasificación para extender la funcionalidad.

<p align="center">
  <img width="100%" alt="Decorator" src="https://github.com/user-attachments/assets/3949567e-acdf-48c9-869d-6dab0a59f67c" />
</p>

---

## Strategy
Define una familia de algoritmos, encapsula cada uno en un objeto, de modo que son
intercambiables. El Strategy permite cambiar el algoritmo sin que afecte al cliente.

<p align="center">
  <img width="100%" alt="Strategy" src="https://github.com/user-attachments/assets/9d512956-d3f4-4108-a24b-a6db7144883c" />
</p>

---

## Composite
Compone objetos en una estructura de árbol para representar jerarquías todo-parte. El
Composite permite que el cliente trate de manera uniforme tanto a objetos individuales como
a objetos compuestos.

<p align="center">
  <img width="100%" alt="Composite" src="https://github.com/user-attachments/assets/794f9f4b-a586-4a59-a5e1-60a01ded6204" />
</p>

---



