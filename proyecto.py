tacos = {'PA': 10, 'CHO': 15, 'SUA': 25, 'LEN': 30, 'BI': 10, 'CO': 45}

lista_tacos = ['PA', 'CHO', 'SUA', 'LEN', 'BI', 'CO']

aguas = {'HO': 'horchata', 'JA': 'jamaica', 'LI': 'limón',
'TA': 'tamarindo'}

lista_aguas = ['HO', 'JA', 'LI', 'TA']

tamaños_aguas = {'G': 30, 'M': 17, 'CH': 10}

lista_tamaños_aguas = ['G', 'M', 'CH']

complementos = {'CQ': 45, 'CP': 25, 'NO': 30, 'GUA': 40, 'FRI': 20}

lista_complementos = ['CQ', 'CP', 'NO', 'GUA', 'FRI']

nombres_t = {'PA': 'pastor', 'CHO': 'chorizo', 'SUA': 'suadero',
'LEN': 'lengua', 'BI': 'bistec', 'CO': 'cochinita'}

nombres_t_a = {'G': 'grande', 'M': 'mediana', 'CH': 'chica'}

nombres_c = {'CQ': 'Chicarrón de queso', 'CP': 'Cebollas preparadas',
'NO': 'Nopales', 'GUA': 'Guacamole', 'FRI': 'Frijoles'}

def Mostrar_Menu(tacos, tamaños_aguas, complementos):

    while True:
        print()
        print('MENÚ')
        print('1. Carta')
        print('2. Realizar pedido')
        print('3. Finalizar')
        opc = input('Seleccione una opción: ')

        if opc == '1':
            Mostrar_Carta(tacos, tamaños_aguas, complementos)
        elif opc == '2':
            Realizar_Pedido(tacos, tamaños_aguas, complementos)
        elif opc == '3':
            Finalizar_Pedido()
        else:
            print('Número inválido, intenta de nuevo.')

def Mostrar_Carta(tacos, tamaños_aguas, complementos) :

    # Función que muestra la carta de productos y precios de la taquería.

    print()
    print('TACOS')
    print('Pastor (PA) ------------------ $10')
    print('Chorizo (CHO) ---------------- $15')
    print('Suadero (SUA) ----------------- $25')
    print('Lengua (LEN) ------------------ $30')
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
    print('Cebollas preparadas (CP) ----- $25')
    print('Nopales (NO) ----------------- $30')
    print('Guacamole (GUA) -------------- $40')
    print('Frijoles (FRI) --------------- $20')

    Mostrar_Menu(tacos, tamaños_aguas, complementos)

def Realizar_Pedido(tacos, tamaños_aguas, complementos):
    # Inicializar variables para el pedido
    total_pedido = 0  # Inicializamos el total del pedido en cero

    print()
    print(
    'FAVOR DE UTILIZAR LOS CÓDIGOS DE CADA PRODUCTO PARA REALIZAR SU PEDIDO',
          '(E.G. Taco de Pastor: PA)')

    while True:
        taco_o_no = input('¿Desea agregar tacos a su orden? ')
        if taco_o_no.lower() == 'si':
            while True :
                sabor_taco = input('Sabor de taco: ')
                if sabor_taco not in lista_tacos :
                    print('Código inválido, intente de nuevo.')
                else :
                    while True :
                        cantidad_tacos = input('Cantidad de tacos: ')
                        try :
                            cantidad_tacos = int(cantidad_tacos)
                            break
                        except :
                            print('Error. Introduce un número.')
                    total_pedido += tacos.get(sabor_taco, 0) * cantidad_tacos
                    break
        else:
            sabor_taco = None
            cantidad_tacos = 0

        agua_o_no = input('¿Desea agregar alguna bebida a su orden? ')
        if agua_o_no.lower() == 'si':
            while True :
                sabor_agua = input('Sabor de agua: ')
                if sabor_agua not in lista_aguas :
                    print('Código inválido, intente de nuevo.')
                else :
                    while True :
                        tamaño_agua = input('Tamaño del agua: ')
                        if tamaño_agua not in lista_tamaños_aguas :
                            print('Código inválido, intente de nuevo.')
                        else :
                            while True :
                                cantidad_agua = input('Cantidad de aguas: ')
                                try :
                                    cantidad_agua = int(cantidad_agua)
                                    break
                                except :
                                    print('Error. Introduce un número.')
                            total_pedido += (tamaños_aguas.get(tamaño_agua, 0) *
                            cantidad_agua)
                            break
                    break
        else:
            sabor_agua = None
            tamaño_agua = None
            cantidad_agua = 0

        extra_o_no = input('¿Deseas agregar algún complemento? ')
        if extra_o_no.lower() == 'si':
            while True :
                extra = input('Complemento: ')
                if extra not in lista_complementos :
                    print('Código inválido, intente de nuevo.')
                else :
                    total_pedido += complementos.get(extra, 0)
                    break
        else :
            extra = None

        propina = input('¿Deseas agregar propina? ')
        if propina.lower() == 'si':
            while True :
                try :
                    print('¿Cuánto deseas agregar?')
                    print('INTRODUCE EL PORCENTAJE, SIN SÍMBOLOS')
                    porcentaje = float(input())
                    total_pedido += (porcentaje / 100) * total_pedido
                    break
                except :
                    print('Error. Introduce un número.')
        else :
            porcentaje = 0

        Confirmacion_Pedido(tacos, tamaños_aguas, complementos,
        nombres_c, nombres_t, nombres_t_a, sabor_taco, sabor_agua, tamaño_agua,
        extra, cantidad_agua, cantidad_tacos, propina, porcentaje, total_pedido,
        aguas)

        # Pregunta si desea agregar más elementos al pedido
        continuar_pedido = input(
        '¿Desea agregar más elementos al pedido? (si/no) ')
        if continuar_pedido.lower() != 'si':
            break  # Sal del bucle si no se desea agregar más elementos

        Mostrar_Menu(tacos, tamaños_aguas, complementos)

def Finalizar_Pedido() :

    # Función que imprime un mensaje de confirmación, y además muestra la
    # encuesta de servicio, donde se calificará el servicio en una escala
    # del 1 al 5.

    while True :
        print('¡Gracias por su compra! Su pedido pronto estará listo.')
        calif = input(
        'Por favor, en una escala del 1 al 5 califique el servicio: ')
        if calif == '1' :
            print('En su próximo pedido prometemos un mejor servicio.')
            exit()
        if calif == '2' :
            print('En su próximo pedido prometemos un mejor servicio.')
            exit()
        if calif == '3' :
            print('Gracias por calificar nuestro servicio.')
            exit()
        if calif == '4' :
            print('Gracias por calificar nuestro servicio.')
            exit()
        if calif == '5' :
            print('¡Gracias! Nos da gusto que hayas recibido un buen servicio.')
            exit()
        else :
            print('Número inválido, intenta de nuevo.')

def Confirmacion_Pedido(tacos, tamaños_aguas, complementos,
nombres_c, nombres_t, nombres_t_a, sabor_taco, sabor_agua, tamaño_agua, extra,
cantidad_agua, cantidad_tacos, propina, porcentaje, total_pedido,
aguas) :
    # Imprime la confirmación del pedido
    print()
    print('CONFIRMACIÓN: ')
    if sabor_taco :
        if cantidad_tacos > 1 :
            print(cantidad_tacos, 'tacos de', nombres_t.get(sabor_taco, 0),
            '- $', tacos[sabor_taco] * cantidad_tacos)
        elif cantidad_tacos == 1 :
            print('Taco de', nombres_t.get(sabor_taco, 0), '- $',
            tacos[sabor_taco] * cantidad_tacos)
    if tamaño_agua :
        if cantidad_agua > 1 :
            print(cantidad_agua, 'aguas',
            nombres_t_a.get(tamaño_agua, 0) + 's',
            'de', aguas.get(sabor_agua, 0), '- $',
            tamaños_aguas[tamaño_agua] * cantidad_agua)
        elif cantidad_agua == 1 :
            print('Agua', nombres_t_a.get(tamaño_agua, 0), 'de',
            aguas.get(sabor_agua, 0),
            '- $', tamaños_aguas[tamaño_agua] * cantidad_agua)
    if extra :
        print(nombres_c.get(extra, 0), '- $', complementos[extra])
    else:
        print('Sin complemento')
    if propina :
        print('Propina:', porcentaje, '%')
    else :
        print('Cuenta cerrada')
    print('Total:', total_pedido)

Mostrar_Menu(tacos, tamaños_aguas, complementos)
