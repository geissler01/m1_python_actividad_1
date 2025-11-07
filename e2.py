print('*** Valor entradas a CINE ***\n')

while True:
    edad = int(input('Ingrese la edad del cliente (años): '))
    while edad < 0 or edad > 125:
        print('Error: Por favor ingrese la edad correcta')
        edad = int(input('Ingrese la edad del cliente (años): '))
    if edad >0 and edad <= 5:
        print('El cliente tiene menos de 5 años. Puede entrar GRATIS')
    elif edad >=5 and edad<=11:
        print('Valor de la entrada "5000" pesos')
    elif edad >=12 and edad<=59:
        print('Valor de la entrada "8000" pesos')
    else:
        print('Valor de la entrada "4000" pesos (descuento adulto mayor)')
    edad = int(input('¿Desea ingresar otro cliente?. MARQUE "1" si desea PARAR o cualquier otro numero para continuar: '))
    if edad == 1:
        break

