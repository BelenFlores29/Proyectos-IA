#inicialización de estado
import re
import time

state=0
Salida=1
intentos =0
continuar = ''

while Salida:
    if state==0:
        print("\n\nHOLA, SOY EL CHATBOT DE PELÍCULAS")
        time.sleep(1.5)
        print("\nNUESTRA SELECCIÓN PARA TI:\n\n" 
                "a) Las películas del momento\n"
                "b) Recomendación personalizada\n\n")

        opcion=input("Selecciona una opción:\t")
        opcion = opcion.lower()
        while True:
            if opcion == 'a':
                state=1
                intentos=0
                break
            elif opcion == 'b':
                state=2
                intentos=0
                break
            else:
                intentos+=1
                if intentos >= 5:
                    continuar = input("No te he comprendido por favor vuelve a repetir tu respuesta. \n¿Deseas continuar? (sí/no) \n\t\t\t")
                    if continuar.lower() == 'si':
                        intentos = 0
                    else:
                        print("Vuelve pronto")
                        Salida=0
                        break
                else:
                    print("No te he comprendido por favor vuelve a repetir tu respuesta")
                    opcion=input()
                    continue


    if state == 1:
        print("\nLAS PELICULAS QUE ESTAN EN LAS CARTELERA ACTUALMENTE: \n"
            "- Vidas pasadas\n"
            "- Madame Web\n"
            "- Dunn (Parte 2)\n"
            "- Demon Slayer: Kimetsu no Yaiba - To the Hashira Training\n"
            "- Bob Marley: La leyenda\n"
            "- Alicia en el País de las Pesadillas\n"
            "- Atrapados en lo profundo\n"
            "- Desaparecer por Completo\n"
            "- El gran cambio\n"
            "- Ferrari\n"
            "- Nadie es lo que parece\n"
            "- Noche de bodas\n"
            "- Todas menos tú\n"
            "- The Chosen: T4 EP 1 y 2\n"
            "\n\n-------------------------------------------------------------------------\n"
            )
        state = 0

    if state == 2:
        print("\nA CONTINUACION TE MOSTRAMOS NUESTRO MENU DE RECOMENDACIONES: ")
        print (
            "\na) Recomendación por género"
            "\nb) Recomendación por actores"  
            "\nc) Recomendación por plataforma" 
        )        
        Recomendacion = input("\nSelecciona una letra dependiendo del tipo de recomendación que quieras: ")
        Recomendacion = Recomendacion.lower()

        if Recomendacion == 'a':
            print("a) Accion\n"
            "b) Anime\n" 
            "c) Cine de intriga\n"
            "d) Clasicas\n"
            "e) Comedia\n"
            "f) Drama\n" 
            "g) Para ver en familia\n"
            "h) Fantasia\n"
            "i) Ficcion\n"
            "j) Mexicanas\n"
            "k) Navideñas\n"
            "l) Romance\n"
            "m) Terror\n")

            Genero = input("\nSELECCIONA TU GENERO: \n")
            Genero.lower()


            if Genero == 'a':
                print ("\n------------------ACCION---------------\n"
                    "- Duro de Matar\n"
                    "- Matrix\n"
                    "- Mad Max: Furia en la Carretera\n"
                    "- Terminator 2: Judgment Day\n"
                    "- John Wick\n"
                    "-------------------------------------\n\n"
                    )
                state = 0
            
            elif Genero == 'b': 
                print ("------------------ANIME---------------\n"
                    "- El viaje de Chihiro\n"
                    "- Mi vecino Totoro \n"
                    "- Akira\n"
                    "- Ghost in the Shell\n"
                    "- Your Name\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'c': 
                print ("----------------INTRIGA---------------\n"
                    "- Seven\n"
                    "- El Silencio de los Corderos\n"
                    "- Memento\n"
                    "- Prisioneros\n"
                    "- El Orfanato\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'd': 
                print ("----------------CLASICAS--------------\n"
                    "- El Mago de Oz\n"
                    "- Titanic\n"
                    "- Harry Potter y El prisionero de Azkaban\n"
                    "- Crepusculo\n"
                    "- Chicas Pesadas\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'e': 
                print ("----------------COMEDIA---------------\n"
                    "- Son Como Niños\n"
                    "- Shrek 2\n"
                    "- ¿...Y Donde Están las Rubias?\n"
                    "- NORBIT\n"
                    "- Scary Movie 1\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'f': 
                print ("-----------------DRAMA----------------\n"
                    "- Casa Grande\n"
                    "- El Juego Bonito\n"
                    "- El lugar de la Esperanza\n"
                    "- Aftersun\n"
                    "- Hasta el Hueso\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'g': 
                print ("---------PARA VER EN FAMILIA---------\n"
                    "- Benji\n"
                    "- Marley y Yo\n"
                    "- Sing\n"
                    "- Wonder\n"
                    "- Hachiko\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'h': 
                print ("---------------FANTASIA---------------\n"
                    "- Harry Potter y El Caliz de fuego\n"
                    "- Peter Pan\n"
                    "- El increíble Castillo Vagabundo\n"
                    "- Los Pitufos en la Aldea Perdida\n"
                    "- El Señor de los anillos\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'i': 
                print ("----------------FICCION---------------\n"
                    "- El Planeta de los Simios\n"
                    "- Presagio\n"
                    "- Ocultos por la Luna\n"
                    "- Spiderman\n"
                    "- Planeta Prohibido\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'j': 
                print ("----------------MEXICANAS---------------\n"
                    "- Niñas mal\n"
                    "- Como si fuera la promera vez\n"
                    "- Como caídos del cielo\n"
                    "- La Casa de las Flores: La Película\n"
                    "- Mirreyes y Godinez\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'k': 
                print ("----------------NAVIDEÑAS---------------\n"
                    "- El expreso polar\n"
                    "- Amor de calendario\n"
                    "- Mi pobre angelito\n"
                    "- Intercambio de princesas\n"
                    "- Un milagro navideño para Daisy\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'l': 
                print ("----------------ROMANCE---------------\n"
                    "- Cuestión de Tiempo\n"
                    "- Call me by your name\n"
                    "- Titanic\n"
                    "- Orgullo y Prejuicio\n"
                    "- Diario de una pasión\n"
                    "-------------------------------------\n\n"
                    )
                state = 0

            elif Genero == 'm': 
                print ("----------------TERROR---------------\n"
                    "- La noche del demonio 3\n"
                    "- Corre\n"
                    "- El exorcista\n"
                    "- Psicosis\n"
                    "- El conjuro: Expediente Warren\n"
                    "-------------------------------------\n\n"
                    )
                state = 0


        if Recomendacion == 'b':
            print ("\n----------------ADAM SANDLER-------------\n"
                "- Como si fuera la primera vez\n "
                "- Son Como niños\n"
                "- El astronauta\n"
                "- Una esposa de mentira\n"
                "- Happy Gilmore\n"
                "------------------------------------------\n\n"

                "\n----------LEONARDO DICAPRIO------------\n"
                "- Titanic\n "
                "- El lobo de Wall Street\n"
                "- LA isla siniestra\n"
                "- El origen\n"
                "- El Gran Gatsby\n"
                "------------------------------------------\n\n"

                "\n-----------------EMMA WATSON----------------\n"
                "- Harry Potter y la Piedra Filosofal\n "
                "- Mujercitas\n"
                "- La Bella y la Bestia\n"
                "- Las Ventajas de ser Inviisible\n"
                "- El Círculo\n"
                "------------------------------------------\n\n"

                "\n--------------LILY COLLINS--------------\n"
                "- Los imprevistos del amor\n "
                "- Casadores de Sombras: Ciudad de Hueso\n"
                "- \Editando el amorn"
                "- Hasta el Hueso\n"
                "- Un sueño posible\n"
                "------------------------------------------\n\n"

            )
            state = 0


        if Recomendacion == 'c':
            print ("\n-----------------NETFLIX----------------\n"
                "- Roma \n "
                "- El Irlandés\n"
                "- Bird Box\n"
                "- La La Land\n"
                "- The Trial of the Chicago 7\n"
                "------------------------------------------\n\n"


                "\n-----------------HBO MAX----------------\n"
                "- Game of Thrones: The Movie \n "
                "- JOKER\n"
                "- Parasite\n"
                "- The Shape of Water\n"
                "- \n"
                "------------------------------------------\n\n"


                "\n--------------AMAZON PRIME-------------\n"
                "- Babylon \n "
                "- Ultima noche en el Soho\n"
                "- Jhon Wick 4\n"
                "- El hijo\n"
                "- Creed 3\n"
                "------------------------------------------\n\n"
            )
            state = 0



