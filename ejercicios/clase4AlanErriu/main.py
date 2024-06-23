from Servicios import  ArchivoServicio

# Tarea1 Siguiente Dia: Definir una función que reciba un parametro de fecha y devuelva la siguiente fecha calendario a la recibida

# fechaSiguiente = fechaServicio.obtenerDiaSiguiente("1/2/2025")
# print(fechaSiguiente)

# ## para testear a groso modo que funciona 
# fechaInicial = "31/12/2024"
# for x in range(1,400):
#     mañana = fechaServicio.obtenerDiaSiguiente(fechaInicial)
#     print(mañana)
#     pasadoMañana = fechaServicio.obtenerDiaSiguiente(mañana)
#     print(pasadoMañana)
#     fechaInicial = pasadoMañana



# #***************************************************************************************************************************************************


# #Tarea 2 Validar un formato de dirección de correo electrónico

# emailEjemplo = 'test@example.com'
# emailEsVerdadero =  validacionesServicio.validarMail(emailEjemplo)
# print(emailEsVerdadero)




#*****************************************************************************************************************************************************



#Tarea 3 Definir una funcion que reciba 3 parametros (archivoOrigen, archivoDestino y palabra) y filtre y elimine del archivo la palabra que entra por parametro

rutaArchivoOrigen = "ejercicios/clase4AlanErriu/Archivos/archivoOrigen.txt"

archivoServicio1 = ArchivoServicio.ArchivoServicioClase(rutaArchivoOrigen)

textoArchivoOrigen  = archivoServicio1.devolverTextoArchivo()

textoNuevo =  archivoServicio1.filtrarPalabra(textoArchivoOrigen, "Argentina")

archivoServicio1.crearArchivo("archivoEjemplo",textoNuevo)




        
