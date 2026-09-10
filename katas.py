"""
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario
con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
"""

def fn1(input):
    output = {}
    for word in input:
        if (word != " "):
            output[word] = output.get(word, 0) + 1
    return output

"""
Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""

lista_1 = [6,0,4,1,1,6,1,5,0]

def doble(inputs):
    outputs=inputs*2
    return outputs

resultado = []

resultado = list(map(doble,lista_1))

print(resultado)

