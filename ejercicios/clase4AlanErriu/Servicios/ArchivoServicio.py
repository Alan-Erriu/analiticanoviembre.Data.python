import os

#Tarea 3 Definir una funcion que reciba 3 parametros (archivoOrigen, archivoDestino y palabra) y filtre y elimine del archivo la palabra que entra por parametro

class ArchivoServicioClase:
  def __init__(self, rutaArchivoOrigen:str, rutaArchivoSalida:str = "ejercicios/clase4AlanErriu/Archivos"):
    self._rutaArchivoOrigen = rutaArchivoOrigen
    self._rutaArchivoSalida = rutaArchivoSalida
    
  def devolverTextoArchivo(self):
    file = open(self._rutaArchivoOrigen, mode='r')
    content = file.read()
    file.close()
    return content
    
  def crearArchivo(self,nombre:str,contenido:str):
    pathNuevoArchivo = os.path.join(self._rutaArchivoSalida, nombre)
    file = open(pathNuevoArchivo, 'w')   
    file.write(contenido)
    file.close()
    print(f"Se ha creado el archivo '{nombre}'.")


  def filtrarPalabra(self,texto:str,palabraParaFiltra:str):
    listaPalabras = texto.split()
    nuevoContenido = [x for x  in listaPalabras if x != palabraParaFiltra]
    nuevoTexto = ' '.join(nuevoContenido)
    return nuevoTexto
    # file = open(nombre, 'a')
    # file.write(contenido)
    # file.close()

# def eliminar_archivo(nombre):
#     if os.path.exists(nombre):
#         os.remove(nombre)
#         print(f"El archivo {nombre} ha sido eliminado.")
#     else:
#         print(f"El archivo {nombre} no existe.")




