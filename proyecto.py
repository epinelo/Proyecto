# Se pregunta al usuario que sabor de tacos ordenará.

sabor_taco = input('¿Cuál es el sabor de tu taco? ')

# Se pregunta al usuario cuántos tacos ordenará y el valor lo hacemos de tipo
# entero.

cantidad_tacos = int(input('¿Cuántos tacos quieres? '))

# Se pregunta al usuario sobre el precio del taco del sabor elegido y el
# valor lo hacemos de tipo flotante.

precio_taco = float(input('¿Cuánto cuesta tu taco? '))

# Se pregunta al usuario que sabor de agua ordenará.

sabor_agua = input('¿Cuál es el sabor de tu agua? ')

# Se pregunta al usuario el tamaño del agua que ordenará.

tamaño_agua = input('¿De que tamaño deseas tu agua? ')

# Se pregunta al usuario sobre el precio del tamaño del agua que ordenará
# y el valor lo hacemos de tipo flotante.

precio_agua = float(input('¿Cuánto cuesta tu agua? '))

# Se pregunta al usuario si desea agregar un complemento, dando dos
# opciones disponibles

extra = input('¿Deseas complementar con chicharrón de queso o cebollas preparadas? ')

# Si el usuario decide agregar un complemento el programa buscará un "si" por respuesta.

# Hago uso de la funcion lower() para que el programa lea la palabra "si"
# en caso de que se escirba en mayúsculas o minúsculas y sepa que es la misma palabra.

# En caso de que el usuario no deseé un complemento, cualquier otro tipo de
# respuesta hará que el programa continúe.

if extra.lower() == 'si' :

#   Se pregunta al usuario que complemento desea agregar a la orden.

    extra = input('¿Qué complemento deseas? ')

#   Se pregunta al usuario sobre el precio del complemento elegido y el valor
#   lo hacemos de tipo flotante.

    precio_extra = float(input('¿Cuánto cuesta tu extra? '))

#    Asigno a la variable "total" el precio de un taco por la cantidad de
#    tacos, más el precio del agua y el extra.

    total = (precio_taco * cantidad_tacos) + precio_agua + precio_extra

else :

#    En el caso de no elegir ningiun complemento, solamente se asigna a "total"
#    el precio de un taco por la cantidad de tacos, más el precio del agua.

    total = (precio_taco * cantidad_tacos) + precio_agua

# Se pregunta al usuario si desea agregar propina.

propina = input('¿Deseas agregar propina? ')

# Si el usuario decide agregar un complemento el programa buscará un "si" por respuesta.

# Hago uso de la funcion lower() para que el programa lea la palabra "si"
# en caso de que se escirba en mayúsculas o minúsculas y sepa que es la misma palabra.

if propina.lower() == 'si' :

#   Se pregunta al usuario cuánto porcentaje de propina desea agregar y el
#   valor lo hacemos de tipo flotante.

    porcentaje = float(input('¿Cuánto deseas agregar? (Introduce el porcentaje, sin símbolos) '))

#   Asigno a la variable "total" el porcentaje de propina más el valor
#   anterior de "total".

    total = (total * (porcentaje / 100)) + total

#   Se imprime el monto total a pagar.

    print('El monto a pagar es de $', total)

else:

#   En caso de no agregar propina solo se imprime el valor de "total"
#   anterior (sin propina) como monto total a pagar.

    print('El monto a pagar es de $', total)
