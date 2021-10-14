import  calculadora_indices  as  calc 

peso = float(input('Ingrese el valor del pero en (Kg): '))
altura = float(input('Ingrese el valor de la altura en (m): '))

print('El valor de IMC es: ',calc.calcular_IMC(peso,altura))