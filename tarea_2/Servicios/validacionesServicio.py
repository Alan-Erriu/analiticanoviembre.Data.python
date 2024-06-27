import re



# ['test@example.com', 'hello@world.com.ar']
# Validar un formato de dirección de correo electrónico

def validarMail(mail:str)->bool: 
  patron=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}\b'
  listMailsEncontrados = re.findall(patron,mail) 
  if len(listMailsEncontrados) == 0: return False
  return True