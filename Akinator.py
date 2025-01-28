class Pregunta:
    def __init__(self, texto, si=None, no=None):
        self.texto = texto
        self.si = si
        self.no = no


def jugar_akinator(pregunta):
    respuesta = input(pregunta.texto + " (si/no): ").lower()
    if respuesta == 'si':
        if pregunta.si is None:
            print("¡Adiviné!")
        else:
            jugar_akinator(pregunta.si)
    elif respuesta == 'no':
        if pregunta.no is None:
            print("No he podido adivinar. ¿Quién es el personaje?")
            nuevo_personaje = input("Nuevo personaje: ")
            nueva_pregunta = input(f"Proporciona una pregunta para distinguir {nuevo_personaje} de {pregunta.texto}: ")
            respuesta_nueva_pregunta = input(f"¿Cuál es la respuesta para {nuevo_personaje}? (si/no): ")
            if respuesta_nueva_pregunta == 'si':
                pregunta.si = Pregunta(nueva_pregunta, si=Pregunta(nuevo_personaje))
            else:
                pregunta.no = Pregunta(nueva_pregunta, no=Pregunta(nuevo_personaje))
        else:
            jugar_akinator(pregunta.no)
    else:
        print("Respuesta no válida. Por favor, responde 'si' o 'no'.")
        jugar_akinator(pregunta)


# Ejemplo de uso
raiz_pregunta = Pregunta("¿Tu personaje es una figura histórica?", si=Pregunta("¿Tu personaje es del siglo XX?"))
jugar_akinator(raiz_pregunta)