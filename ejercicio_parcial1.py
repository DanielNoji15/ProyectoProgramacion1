import random

def es_inteligente(numero):
    texto = str(numero)
    for digito in texto:
        if int(digito) % 2 != 0:
            return False
    return True

def genera_numeros(cuantos):
    numeros = []
    resultados = []
    for _ in range(cuantos):
        numero = random.randint(0, 999)
        numeros.append(numero)
        resultados.append(es_inteligente(numero))
    return numeros, resultados

def muestra_resultados(numeros, resultados):
    salida = f"Estos son los números que vamos a revisar: {', '.join(map(str, numeros))}\n"
    salida += "\n".join(f"{numeros[i]}: {'sí' if resultados[i] else 'no'}" for i in range(len(numeros)))
    print(salida)

# Le pedimos al usuario cuántos números quiere
try:
    cantidad = int(input("Oye,¿cuántos números quieres revisar? "))
    if cantidad <= 0:
        print("pero que no sea negativo")
    elif cantidad > 10000:
        print("pero que sea menor que 1000")
    else:
        numeros, resultados = genera_numeros(cantidad)
        muestra_resultados(numeros, resultados)
except ValueError:
    print("metalo pues")