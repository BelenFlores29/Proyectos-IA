import time
import random 


Lista = ['TABASCO', 'TAMAULIPAS', 'AGUASCALIENTES', 'COLIMA', 'YUCATAN', 'GUANAJUATO', 'MONTERREY', 
        'CHIAPAS', 'TLAXCALA', 'NAYARIT', 'JALISCO', 'VERACRUZ', 'OAXACA', 'SINALOA', 'SONORA', 'COAHUILA', 
        'CHIHUAHUA', 'PUEBLA', 'QUERETARO', 'TAMAULIPAS']
nom = input ("\n\n\t¿CUAL ES TU NOMBRE?\n")
nombre = nom.upper()

print("\n¡HOLA "+nombre, "LLEGÓ EL MOMENTO DE JUGAR AL AHORCADO!\n")

time.sleep(1)
print("TU PALABRA ES UNO DE LOS ESTADO DE MÉXICO")
print("-------------COMIENZA A ADIVINAR------------------")
time.sleep(0.5)
print("\nTU PALABRA ES: ")
time.sleep(0.5)
palabra = random.choice(Lista)
tupalabra=''

vidas = 5 

while vidas > 0 :
    fallas = 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end = "")
        
        else: 
            print("*", end = "")
            fallas+=1
    if fallas == 0:
        print("\n\n¡FELICIDADES CAMPEON, HAS GANADO!")
        break

    letra = input("\nIntroduce tu mejor letra: ")
    tuletra = letra.upper()
    tupalabra += tuletra

    if tuletra not in palabra:
        vidas -=1
        print ("\nTE HAS EQUIVOCADO")
        print("\nTIENES ", +vidas," VIDAS\n")

    if vidas == 0:
        print("\nBUEN INTENTO PERDEDOR, NOS VEMOS LA PRÓXIMA")
        print("""
       ___
      |   |
     _O/  |
      |   |
     / \  |
    ______|
        """)
    elif vidas == 1:
        print("""
       ___
      |   |
     _O/  |
      |   |
       \  |
    ______|
        """)
    elif vidas == 2:
        print("""
       ___
      |   |
     _O/  |
      |   |
          |
    ______|
        """)
    elif vidas == 3:
        print("""
       ___
      |   |
     _O/  |
          |
          |
    ______|
        """)
    elif vidas == 4:
        print("""
       ___
      |   |
      O/  |
          |
          |
    ______|
        """)
    elif vidas == 5:
        print("""
       ___
      |   |
      O   |
          |
          |
    ______|
        """)

else:
    print("GRACIAS POR PARTICIPAR:)")