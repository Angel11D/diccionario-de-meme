meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una forma de reírse",
            "SHEESH": "Ligeria desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }

word = input("Escribe una palabra que no entiendas: ").upper()


if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("El significado es: ", meme_dict)
else:
    print("Palabra no encontrada")
    # ¿Qué hacer si no se encuentra la palabra?
