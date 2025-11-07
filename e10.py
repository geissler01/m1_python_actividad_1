print('***\n Club "Noche Estelar" ***\n')

print('--- Reglas ----')
print('Edad >= 18 -- Puede entrar solo si tiene documento')
print('Edad < 18  -- "Entrada denegada"')
print('Si tiene 18 o mas, pero no tiene documento => "Debe presentar documento"\n')

# Validacion de datos
while True:
    edad = int(input('¿Cuántos años tiene el cliente?: '))
    while edad < 0 or edad > 125:
        print('Error: Ingrese edad nuevamente')
        edad = int(input('¿Cuántos años tiene el cliente?: '))
    break

if edad >= 18:
    documento = input('¿tiene documento?: si / no : ')
    if documento.lower() == 'si':
        print('Adelante, puede pasar')
    else:
        print('No puede pasar hasta que muestre el documento')
else:
    print('Entrada denegada')
