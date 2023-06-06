def calculadora(a, b):
	k = input('Deseja fazer qual operacao? ').upper()
	if k == 'SOMA':
		return print(a + b)
	if k == 'SUBTRACAO':
		return print(a - b)
	if k == 'MULTIPLICACAO':
		return print(a * b)
	if k == 'DIVISAO':
		return print(a / b)



print('='*25, 'CALCULADORA 2000', '='*25)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
calculadora(n1, n2)
