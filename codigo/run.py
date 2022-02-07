"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática: Generar un solución en lenguaje de programación Python que permita ingresar nuevas cuentas de
    diversas plataformas.
"""


def crearFacebook():
    ##Metodo llamado desde el metodo principal cuando (opcion=1) que solicita datos por teclado necesarios para la
    # creación de Facebook.
    print("Creando Facebook")
    username = (input("Ingrese su nombre de usuario "))
    edad = int(input("Ingrese su edad "))
    ciudad = (input("Ingrese ciudad de origen "))
    pais = (input("Ingrese país de origen "))
    correo = (input("Ingrese su correo electrónico "))
    cadena = ("\nFacebook creado\n" + username + "\n" + str(edad) + "\n" + ciudad + "\n" + correo + "\n")
    return cadena


def crearTwitter():
    ##Metodo llamado desde el metodo principal cuando (opcion=2) que solicita datos por teclado necesarios para la
    # creación de Twitter.
    print("Creando Twitter")
    username = (input("Ingrese su nombre de usuario "))
    nombres = (input("Ingrese sus nombres "))
    apellidos = (input("Ingrese sus apellidos "))
    edad = int(input("Ingrese su edad "))
    ciudad = (input("Ingrese ciudad de origen "))
    pais = (input("Ingrese país de origen "))
    idioma = (input("Ingrese su idioma dominante "))
    correo = (input("Ingrese su correo electrónico "))
    print("\nTwitter creado\n" + username + "\n" + nombres + "\n" + apellidos + "\n" + str(
        edad) + "\n" + ciudad + "\n" + pais + "\n"
          + idioma + "\n" + correo + "\n")


def crearWhatsapp():
    ##Metodo llamado desde el metodo principal cuando (opcion=3) que solicita datos por teclado necesarios para la
    # creación de Whatsapp.
    print("Creando Whatsapp")
    username = (input("Ingrese su nombre de usuario "))
    numero = int(input("Ingrese su número telefónico "))
    edad = int(input("Ingrese su edad "))
    ciudad = (input("Ingrese ciudad de origen "))
    pais = (input("Ingrese país de origen "))
    cadena = ("\nWhatsapp creado\n" + username + "\n" + str(numero) + "\n" + str(
        edad) + "\n" + ciudad + "\n" + pais + "\n")
    return cadena


def crearTelegram():
    ##Metodo llamado desde el metodo principal cuando (opcion=4) que solicita datos por teclado necesarios para la
    # creación de Telegram.
    print("Creando Telegram")
    username = (input("Ingrese su nombre de usuario "))
    numero = int(input("Ingrese su número telefónico "))
    edad = int(input("Ingrese su edad "))
    ciudad = (input("Ingrese ciudad de origen "))
    pais = (input("Ingrese país de origen "))
    area = (input("Ingrese área de intéres "))
    print("\nTelegram creado\n" + username + "\n" + str(numero) + "\n" + str(
        edad) + "\n" + ciudad + "\n" + pais + "\n" + area + "\n")


def crearSignal():
    ##Metodo llamado desde el metodo principal cuando (opcion=5) que solicita datos por teclado necesarios para la
    # creación de Signal.
    print("Creando Signal")
    username = (input("Ingrese su nombre de usuario "))
    numero = int(input("Ingrese su número telefónico "))
    edad = int(input("Ingrese su edad "))
    ciudad = (input("Ingrese ciudad de origen "))
    pais = (input("Ingrese país de origen "))
    hobby = (input("Ingrese su hobby principal "))
    cadena = ("\nSignal creado\n" + username + "\n" + str(numero) + "\n" + str(
        edad) + "\n" + ciudad + "\n" + pais + "\n" + hobby + "\n")
    return cadena


def crearInstagram():
    ##Metodo llamado desde el metodo principal cuando (opcion=6) que solicita datos por teclado necesarios para la
    # creación de Instagram.
    print("Creando Instagram")
    username = (input("Ingrese su nombre de usuario "))
    ciudad = (input("Ingrese ciudad de origen "))
    edad = int(input("Ingrese su edad "))
    correo = (input("Ingrese su correo electrónico "))
    print("\nInstagram creado\n" + username + "\n" + str(edad) + "\n" + correo + "\n")


def crearFlickr():
    ##Metodo llamado desde el metodo principal cuando (opcion=7) que solicita datos por teclado necesarios para la
    # creación de Flickr.
    print("Creando Flickr")
    username = (input("Ingrese su nombre de usuario "))
    correo = (input("Ingrese su correo electrónico "))
    cadena = ("\nFlickr creado\n" + username + "\n" + correo + "\n")
    return cadena


def obtenerMensaje(contador):
    ##método llamado desde el método principal que contiene los condicionales necesarios para presentar
    # el mensajeFinal de acuerdo al número de cuentas creadas mediante un arreglo unidimensional.
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente Campaña"]
    if contador <= 0:
        print("Ninguna cuenta ha sido creada")
    if contador >= 1 and contador <= 5:
        print(mensajeFinal[0])
    if contador >= 6 and contador <= 15:
        print(mensajeFinal[1])
    if contador >= 16:
        print(mensajeFinal[2])


if __name__ == "__main__":
    salida = True
    contador = 0
    while salida:
        opcion = int(input("Ingrese\n"
                           " [1]para crear Facebook\n "
                           "[2]para crear Twitter\n "
                           "[3]para crear Whatsapp\n "
                           "[4]para crear Telegram\n "
                           "[5]para crear Signal\n "
                           "[6]para crear Instagram\n "
                           "[7]para crear Flickr\n"))
        if opcion <= 0 or opcion > 7:
            print("Valor no válido, siga intentando")
        else:
            if opcion == 1:
                mensaje = crearFacebook()
                print(mensaje)
                contador = contador + 1
            else:
                if opcion == 2:
                    crearTwitter()
                    contador = contador + 1
                else:
                    if opcion == 3:
                        mensaje = crearWhatsapp()
                        print(mensaje)
                        contador = contador + 1
                    else:
                        if opcion == 4:
                            crearTelegram()
                            contador = contador + 1
                        else:
                            if opcion == 5:
                                mensaje = crearSignal()
                                print(mensaje)
                                contador = contador + 1
                            else:
                                if opcion == 6:
                                    crearInstagram()
                                    contador = contador + 1
                                else:
                                    if opcion == 7:
                                        mensaje = crearFlickr()
                                        print(mensaje)
                                        contador = contador + 1
        salida = int(input("Para seguir creando cuentas ingrese [1]\n"
                           "Para finalizar proceso ingrese [2]\n"
                           "ADVERTENCIA: En caso de ingresar un número diferente de 1 o 2, "
                           "el proceso será anulado en su totalidad\n"))
        if salida == 1:
            salida = True
        else:
            if salida == 2:
                salida = False
                obtenerMensaje(contador)
            else:
                print("valor incorrecto, procedimiento anulado.")
                salida = False