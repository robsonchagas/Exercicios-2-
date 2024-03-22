#Programa que pede para o usuário o nome de 13 pessoas
i = 0
lista = []
while i < 13:
  nome = input("Digite o nome da pessoa: ")
  i = i + 1
  lista.append(nome)
print(lista)

#Programa que imprime número de 0 a 1000
i = 0
while i < 100:
  i = i + 1
  print(i)

#Programa que imprime os números pares de 0 a 1000
i = 0
while i < 100:
  i = i + 2
  print(i)

#Programa que imprime números de 0 a 1000 em ordem decrescente
i = 100
while i > 0:
  i = i - 1
  print(i)

#Programa que solicita o time de 10 usuários, ao final imprimir o total de cada
i = 0
lista = []
while i < 10:
  print("Informe o time do usuário", i + 1)
  time = input("Digite o time: ")
  lista.append(time)
  i = i + 1
total_times = {}
for time in lista:
  total_times[time] = total_times.get(time, 0) + 1
print(total_times)

#Programa para digitar 20 números e ao final imprimir todos números digitados
i = 0
lista = []
while i < 20:
  numero = float(input("Digite o número: "))
  lista.append(numero)
  i = i + 1
print(lista)

#Programa para solicitar 10 números e ao final somar todos
print("Digite 10 números:")
soma = 0
for i in range(10):
  numero = float(input("Digite o número: "))
  soma = soma + numero
print(soma)

#Programa que solicita quantos números será digitados e ao final validade se é neg, pos ou zero
quant = int(input("Digite a quantidade de números: "))
i = 0
for i in range(quant):
  numero = float(input("Digite o número: "))
  if numero > 0:
    print("O número é positivo")
  else:
    if numero < 0:
      print("O número é negativo")
    else:
      print("O número é zero")

#Programa que pede dois valores e imprima números pares entre eles, caso negativo encerra
i = 0
val1 = int(input("Digite o primeiro valor:"))
val2 = int(input("Digite o segundo valor:"))
if val1 > 0 and val2 > 0:
  for i in range(val1, val2 + 1):
    if i % 2 == 0:
      print(i)
else:
  print("Valor inválido")

#Programa que some os valores de 0 até 198
soma = 0
for i in range(198):
  soma += i
print("A soma dos valores de 0 até 198 é:", soma)

#Programa que imprime a soma dos valores pares e ímpares
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
soma_par = 0
soma_impar = 0
for i in range(val1, val2 + 1):
    if i % 2 == 0:
        soma_par += i
    else:
        soma_impar += i
print("A soma dos valores pares é:", soma_par)
print("A soma dos valores ímpares é:", soma_impar)

#Programa para digitar números positivos quando negativo encerrar
lista = []
while True:
  numero = float(input("Digite um número positivo (ou um número negativo para encerrar): "))
  if numero < 0:
    break
  lista.append(numero)
print(lista)

#Programa que calcule o fatorial de um número não permitindo negativos
numero = int(input("Digite um número não negativo para calcular o fatorial: "))
if numero < 0:
    print("Número inválido. Por favor, insira um número não negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print("O fatorial de", numero, "é:", fatorial)

#Programa que diga se o número é primo ou não
numero = int(input("Digite um número inteiro: "))
if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(numero, "não é um número primo.")
            break
    else:
        print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")

#Programa que imprime os números primos entre 0 a 200 e soma no final
primos = []
for num in range(2, 201):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)
print("Números primos entre 0 e 200:")
for primo in primos:
    print(primo, end=" ")
soma_primos = sum(primos)
print("\nA soma dos números primos é:", soma_primos)