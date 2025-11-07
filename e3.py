print('*** Gimnasio "Solo Leveling Fit" ***\n')
#dias = int(input('¿Cuántos días entrenaste esta semana?: '))

while True:
    dias = int(input('¿Cuántos días entrenaste esta semana?: '))
    if dias < 0 or dias > 7:
         print('Por favor ingrese una cantidad valida')
         continue
    elif dias >= 4:
         print('"Excelente disciplina": ganas 1 PUNTO DE ENERGÍA')
    elif dias >= 2 and dias <=3:
         print('Bien, pero puedes dar más')
    else :
         print('No aflojes, tú puedes nejorar')
    if dias >=0 and dias <=7:
         break