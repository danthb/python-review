e1 = {'nombre': 'Juan', 'matematicas': 4.0,
      'español': 3.0, 'ciencias': 3.0, 'literatura': 5.0, 'arte': 4.0}
e2 = {'nombre': 'Ana', 'matematicas': 1.0,
      'español': 5.0, 'ciencias': 4.0, 'literatura': 5.0, 'arte': 5.0}
e3 = {'nombre': 'Pedro', 'matematicas': 3.0,
      'español': 3.0, 'ciencias': 3.0, 'literatura': 3.0, 'arte': 3.0}
e4 = {'nombre': 'María', 'matematicas': 5.0,
      'español': 5.0, 'ciencias': 5.0, 'literatura': 5.0, 'arte': 5.0}
e5 = {'nombre': 'Jorge', 'matematicas': 5.0,
      'español': 5.0, 'ciencias': 5.0, 'literatura': 5.0, 'arte': 5.0}


def mejor_de_cada_curso(e1: dict, e2: dict, e3: dict, e4: dict, e5: dict) -> dict:
    estudiantes = [e1, e2, e3, e4, e5]
    quintil = []
    mejor_promedio = 0
    promedio = 0

    # Calculate grade average for each student and make a quintil stack student
    for e in estudiantes:
        promedio = 0
        suma = 0
        for calificacion in e.keys():
            if calificacion != 'nombre':
                suma += e[calificacion]
        promedio = round(suma / (len(e)-1))
        e['promedio'] = promedio

        if e['promedio'] > mejor_promedio:
            mejor_promedio = e['promedio']
    # If there are more than one student with the same average,
    for e in estudiantes:
        if e['promedio'] == mejor_promedio:
            quintil.append(e)
    if len(quintil) == 1:
        return quintil[0]
    else:
        quintil.sort(key=lambda x: x['nombre'])
        return quintil[0]


print('El mejor del curso es' + str(mejor_de_cada_curso(e1, e2, e3, e4, e5)))
