def anioBisiesto(anio):
  return anio%4 == 0 and (anio %100 !=0 or anio%400 == 0)

def fechaValida(fecha):
  esValida = True

  partesFecha = fecha.split('/')
  if len(partesFecha) != 3:
    esValida = False

  else:

    dia = int(partesFecha[0])
    mes = int(partesFecha[1])
    anio = int(partesFecha[2])

  if not (1 <= mes <= 12 and 1<= dia <= 31):
    esValida = False

  elif mes in [4,6,9,11] and dia > 30:
    esValida = False

  elif mes == 2:

    if anioBisiesto(anio) and dia > 29:
      esValida = False

    elif not anioBisiesto(anio) and dia > 28:
      esValida = False

  return esValida


def obtenerDiaSiguiente(fecha:str):
  if not fechaValida(fecha): return "fecha invalida"
  listaPartesFecha = fecha.split("/")
  dia = int(listaPartesFecha[0])
  mes = int(listaPartesFecha[1])
  anio = int(listaPartesFecha[2])
  if dia == 30 and mes in [4,6,9,11]:  #caso meses de 30 dias -> pasamos al siguinte mes
    dia = 1
    mes  += 1
  elif dia == 31 and mes not in [4,6,9,11,12]:
    dia = 1
    mes  += 1
  elif anioBisiesto(anio) and dia == 29 and mes ==2: # febrero/29 con año bisiesto ->pasamos al siguiente mes  
    mes += 1
    dia = 1
  elif mes == 2 and dia == 28 and not anioBisiesto(anio):
    mes += 1
    dia = 1
  elif mes == 2 and dia < 28:
    dia +=1
  elif mes == 2:
    dia =+1
  elif  dia < 31 and mes not in [4,6,9,11]: #dia es menor a 31 y estamos en un mes de 31 dias -> agregamos un dia 
    dia +=1
  elif dia < 30 and mes in [4,6,9,11]:  # estamos en un mes de 30 dias y dia es menor a 30 -> sumamos un día
    dia +=1
  elif mes == 12 and dia == 31:   # año nuevo 
    anio +=1
    dia = 1
    mes = 1 
    print("año nuevo")
  if not fechaValida(str(dia) + "/" + str(mes) +"/"+ str(anio)): return "sucedio un error"
  return str(dia) + "/" + str(mes) +"/"+ str(anio)

  

    

  
