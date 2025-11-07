print('*** Panederia Don Pancho ***\n')
print('Si compra mas de 20 panes => 10% descuento')
print('Si compra mas de 50 panes => 20% descuento\n')

while True:
    panes = int(input('Ingrese la cantidad de panes que desea comprar: '))
    if panes <= 0:
         print('Por favor ingrese una cantidad valida')
         continue
    elif panes > 0 and panes < 20:
         total = panes*(300)
         print(f'{panes} cuestan {total} pesos')
    elif panes >=20 and panes <50:
         total = panes*(0.9*300)
         print(f'{panes} cuestan {total} pesos')
    else :
         total = panes*(0.8*300)
         print(f'{panes} cuestan {total} pesos')
    compra= int(input('¿Desea realizar otra compra?. MARQUE "1" si desea parar o cualquier otro numero para continuar comprando: '))
    if compra == 1:
        break


