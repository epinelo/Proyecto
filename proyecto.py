def Mostrar_Menu() :

    # Función que muestra el Menú de opciones.

    print()
    print('MENÚ')
    print('1. Carta')
    print('2. Realizar pedido')
    print('3. Finalizar')
    opc = input('Seleccione una opción: ')
    Opcion_Menu(opc)

def Opcion_Menu(opc) :

    # Función que evalua la opción dada por el usuario.

    if opc == '1' :
        Mostrar_Carta()
    elif opc == '2' :
        Realizar_Pedido()
    elif opc == '3' :
        Finalizar_Pedido()
    else :
        print('Número inválido, intenta de nuevo.')
        Mostrar_Menu()

def Mostrar_Carta() :

    # Función que muestra la carta de productos y precios de la taquería.

    print()
    print('TACOS')
    print('Pastor ------------- $10')
    print('Chorizo ------------ $15')
    print('Suadero ------------ $25')
    print('Lengua ------------- $30')
    print('Bistec ------------- $10')
    print('Cochinita ---------- $45')
    print()

    print('AGUAS')
    print('Grande (1L) -------- $30')
    print('Mediana (600ml) ---- $17')
    print('Chica (355ml) ------ $10')
    print('SABORES')
    print('Horchata')
    print('Jamaica')
    print('Limón')
    print('Tamarindo')

    Mostrar_Menu()

def Realizar_Pedido() :

    # Función que se encarga de registrar el pedido mediante inputs y, haciendo
    # uso de otras funciones, calcula el total tomando en cuenta si el usuario
    # elijó algún complemento y/o decidió agregar propina.

    print()
    sabor_taco = input('¿Cuál es el sabor de tu taco? ')
    cantidad_tacos = int(input('¿Cuántos tacos quieres? '))
    precio_taco = float(input('¿Cuánto cuesta tu taco? '))

    sabor_agua = input('¿Cuál es el sabor de tu agua? ')
    tamaño_agua = input('¿De que tamaño deseas tu agua? ')
    precio_agua = float(input('¿Cuánto cuesta tu agua? '))

    extra = input(
    '¿Deseas complementar con chicharrón de queso o cebollas preparadas? ')
    if extra.lower() == 'si' :
        print()
        print('Chicarrón de queso ------------- $45')
        print('Cebollas preparadas ------------ $25')
        print()
        extra = input('¿Qué complemento deseas? ')
        precio_extra = float(input('¿Cuánto cuesta tu extra? '))
        tot = Complemento(precio_taco, cantidad_tacos, precio_agua,
                            precio_extra)
        propina = input('¿Deseas agregar propina? ')
        if propina.lower() == 'si' :
            porcentaje = float(input(
            '¿Cuánto deseas agregar? (Introduce el porcentaje, sin símbolos) '))
            tot = Propina(porcentaje, tot)
            Confirmacion_Pedido_Propina(sabor_taco, cantidad_tacos, sabor_agua,
                                tamaño_agua, extra, porcentaje, propina, tot)
        else:
            Confirmacion_Pedido(sabor_taco, cantidad_tacos, sabor_agua,
                                    tamaño_agua, extra, propina, tot)
    else :
        tot = Total(precio_taco, cantidad_tacos, precio_agua)
        propina = input('¿Deseas agregar propina? ')
        if propina.lower() == 'si' :
            porcentaje = float(input(
            '¿Cuánto deseas agregar? (Introduce el porcentaje, sin símbolos) '))
            tot = Propina(porcentaje, tot)
            Confirmacion_Pedido_Propina(sabor_taco, cantidad_tacos, sabor_agua,
                                tamaño_agua, extra, porcentaje, propina, tot)
        else:
            tot = Total(precio_taco, cantidad_tacos, precio_agua)
            Confirmacion_Pedido(sabor_taco, cantidad_tacos, sabor_agua,
                                    tamaño_agua, extra, propina, tot)

    Mostrar_Menu()

def Confirmacion_Pedido_Propina(sabor_taco, cantidad_tacos, sabor_agua,
                            tamaño_agua, extra, porcentaje, propina, tot) :

    # Función que imprime la confirmación del pedido si el usuario decidió
    # agregar propina.

    print()
    print('CONFIRMACIÓN: ')
    print(cantidad_tacos, 'tacos de', sabor_taco)
    print('Agua', tamaño_agua, 'de', sabor_agua)
    if (extra.lower() == 'chicharrón de queso' or
    extra.lower() == 'cebollas preparadas'):
        print(extra)
    else:
        print('Sin complemento')
    if propina.lower() == 'si' :
        print('Propina:', porcentaje)
    else :
        print('Cuenta cerrada')
    print('Total:', tot)

def Confirmacion_Pedido(sabor_taco, cantidad_tacos, sabor_agua, tamaño_agua,
                            extra, propina, tot) :

    # Función que imprime la confirmación del pedido si el usuario decidió
    # no agregar propina.

    print()
    print('CONFIRMACIÓN: ')
    print(cantidad_tacos, 'tacos de', sabor_taco)
    print('Agua', tamaño_agua, 'de', sabor_agua)
    if (extra.lower() == 'chicharrón de queso' or
    extra.lower() == 'cebollas preparadas'):
        print(extra)
    else:
        print('Sin complemento')
    if propina.lower() == 'si' :
        print('Propina:', porcentaje)
    else :
        print('Cuenta cerrada')
    print('Total:', tot)

def Finalizar_Pedido() :

    # Función que imprime un mensaje de confirmación, y además muestra la
    # encuesta de servicio, donde se calificará el servicio en una escala
    # del 1 al 5.

    print('¡Gracias por su compra! Su pedido pronto estará listo.')
    calif = input('Por favor, en una escala del 1 al 5 califique el servicio: ')
    if calif == '1' :
        print('En su próximo pedido prometemos un mejor servicio.')
    if calif == '2' :
        print('En su próximo pedido prometemos un mejor servicio.')
    if calif == '3' :
        print('Gracias por calificar nuestro servicio.')
    if calif == '4' :
        print('Gracias por calificar nuestro servicio.')
    if calif == '5' :
        print('¡Gracias! Nos da gusto que hayas recibido un buen servicio.')
        return

def Complemento(precio_taco, cantidad_tacos, precio_agua, precio_extra) :

    # Función que realiza el cálculo del total del pedido con complemento.

    total = (precio_taco * cantidad_tacos) + precio_agua + precio_extra
    return total

def Total(precio_taco, cantidad_tacos, precio_agua) :

    # Función que realiza el cálculo del total del pedido sin complemento.

    total = (precio_taco * cantidad_tacos) + precio_agua
    return total

def Propina(porcentaje, total) :

    # Función que realiza el cálculo del total del pedido con propina.

    total = (total * (porcentaje / 100)) + total
    return total

Mostrar_Menu()
