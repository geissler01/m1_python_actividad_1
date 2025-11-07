print('*** Heladeria "Frosty" ***\n')
print('Sabores y precios')
print('Chocolate => 4000')
print('Vainilla  => 3500\n')
print('Topping   => 1000 opcional')

while True:
    sabor = int(input('¿Qué sabor desea?: Marque 1) para CHOCOLATE o 2) para VAINILLA: '))

    if sabor == 1:
        opcional = int(input('Marque 1) si desea Topping o 2) si no lo quiere: '))
        if opcional == 1:
            print(f'El helado de Chocolate con Topping cuesta {4000+1000} pesos')
        else:
            print(f'El helado de chocolate cuesta {4000}')
    elif sabor == 2:
        opcional = int(input('Marque 1) si desea Topping o 2) si no lo quiere: '))
        if opcional == 1:
            print(f'El helado de Chocolate con Topping cuesta {3500+1000} pesos')
        else:
            print(f'El helado de Vaililla cuesta {3500}')
    else :
        print('Por favor ingrese un sabor disponible')
        continue
    compra= int(input('¿Desea realizar otra compra?. MARQUE "1" si desea PARAR o cualquier otro numero para CONTINUAR: '))
    if compra == 1:
        break

