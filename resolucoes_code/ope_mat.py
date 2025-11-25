# Solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
while True:
  print('Selecione uma operacao:')
  print('1 - Soma')
  print('2 - Subtração')
  print('3 - Multiplicão')
  print('4 - Divisão')
  print('0 - Encerrar')
  op = int(input())
  if op == 0:
    break;
  valor1 = int(input('Digite o valor 1: '))
  valor2 = int(input('Digite o valor 2: '))
  if op == 1:
    print(valor1 + valor2)
  elif op == 2:
    print(valor1 - valor2)
  elif op == 3:
    print(valor1 * valor2)
  elif op == 4:
    print(valor1 / valor2)
