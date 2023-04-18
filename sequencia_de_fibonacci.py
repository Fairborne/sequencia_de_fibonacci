# Calculando a sequência
seq = []

num = int(input("Digite um número: "))
seq.append(0)
seq.append(num)

for i in range(1, 9):
    soma = seq[i] + seq[i-1]
    seq.append(soma)

print(f"A sequência de Fibonacci é = {seq}")

# Analisando se o número informado faz parte da sequência de Fibonacci
fibonacci = list([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

i = 0

while i < len(fibonacci):
    if fibonacci == num:
        print("O número digitado faz parte da sequência de Fibonacci.")
        break
    i = i + 1
else:
    print("O número digitado não faz parte da sequência de Fibonacci.")