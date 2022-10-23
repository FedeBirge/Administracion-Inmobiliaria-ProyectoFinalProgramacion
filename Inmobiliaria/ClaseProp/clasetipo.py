class tipo:
    Nombre = ""

    def __init__(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return "Nombre: " + str(self.Nombre)
