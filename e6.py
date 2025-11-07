print('*** Parqueadero "RapidCar" ***\n')

print('--- Tarifas ---')
print('0 a 5 horas: 2.000 x hora')
print('5 horas o mas: 2.000 x hora + multa fija de 5.000\n')

while True:
    horas = int(input('Ingrese el numero de horas de parqueo: '))
    while horas < 0:
        print('Error: Por favor ingrese un numero de horas correcto')
        horas = int(input('Ingrese el numero de horas de parqueo: '))

    if horas >= 0 and horas < 5:
        print(f'El costo del parqueadero para su vehiculo es = {(2000*horas)}')
        
    else :
        print(f'El costo del parqueadero para su vehiculo es = {(2000*horas)+5000}')

    if horas >= 0:
         break