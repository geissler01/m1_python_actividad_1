print('*** Restaurante "El Sabor Colombiano" ***\n')

print('Menú: $12.000')
print('--- Opciones bebida ---')
print('SI  => $3.000')
print('NO  => $0')
print('IVA => 8%\n')

bebida = input('¿Desea incluir bebida al Menú?: escriba si / no: ')
if bebida.lower() == 'si':
    costo = 12000 + 3000
    costo_IVA = costo + (0.08*costo)
    print(f'Costo sin IVA = {costo}')
    print(f'Costo con IVA = {costo_IVA}')

else:
    costo = 12000
    costo_IVA = costo + (0.08*costo)
    print(f'Costo sin IVA = {costo}')
    print(f'Costo con IVA = {costo_IVA}')
