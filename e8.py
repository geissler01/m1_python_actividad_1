print('*** Empresa "TecnoPlus" ***\n')

#nota1 = float(input('Ingrese la calificacion obtenida en Prueba técnica: '))
#nota2 = float(input('Ingrese la calificacion obtenida en Prueba lógica: '))

# Opcion 1
while True:
    nota1 = float(input('Ingrese la calificacion obtenida en Prueba técnica: '))
    if nota1 < 0 or nota1 > 5:
        print('Error: por favor ingrese una nota valida (0.0 - 5.0)')
        nota1 = float(input('Ingrese la calificacion obtenida en Prueba técnica: '))
    if nota1 >=0 and nota1<=5:
        break
# Opcion 2, mas elegante
while True:
    nota2 = float(input('Ingrese la calificacion obtenida en Prueba lógica: '))
    while nota2 < 0 or nota2 > 5:
        print('Error: por favor ingrese una nota valida (0.0 - 5.0)')
        nota2 = float(input('Ingrese la calificacion obtenida en Prueba lógica: '))
    break

nota_final = (nota1*0.7)+(nota2*0.3)

if nota_final >= 3:
    print(f'\nFelicidades, haz APROBADO con una nota de {round(nota_final, 2)}')
elif nota_final >= 2 and nota_final < 3:
    print(f'\nREVISIÓN: Tu nota final es {round(nota_final, 2)}')
else:
    print(f'\nREPROBADO: Tu nota final es {round(nota_final, 2)}')
