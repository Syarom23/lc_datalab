'''
validación 1
valida que un correo electronico sea valido o no valido
'''

import re

email = "@ejemplo.com"

regex_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(regex_email, email):
    print("El correo es válido.")
else:
    print("El correo NO es válido.")


'''
validación 2 
solo valida nombre y apellido , solo letras y espacios
'''

import re

nombre = "Carlos Duvan"
# Solo letras y espacios
regex_nombre = r"^[a-zA-Z\s]+$"

if re.match(regex_nombre, nombre):
    print("Válido")
else:
    print("No válido")

