#constanza torres
#12/05/2025

# Básico: imprime todos los números enteros del 0 al 100
for i in range(101):
    print(i)

# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for i in range(2, 501, 2):
    print(i)

# Contando Vanilla Ice: imprime números del 1 al 100 con condiciones especiales
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Wow. Número gigante a la vista: suma los números pares del 0 al 500,000
suma_total = sum(range(0, 500001, 2))
print("La suma total es:", suma_total)

# Regrésame al 3: imprime los números positivos desde 2024 en cuenta regresiva de 3 en 3
for i in range(2024, 0, -3):
    print(i)

# Contador dinámico: imprime números múltiplos de 'multiplo' entre 'numInicial' y 'numFinal'
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
