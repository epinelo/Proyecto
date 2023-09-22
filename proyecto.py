tacos = {'PA': 10, 'CHO': 15, 'SUA': 25, 'LEN': 30, 'BI': 10, 'CO': 45}

aguas = {'G': 30, 'M': 17, 'CH': 10}

complementos = {'CQ': 45, 'CP': 25, 'NO': 30, 'GUA': 40, 'FRI': 20}

def Mostrar_Menu(tacos, aguas, complementos):

    while True:
        print()
        print('MENÚ')
        print('1. Carta')
        print('2. Realizar pedido')
        print('3. Finalizar')
        opc = input('Seleccione una opción: ')

        if opc == '1':
            Mostrar_Carta(tacos, aguas, complementos)
        elif opc == '2':
            Realizar_Pedido(tacos, aguas, complementos)
        elif opc == '3':
            Finalizar_Pedido()
            break  # Salir del bucle cuando el usuario elige finalizar
        else:
            print('Número inválido, intenta de nuevo.')

def Mostrar_Carta(tacos, aguas, complementos) :

    # Función que muestra la carta de productos y precios de la taquería.

    print()
    print('TACOS')
    print('Pastor (PA) ------------------ $10')
    print('Chorizo (CHO) ---------------- $15')
    print('Suadero (SU) ----------------- $25')
    print('Lengua (LE) ------------------ $30')
    print('Bistec (BI) ------------------ $10')
    print('Cochinita (CO) --------------- $45')
    print()

    print('AGUAS')
    print('Grande (1L) (G) -------------- $30')
    print('Mediana (600ml) (M) ---------- $17')
    print('Chica (355ml) (CH) ----------- $10')
    print('SABORES')
    print('Horchata (HO)')
    print('Jamaica (JA)')
    print('Limón (LI)')
    print('Tamarindo (TA)')
    print()

    print('COMPLEMENTOS')
    print('Chicharrón de queso (CQ) ----- $45')
    print('Cebollas preparadas (CP) ----- $45')
    print('Nopales (NO) ----------------- $45')
    print('Guacamole (GUA) -------------- $45')
    print('Frijoles (FRI) --------------- $45')

    Mostrar_Menu(tacos, aguas, complementos)

def Realizar_Pedido(tacos, aguas, complementos):
    # Inicializar variables para el pedido
    total_pedido = 0  # Inicializamos el total del pedido en cero

    print()
    print(
    'FAVOR DE UTILIZAR LOS CÓDIGOS DE CADA PRODUCTO PARA REALIZAR SU PEDIDO',
          '(E.G. Taco de Pastor: PA)')

    while True:
        taco_o_no = input('¿Desea agregar tacos a su orden? ')
        if taco_o_no.lower() == 'si':
            sabor_taco = input('Sabor de taco: ')
            cantidad_tacos = int(input('Cantidad de tacos: '))
            total_pedido += tacos.get(sabor_taco, 0) * cantidad_tacos
        else:
            sabor_taco = None
            cantidad_tacos = 0

        agua_o_no = input('¿Desea agregar alguna bebida a su orden? ')
        if agua_o_no.lower() == 'si':
            sabor_agua = input('Sabor de agua: ')
            tamaño_agua = input('Tamaño del agua: ')
            cantidad_agua = int(input('Cantidad de aguas: '))
            total_pedido += aguas.get(tamaño_agua, 0) * cantidad_agua
        else:
            sabor_agua = None
            tamaño_agua = None
            cantidad_agua = 0

        extra_o_no = input('¿Deseas agregar algún complemento? ')
        if extra_o_no.lower() == 'si':
            extra = input('Complemento: ')
            total_pedido += complementos.get(extra, 0)
            propina = input('¿Deseas agregar propina? ')
            if propina.lower() == 'si':
                porcentaje = float(input('¿Cuánto deseas agregar?',
                '(Introduce el porcentaje, sin símbolos) '))
                total_pedido += (porcentaje / 100) * total_pedido

        # Imprime la confirmación del pedido
        print()
        print('CONFIRMACIÓN:')
        if sabor_taco:
            print(f'{cantidad_tacos} tacos de {sabor_taco} - ${tacos.get(
            sabor_taco, 0) * cantidad_tacos}')
        if tamaño_agua:
            print(f'Agua {tamaño_agua} de {sabor_agua} - ${aguas.get(
            tamaño_agua, 0) * cantidad_agua}')
        if extra:
            print(f'{extra} - ${complementos.get(extra, 0)}')
        print(f'Total: ${total_pedido}')

        # Pregunta si desea agregar más elementos al pedido
        continuar_pedido = input(
        '¿Desea agregar más elementos al pedido? (si/no) ')
        if continuar_pedido.lower() != 'si':
            break  # Sal del bucle si no se desea agregar más elementos

        Mostrar_Menu(tacos, aguas, complementos)

def Confirmacion_Pedido_Propina(tacos, aguas, complementos, sabor_taco,
                            cantidad_tacos, sabor_agua, tamaño_agua, extra_o_no,
                            extra, porcentaje, propina, tot) :

    # Función que imprime la confirmación del pedido si el usuario decidió
    # agregar propina.

    print()
    print('CONFIRMACIÓN: ')
    print(cantidad_tacos, 'tacos de', sabor_taco, '-',
    tacos[sabor_taco] * cantidad_tacos)
    print('Agua', tamaño_agua, 'de', sabor_agua, '-',
    aguas[tamaño_agua])
    if extra_o_no.lower() == 'si' :
        print(extra, '-', complementos[extra])
    else:
        print('Sin complemento')
    if propina.lower() == 'si' :
        print('Propina:', porcentaje)
    else :
        print('Cuenta cerrada')
    print('Total:', tot)

def Confirmacion_Pedido(tacos, aguas, complementos, sabor_taco, cantidad_tacos,
                        sabor_agua, tamaño_agua,extra_o_no, extra, propina,
                        tot) :

    # Función que imprime la confirmación del pedido si el usuario decidió
    # no agregar propina.

    print()
    print('CONFIRMACIÓN: ')
    print(cantidad_tacos, 'tacos de', sabor_taco, '-',
    tacos[sabor_taco] * cantidad_tacos)
    print('Agua', tamaño_agua, 'de', sabor_agua, '-',
    aguas[tamaño_agua])
    if extra_o_no.lower() == 'si' :
        print(extra, '-', complementos[extra])
    else:
        print('Sin complemento')
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

def Complemento(tacos, aguas, complementos, sabor_taco, cantidad_tacos,
tamaño_agua, precio_extra) :

    # Función que realiza el cálculo del total del pedido con complemento.

    total = (tacos[sabor_taco] * cantidad_tacos) + aguas[tamaño_agua] +
    complementos[extra]
    return total

def Total(tacos, aguas, complementos, sabor_taco, cantidad_tacos, tamaño_agua) :

    # Función que realiza el cálculo del total del pedido sin complemento.

    total = (tacos[sabor_taco] * cantidad_tacos) + aguas[tamaño_agua]
    return total

def Propina(porcentaje, total) :

    # Función que realiza el cálculo del total del pedido con propina.

    total = (total * (porcentaje / 100)) + total
    return total

Mostrar_Menu(tacos, aguas, complementos)
