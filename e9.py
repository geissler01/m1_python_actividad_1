print('*** Supermercado "AhorroMax" ***\n')

print('Costo por producto =  $2.000')
print('10 a 29 unidades   => 5% descuento')
print('30 unidades o mas  => 15% descuento')
print('Costos de envio    => $5.000')
print('Envío gratis por compras mayores de $50.000\n')

precio_1 = 2000
precio_2 = 0.95*precio_1
precio_3 = 0.85*precio_1

# Validacion de cantidad
while True:
    cantidad = int(input('Ingrese la cantidad de productos que desea comprar: '))
    while cantidad < 0:
        print('Error: por favor ingrese una cantidad valida')
        cantidad = int(input('Ingrese la cantidad de productos que desea comprar: '))
    break

if cantidad >= 10 and cantidad < 30:
    costo = cantidad * precio_2
    if costo < 50000:
        print(f'El costo final de su compra es: {costo + 5000} (incluye costos de envío)')
    else:
        print(f'El costo final de su compra es: {costo} (Envío gratis)')

elif cantidad >= 30:
    costo = cantidad * precio_3
    if costo < 50000:
        print(f'El costo final de su compra es: {costo + 5000}')
    else:
        print(f'El costo final de su compra es: {costo } (Envío gratis)')
else:
    costo = cantidad * precio_1
    print(f'El costo final de su compra es: {costo + 5000} (incluye costos de envío)')

