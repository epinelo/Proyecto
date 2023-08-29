# TC 1028.414 Proyecto - TAQUERÍA TEC
## CONTEXTO (Avance 1)
Para este proyecto, he decidio basarme en aplicaciones de entrega de alimentos como Rappi, Uber eats, Didi food, etc. El programa desplegará un menú de opciones. En el menú, tendrás la opción de observar la carta de una taquería, en la que se ofrecerá una variedad de sabor de tacos, sabores y tamaños de agua, y complementos como cebollas preparadas y chicharrón de queso para realizar un pedido. En la carta se mostrarán todos los productos y sus precios. La segunda opción del menú será continuar con la realización de tu pedido, donde ingresarás los productos que deseas. Al terminar con tu pedido se preguntará sobre la propina, en caso de agregar propina, se calculará el porcentaje deseado. La tercera opción hará una confirmación y mostrará el total, con o sin propina. Finalmente, el programa terminará con tu pedido con una encuesta de servicio.
## Operadores (Avance 2)
En el programa que estoy trabajando, habrá una sección en la que el usuario podrá consultar cuánto deberá pagar después de realizar su orden, por lo que incluiré operadores para realizar algunos cálculos. Estos cálculos son la suma de los precios de los productos seleccionados, y en caso de que el usuario deseé agregar propina, se hará un segundo cálculo para arrogar el total después de agregar el porcentaje de propina deseado.

Para este avance realicé un código prueba que hace el trabajo de los cálculos de la cuenta total, con o sin propina, del pedido realizado. Al correr el código se pide el ingreso de los productos deseados y sus características (sabor, tamaño, cantidad, precio). Luego, se pregunta al usuario si desea agregar un complemento a su orden, dando dos opciones. El programa buscará un "si" por respuesta (sin importar las mayúsculas o minúsculas) en caso de el usuario deseé un complemento. Si obtiene un "si" por respuesta, se pedirá el complemento y su precio, y calculará el total a pagar agregando el costo del complemento a la cuenta. Si el prgrama no encuentra un "si" por respuesta, seguirá con el código. Después se preguntará al usuario si desea agregar propina. Al igual que la parte del complemento, si el programa recibe un "si" por respuesta, pedirá el ingreso de la propina el porcentaje, calculará la propina, la agregará a la cuenta e imprimirá el total del pedido. Si no desea agregar propina, solo imprimirá el total.

Para la realización de estos cálculos, he agregado las siguientes operaciones al programa:

>Cálculo del total sin propina (con complemento):
>
>>total = (precio_taco * cantidad_tacos) + precio_agua + precio_extra

>Cálculo del total con propina:
>
>>total = (total * (porcentaje / 100)) + total

## Funciones (Avance 3)
Como se ha mencionado anteriormente, el programa hará distintas tareas para completar un pedido, como mostrar la carta, resgistrar los productos seleccionados, calcular el total, la propina y confirmar la orden. Declararé una serie de funciones, una para cada tarea, para la facilidad de lectura del código y la realización de cada tarea. 

Agregue al código las siguientes funciones:

>Mostrar_Menu: Función que muestra el Menú de opciones.
>
>Opcion_Menu: Función que evalua la opción dada por el usuario.
>
>Mostrar_Carta: Función que muestra la carta de productos y precios de la taquería.
>
>Realizar_Pedido: Función que se encarga de registrar el pedido mediante inputs y, haciendo uso de otras funciones, calcula el total tomando en cuenta si el usuario elijó algún complemento y/o decidió agregar propina.
>
>Confirmacion_Pedido_Propina: Función que imprime la confirmación del pedido si el usuario decidió agregar propina.
>
>Confirmacion_Pedido: Función que imprime la confirmación del pedido si el usuario decidió no agregar propina.
>
>Finalizar_Pedido: Función que imprime un mensaje de confirmación, y además muestra la encuesta de servicio, donde se calificará el servicio en una escala del 1 al 5.
>
>**Complemento**: Función que realiza el cálculo del total del pedido con complemento.
>
>Total: Función que realiza el cálculo del total del pedido sin complemento.
>
>Propina: Función que realiza el cálculo del total del pedido con propina.

El siguiente código contiene la parte del programa con las funciones declaradas: [proyecto.py](proyecto.py)
