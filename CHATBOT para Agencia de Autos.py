#inicialización de estado
import re
import time

 # Lenguaje natural por expresiones regulares
Promo_RE = r"1|promociones|promos?|descuentos|promocionez|promocion|" \
           r"promocion?|promociones?|promocioness|prmociones|promocions|" \
           r"promocione|promocionnes|promocioness|promociones!|promocionnes!"\
           r"promocionnes?|descuento|descuentos?|descuento?|descuentoss|descuentoz|descuentoss|"\
           r"promociones |Promociones|Promociones |descuentos |Descuentos|Descuentos |" \
           r"promos |Promos|Promos|P|Prom|prom| p "
Cita_RE = r"3|cita|Cita|servicio|Servicio|Cíta|ci[í]ta|servi[í]ci[í]o|agendar|ci[í]ta |Ci[í]ta" \
          r"servi[í]ci[í][í][í]o |Servi[í]ci[í]o|Servi[í]ci[í]o |" \
          r"agendar |Agendar|Agendar |agendamiento|Agendamiento|agendamiento |Agendamiento "
Venta_RE = r"2|venta|comprar|venden|" \
           r"venta |Venta|Venta |" \
           r"comprar |Comprar|Comprar |" \
           r"venden |Venden|Venden |" \
           r"ventas|compras|vendiendo|" \
           r"ventas |Ventas|Ventas |" \
           r"compras |Compras|Compras |" \
           r"vendiendo |Vendiendo|Vendiendo "
placa_Re = r"\d\d\d[\s| |-]?\w\w\w"
afirmacion_RE = r"s[i|í]|claro|definitavamente|" \
                r"s[i|í] |S[i|í]|S[i|í] |" \
                r"claro |Claro|Claro |" \
                r"definitavamente |Definitavamente|Definitavamente |definitavamnte|Definitavamnte|definitavamnte "\
                r"porsupesto|porsupesto |Porsupuesto|Porsupuesto |"\
                r"clro|Clro|clro |Clro " \
                r"afirmativo |Afirmativo|Afirmativo |" \
                r"afirmativ |Afirmativ|afirmativ |" \
                r"afirmativoo|Afirmativoo|afirmativoo "

state=0
Salida=1
intentos =0
while Salida:
    if state==0:
        print("Hola soy el Chatbot de la FORD ¿En qué te puedo ayudar?")
        time.sleep(1)
        opcion=input("Soy capaz de informarte de nuestras promociones, venta de vehículos y ayudarte a agendar un cita. \n\t\t\t")
        while True:
            if re.findall(Promo_RE, opcion, flags=0)!=[]:
                state=1
                intentos=0
                break
            elif re.findall(Cita_RE, opcion, flags=0)!=[]:
                state=2
                intentos=0
                break
            elif re.findall(Venta_RE, opcion, flags=0)!=[]:
                state=3
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
           print("Nuestro catálogo de promociones vigentes son...\n")
           print("1.- Tasa de interés reducida\n"
                 "2.- Arrendamiento con cuotas mensuales\n"
                 "3.- Neumático de refacción gratis\n"
                 "4.- 3 meses gratis de seguro\n")
           respProm = input("\nElige una opción para ver detalles de cada promoción\n")
           if respProm == '1':
                 print("\nObten una tasa de interés reducida al 15% al comprar una camioneta último modelo\n")
                 state = 0
           if respProm == '2':
                 print("\nSi estarás en la ciudad unos meses y no quieres moverte en transporte público,\n puedes adquirir un automóvil con nosotros y pagar su arrendamiento los primeros 5 días de cada mes\n")
                 state = 0
           if respProm == '3':
                 print("\nAl dar el enganche para adquirir un carro del año, podrás obtener un neumático de refacción gratis\n")
                 state = 0
           if respProm == '4':
                 print("\nSi adquieres un automóvil con nosotros, podrás obtener 3 meses de seguro gratis\n")
                 state = 0
           else:
                 state=6
    if state == 2:
        name = input("Dime tu nombre para agendar la cita. \n\t\t\t")
        state = 4
    if state == 3:
        print("En un momento te contactara un agente de ventas")
        Salida=0
    if state == 4:
        placa = input("Podrias proporcionarme tu placa. \n\t\t\t")
        if re.findall(placa_Re, placa, flags=0)!=[]:
            state = 5
        else:
            print("Placa Invalida")
    if state == 5:
        print("Gracias {} en un momento te atendera un operador".format(name))
        Salida=0
    if state == 6:
        opcion=input("¿te puedo ayudar en algo más?  \n\t\t\t")
        if re.findall(afirmacion_RE, opcion, flags=0!=[]):
            state=0
        else:
            print("Gracias fue un placer atenderte")
            Salida=0