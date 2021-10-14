import  calculadora_indices  as  calc 

peso = float(input('Ingrese el valor del pero en (Kg): '))
altura = float(input('Ingrese el valor de la altura en (cm): '))
edad = int(input('Ingrese el valor de la edad en (años): '))
valor_genero = float(input('Ingrese el valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161. : '))

print('La cantidad de calorias en reposo es: ',calc.calcular_calorias_en_reposo(peso,altura, edad, valor_genero), 'cal')