# **Proyecto Laberinto - Diseño de Software**
Este proyecto forma parte de la asignatura de Diseño de Software y consiste en implementar un laberinto el cuál está compuesto por habitaciones que están conectadas entre sí por puertas y separadas por paredes. En su desarrollo se han incorporado diferentes patrones de diseño para mejorar la estructura y flexibilidad del código.

## Descripción
Los componentes principales que forman el laberinto son los siguientes:
- Elemento Mapa: Es la interfaz comun de los elementos.
- Pared: Es un elemento del mapa que no se puede atravesar.
- Puerta: Es un elemento del mapa que une dos habitaciones.

## Diagrama final



## 01. Factory Method
Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.

<p align="center">
<img width="50%"  alt="01  Factory Method" src="https://github.com/user-attachments/assets/05f0ab58-b828-4f71-bda9-0e95371b0c32" />

</p>


---

## 02. Decorator
Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

<p align="center">
<img width="50%" alt="02  Decorator" src="https://github.com/user-attachments/assets/bfcbf185-326e-495a-897a-76fb02f922de" />

</p>

---

## 03. Strategy
Strategy es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.

<p align="center">
<img width="50%" alt="03  Strategy" src="https://github.com/user-attachments/assets/1fd23d6d-70df-428c-b054-cf1ecf7ef7c5" />

</p>

---

## 04. Composite
Composite es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.

<p align="center">
<img width="50%" alt="04  Composite" src="https://github.com/user-attachments/assets/c6767fbf-ba0e-4e2f-bfe3-367931b91bfa" />

</p>

---

## 05. Iterator
Iterator es un patrón de diseño de comportamiento que te permite recorrer elementos de una colección sin exponer su representación subyacente (lista, pila, árbol, etc.).

<p align="center">
<img width="50%" alt="05  Iterator" src="https://github.com/user-attachments/assets/b42feb40-685f-4a52-8534-92c15d018181" />
</p>

---

## 06. Template Method
Template Method es un patrón de diseño de comportamiento que define el esqueleto de un algoritmo en la superclase pero permite que las subclases sobrescriban pasos del algoritmo sin cambiar su estructura.

<p align="center">
<img width="50%" alt="06  Template Method" src="https://github.com/user-attachments/assets/c6abacdb-96a4-4007-b0ad-bca66177e2d8" />
</p>

---

## 07. Abstract Factory
Abstract Factory es un patrón de diseño creacional que nos permite producir familias de objetos relacionados sin especificar sus clases concretas.

<p align="center">

</p>

---

## 08. Singleton
Singleton es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.

<p align="center">
<img width="50%"  alt="08  Singleton" src="https://github.com/user-attachments/assets/8cbf442d-cafc-4888-8218-756adf2507ee" />

</p>

---


## 09. Builder
Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.

<p align="center">
<img width="50%" alt="09  Builder" src="https://github.com/user-attachments/assets/d03d6072-6330-48c0-9cde-1e511e21505d" />
</p>

---


## 10. Proxy
Proxy es un patrón de diseño estructural que te permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

<p align="center">
<img width="50%"  alt="10  Proxy" src="https://github.com/user-attachments/assets/44ac55e0-80fe-4b6e-bdeb-2010c289d4a3" />

</p>

---


## 11. Adapter
Adapter es un patrón de diseño estructural que permite la colaboración entre objetos con interfaces incompatibles.

<p align="center">

</p>

---


## 12. Bridge
Bridge es un patrón de diseño estructural que te permite dividir una clase grande, o un grupo de clases estrechamente relacionadas, en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.

<p align="center">
<img width="50%"  alt="12  Bridge" src="https://github.com/user-attachments/assets/0bb7e31b-a05c-4eb1-95b1-85a740c1460a" />

</p>

---


## 13. Mediator
Mediator es un patrón de diseño de comportamiento que te permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre los objetos, forzándolos a colaborar únicamente a través de un objeto mediador.

<p align="center">

</p>

---


## 14. Observer
<p align="center">

</p>

---


## 15. Command
Command es un patrón de diseño de comportamiento que convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud. Esta transformación te permite parametrizar los métodos con diferentes solicitudes, retrasar o poner en cola la ejecución de una solicitud y soportar operaciones que no se pueden realizar.

<p align="center">
<img width="50%" alt="15  Command" src="https://github.com/user-attachments/assets/21ab6c53-1b0a-4e9f-8544-658ee04c4705" />

</p>

---


## 16. State
State es un patrón de diseño de comportamiento que permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara su clase.

<p align="center">
<img width="50%"  alt="16  State" src="https://github.com/user-attachments/assets/3c3b8dfa-ab4a-4348-8256-a4eedc473352" />

</p>

---


## 17. Prototype
Prototype es un patrón de diseño creacional que nos permite copiar objetos existentes sin que el código dependa de sus clases.

<p align="center">
<img width="50%" alt="17  Prototype" src="https://github.com/user-attachments/assets/ec05b430-3e38-4052-b5b9-86bea501f50b" />

</p>

---


## 18. Visitor
Visitor es un patrón de diseño de comportamiento que te permite separar algoritmos de los objetos sobre los que operan.

<p align="center">

</p>

---


## 19. Flyweight
Flyweight es un patrón de diseño estructural que te permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo las partes comunes del estado entre varios objetos en lugar de mantener toda la información en cada objeto.

<p align="center">

</p>

---
