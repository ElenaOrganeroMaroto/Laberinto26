# **Proyecto Laberinto - Diseño de Software**
Este proyecto forma parte de la asignatura de Diseño de Software y consiste en implementar un laberinto el cuál está compuesto por habitaciones que están conectadas entre sí por puertas y separadas por paredes. En su desarrollo se han incorporado diferentes patrones de diseño para mejorar la estructura y flexibilidad del código.

## Descripción
Los componentes principales que forman el laberinto son los siguientes:
- Elemento Mapa: Es la interfaz comun de los elementos.
- Pared: Es un elemento del mapa que no se puede atravesar.
- Puerta: Es un elemento del mapa que une dos habitaciones.

## Diagrama inicial



## 01. Factory Method
Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.

<p align="center">
<img width="100%"  alt="01  Factory Method" src="https://github.com/user-attachments/assets/05f0ab58-b828-4f71-bda9-0e95371b0c32" />

</p>


---

## 02. Decorator
Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

<p align="center">
<img width="100%" alt="02  Decorator" src="https://github.com/user-attachments/assets/bfcbf185-326e-495a-897a-76fb02f922de" />

</p>

---

## 03. Strategy
Define una familia de algoritmos, encapsula cada uno en un objeto, de modo que son
intercambiables. El Strategy permite cambiar el algoritmo sin que afecte al cliente.

<p align="center">
<img width="100%" alt="03  Strategy" src="https://github.com/user-attachments/assets/f0ee1cfb-c890-42dc-9acc-59a4809f3b42" />
</p>

---

## 04. Composite
Compone objetos en una estructura de árbol para representar jerarquías todo-parte. El
Composite permite que el cliente trate de manera uniforme tanto a objetos individuales como
a objetos compuestos.

<p align="center">
<img width="100%" alt="Composite" src="https://github.com/user-attachments/assets/794f9f4b-a586-4a59-a5e1-60a01ded6204" />
</p>

---

## 05. Iterator
Proporciona una forma de acceder secuencialmente a los elementos de un agregado
(colección, conjunto, aggregate) sin exponer su implementación.

<p align="center">
<img width="100%" alt="05  Iterator" src="https://github.com/user-attachments/assets/353912e0-4d2a-43fa-935f-15fa961558ad" />

</p>

---

## 06. Template Method
Define el esqueleto de un algoritmo en una operación, dejando que las subclases definan
algunos de los pasos. El Template Method deja que las subclases redefinan ciertos pasos de un
algoritmo sin variar la estructura del algoritmo.

<p align="center">
<img width="100%" alt="06  Template Method" src="https://github.com/user-attachments/assets/e315da60-96a8-427c-8a02-c4cb747da9c3" />
</p>

---

## 07. Abstract Factory
Proporciona una interface para crear familias de objetos relacionados o dependientes sin 
especificar sus clases concretas.

<p align="center">
<img width="100%" alt="07  Abstract Factory" src="https://github.com/user-attachments/assets/1bdf78b0-d02c-4183-adee-2e2ffbdbb619" />
</p>

---

## 08. Singleton
Asegura que una clase sólo tiene una instancia y proporciona un punto de acceso a la 
instancia.

<p align="center">
<img width="100%" alt="08  Singleton" src="https://github.com/user-attachments/assets/ca5456ec-6897-43e3-9e42-b8863809d459" />
</p>

---


## 09. Builder
Separa la construcción de un objeto complejo de su representación, de modo que el mismo 
proceso de construcción se utiliza para crear diferentes representaciones.

<p align="center">
<img width="100%" alt="09  Builder" src="https://github.com/user-attachments/assets/1418dfd1-3136-414c-a3c4-431c4cd2c7cf" />
</p>

---


## 10. Proxy
Proporciona un sustituto o referencia a otro objeto para controlar el acceso a ese objeto.

<p align="center">

</p>

---


## 11. Adapter
Convierte la interface de una clase en la interface que espera el cliente. El Adapter permite
trabajar juntas a unas clases que tienen interfaces incompatibles.

<p align="center">

</p>

---


## 12. Bridge
Desacopla una abstracción de su implementación de modo que las dos puedan variar de forma
independiente.

<p align="center">

</p>

---


## 13. Mediator
Define un objeto que encapsula la interacción entre un conjunto de objetos. El Mediator
promueve un acoplamiento débil al evitar que los objetos tengan referencia al resto de objetos
de forma explícita, lo cual permite variar su interacción de forma independiente.


<p align="center">

</p>

---
