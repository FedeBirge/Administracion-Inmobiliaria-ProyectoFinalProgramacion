class propiedad:
    Nombre = ""
    Direccion = ""
    Contacto = 0

    def __init__(self, nombre, direccion, contacto):
        self.Nombre = nombre
        self.Direccion = direccion
        self.Contacto = contacto

    def getNombre(self):
        return self.Nombre

    def getDireccion(self):
        return self.Direccion

    def getContacto(self):
        return self.Contacto

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def setContacto(self, contacto):
        self.Contacto = contacto

    def __str__(self):
        return "Nombre: "+self.Nombre+" Direccion: "+self.Direccion+" Contacto: "+str(self.Contacto)


if __name__ == '__main__':
    print("Soy la Clase Propiedad")
