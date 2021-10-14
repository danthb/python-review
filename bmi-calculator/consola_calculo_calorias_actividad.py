import  calculadora_indices  as  calc 

peso = float(input('Ingrese el valor del pero en (Kg): '))
altura = float(input('Ingrese el valor de la altura en (cm): '))
edad = int(input('Ingrese el valor de la edad en (años): '))
valor_genero = float(input('Ingrese el valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161. : '))
valor_actividad = float(input('''Ingrese el valor que depende de la actividad física semanal:  
                            • 1.2: poco o ningún ejercicio 
                            • 1.375: ejercicio ligero (1 a 3 días a la semana) 
                            • 1.55: ejercicio moderado (3 a 5 días a la semana) 
                            • 1.725: deportista (6 -7 días a la semana) 
                            • 1.9: atleta (entrenamientos mañana y tarde)  '''))

print('La cantidad de calorias en actividad es: ',calc.calcular_calorias_en_actividad(peso,altura, edad, valor_genero, valor_actividad), 'cal')