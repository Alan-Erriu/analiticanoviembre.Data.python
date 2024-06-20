#Siguiente Dia: Definir una función que reciba un parametro de fecha y devuelva la siguiente fecha calendario a la recibida
#Validar un formato de dirección de correo electrónico

#Definir una funcion que reciba 3 parametros (archivoOrigen, archivoDestino y palabra) y filtre y elimine del archivo la palabra que entra por parametro
from Servicios.fechaServicio import obtenerDiaSiguiente, fechaValida

fechaSiguiente = obtenerDiaSiguiente("1/2/2025")
print(fechaSiguiente)



## para testear a groso modo que funciona 
fechaInicial = "31/12/2024"
for x in range(1,400):
    mañana = obtenerDiaSiguiente(fechaInicial)
    print(mañana)
    pasadoMañana = obtenerDiaSiguiente(mañana)
    print(pasadoMañana)
    fechaInicial = pasadoMañana



        
