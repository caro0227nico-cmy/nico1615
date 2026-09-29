palabras = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in palabras.keys():
    print(palabras[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("la palabra no ha sido encontrada")
    # ¿Qué hacer si no se encuentra la palabra?

