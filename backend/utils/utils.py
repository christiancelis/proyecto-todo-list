def leerDato(msg):
    while True:
        try:
            Nombre = input(msg)
            Nombre.strip()
            if(Nombre==""):
                print("Nombre no valido")
                continue
            return Nombre
        except Exception as e:
            print("Error al ingresar el nombre", e)


def leerintMenu(msg,inicial,final):
    while True:
        try:
            Entero = int(input(msg))
            if(Entero<inicial or Entero>final):
                print(f"Valor invalido, debe estar entre {inicial} y {final}")
                continue
            return Entero
        except Exception as e:
            print("Error al ingresar el numero", e)