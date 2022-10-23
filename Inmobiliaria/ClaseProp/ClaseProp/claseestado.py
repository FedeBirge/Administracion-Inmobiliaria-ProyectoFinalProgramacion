class estado:
    Nombre = ""

    def __init__(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return "Nombre: "+self.Nombre


if __name__ == '__main__':
    print("Soy la Clase Estado")
