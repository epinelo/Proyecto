# TC 1028.414 Proyecto
## CONTEXTO (Avance 1)
Para este proyecto, he decidio basarme en aplicaciones de entrega de alimentos como Rappi, Uber eats, Didi food, etc. En el programa, tendrás la opción de observar el menú de una taquería, en la que se ofrecerá una variedad de sabor de tacos, sabores de agua y complementos como cebolla, cilantro, piña y queso en tus tacos para realizar un pedido. En el menú se mostrarán todos los productos y sus precios. La segunda opción del programa será continuar con la realización de tu pedido, donde ingresarás los productos que deseas. Al terminar con tu pedido se hará una confirmación y el programa procederá con el precio total del pedido. Finalmente, preguntará si deseas agregar propina. En caso de agregar propina, se calculará el porcentaje deseado y arrogará el nuevo total, para así finalizar con el pedido.
## Operadores (Avance 2)
En el programa que estoy trabajando, habrá una sección en la que el usuario podrá consultar cuánto deberá pagar después de realizar su orden. Estos cálculos son la suma de los precios de los productos seleccionados, y en caso de que el usuario deseé agregar propina, se hará un segundo cálculo para arrogar el total después de agregar el porcentaje de propina deseado.

Para la realización de estos calculos, he agregado las siguientes operaciones al programa:

Cálculo del total sin propina:
  total = (precio_taco * cantidad_tacos) + precio_agua + precio_extra

Cálculo del total con propina:
  total = (total * (porcentaje / 100)) + total
