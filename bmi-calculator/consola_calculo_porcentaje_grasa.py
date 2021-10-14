import  calculadora_indices  as  calc 

peso = float(input('Ingrese el valor del pero en (Kg): '))
altura = float(input('Ingrese el valor de la altura en (m): '))
edad = int(input('Ingrese el valor de la edad en (años): '))
valor_genero = float(input('Ingrese en  caso de ser masculino debe ser  10.8  y  en  caso  de  ser  femenino  debe  ser  0: '))
print('El porcentaje de grasa es: ',calc.calcular_porcentaje_grasa(peso,altura, edad, valor_genero), '%')