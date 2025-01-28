BD = [
    {"Nombre": "Silla", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": True, "Exterior": True, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": True},

    {"Nombre": "Cama", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": False, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": True},

    {"Nombre": "Hamburguesa", "Tangible": True, "Cuantitativo": True, "Tamaño": True, "Peso": True, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": True, "Temperatura": False, "Comestible": True, "Saludable": False, "Estado": False, "Institucion": True},

    {"Nombre": "Agua", "Tangible": True, "Cuantitativo": False, "Tamaño": False, "Peso": False, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": True, "Estado": True, "Institucion": False},

    {"Nombre": "Sala", "Tangible": False, "Cuantitativo": False, "Tamaño": False, "Peso": False, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": True, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Martillo", "Tangible": True, "Cuantitativo": True, "Tamaño": True, "Peso": True, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": True, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": True, "Saludable": False, "Estado": False, "Institucion": True},

    {"Nombre": "Pantalon", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": True, "Exterior": False, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": True, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": True, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": True},

    {"Nombre": "Perro", "Tangible": True, "Cuantitativo": True, "Tamaño": True, "Peso": False, "Exterior": True, "Transporte": False, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": True, "Sexo": True, "Famoso": False, 
    "Oloroso": True, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Mariposa", "Tangible": True, "Cuantitativo": True, "Tamaño": True, "Peso": True, "Exterior": True, "Transporte": False, 
    "Vuela":True, "Lugar": False, "Funcion": False, "Interior": False, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Caballo", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": False, "Exterior": True, "Transporte": True, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": False, "Uso": False, "Ruidoso": False, "Sexo": True, "Famoso": False, 
    "Oloroso": True, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Avion", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": False, "Exterior": True, "Transporte": True, 
    "Vuela":True, "Lugar": False, "Funcion": False, "Interior": False, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": True, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Camion", "Tangible": True, "Cuantitativo": True, "Tamaño": False, "Peso": False, "Exterior": True, "Transporte": True, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": True, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

    {"Nombre": "Automovil", "Tangible": True, "Cuantitativo": True, "Tamaño": True, "Peso": False, "Exterior": True, "Transporte": True, 
    "Vuela":False, "Lugar": False, "Funcion": False, "Interior": False, "Uso": False, "Ruidoso": False, "Sexo": False, "Famoso": False, 
    "Oloroso": False, "Temperatura": False, "Comestible": False, "Saludable": False, "Estado": False, "Institucion": False},

]


def Opcion (opcion, propiedad):

    if opcion == "SI" or opcion == "si":
        Opc = True
    else:
        Opc = False

    to_remove = []

    for d in BD:
        if d[propiedad] != Opc:
            to_remove.append(d)
    
    for i in to_remove:
        BD.remove(i)

    if len(BD) == 1:
        print ("Estás pensando en " + BD[0]["Nombre"] + "?")
        quit()

print ("\nResponde si o no: ")

Opc = input ("\n - ¿Estás pensando en algo tangible? ")
Opcion (Opc, "Tangible")

Opc = input ("\n - ¿Estás pensando en algo que se encuentra al aire libre? ")
Opcion (Opc, "Exterior")

Opc = input ("\n - ¿Estás pensando en un lugar? ")
Opcion (Opc, "Lugar")

Opc = input ("\n - ¿Estás pensando en algo que vuela? ")
Opcion (Opc, "Vuela")

Opc = input ("\n - ¿Estás pensando en algo que usas para transportarte? ")
Opcion (Opc, "Transporte")

Opc= input ("\n - ¿Estás pensando en algo que encuentras en alguna institución (escuela/hospital/banco/restaurante)? ")
Opcion (Opc, "Institucion")

Opc = input ("\n - ¿Estás pensando en algo que puedes encontrar dentro de una casa? ")
Opcion (Opc, "Interior")

Opc = input ("\n - ¿Estás pensando en algo líquido? ")
Opcion (Opc, "Estado")

Opc = input ("\n - ¿Estás pensando en algo cuantitativo? ")
Opcion (Opc, "Cuantitativo")

Opc = input ("\n - ¿Estás pensando en algo que produce ruido? ")
Opcion (Opc, "Ruidoso")

Opc= input ("\n - ¿Estás pensando en algo que puedes sostener en tus manos? ")
Opcion (Opc, "Peso")

Opc = input ("\n - ¿Estás pensando en algo que te ayuda a realizar alguna tarea? ")
Opcion (Opc, "Funcion")

Opc= input ("\n - ¿Estás pensando en algo de tamaño pequeño? ")
Opcion (Opc, "Tamaño")

Opc = input ("\n - ¿Estás pensando en algo que puedes usar en alguna parte cuerpo? ")
Opcion (Opc, "Uso")

Opc = input ("\n - ¿Estás pensando en algo oloroso? ")
Opcion (Opc, "Oloroso")

Opc = input ("\n - ¿Estás pensando en algo que tiene temperatura caliente? ")
Opcion (Opc, "Temperatura")

Opc = input ("\n - ¿Estás pensando en algo comestible? ")
Opcion (Opc, "Comestible")

Opc = input ("\n - ¿Estás pensando en algo saludable? ")
Opcion (Opc, "Saludable")

Opc = input ("\n - ¿Estás pensando en algo que puede tener crías o hijos? ")
Opcion (Opc, "Sexo")

Opc = input ("\n - ¿Estás pensando en un famoso? ")
Opcion (Opc, "Famoso")












