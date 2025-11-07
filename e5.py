print('*** Libreria "El Saber" ***\n')

print('Costo por Libro =  25.000 pesos')
print('Estudiantes     => 15% descuento')
print('Cupon "LIBRO10" => 10% descuento adicional \n')

precio_1 = 25000
precio_2 = 0.85*precio_1
precio_3 = 0.9*precio_2

estudiante = int(input('Marque "1" si ES ESTUDIANTE o cualquier otro numero si NO LO ES: '))

if estudiante == 1:
    cupon = int(input('Marque "1" si tiene CUPON de descuento, o cualquier numero si NO LO TIENE: '))
    if cupon == 1:
        codigo = input('Ingrese su CUPON de descuento: ')
        if codigo == 'LIBRO10':
            print(f'El costo final por libro para usted es: {precio_3}')
        else:
            print(f'Su CUPON no aplica para descuento adicial. Precio final por libro = {precio_2}')
    else:
        print(f'Precio por libro = {precio_2}')
else:
    print(f'El precio por libro es = {precio_1}')
