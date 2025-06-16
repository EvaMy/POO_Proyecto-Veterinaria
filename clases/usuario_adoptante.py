from clases.persona import Persona  

usuarios_adoptantes=[]

class UsuarioAdoptante(Persona):
    def __init__(self,nombre,apellido, dni, email, preferencias):
        super().__init__(nombre, apellido, dni,email)
        self.preferencias=preferencias ##FIJARSE (raza,edad,tamaño,peso,temperamento,estado_salud, ¿Hacerlo múltiple?)

    def registrar_Persona(self):
        usuarios_adoptantes.append(self)

    def modificar_datos(self, nombre, apellido, email, preferencias):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.preferencias=preferencias

    @staticmethod
    def buscar_persona( usuarios_adoptantes, dni_buscado):
        i=0
        v=len(usuarios_adoptantes)
        while i<v:
            if usuarios_adoptantes[i].dni==dni_buscado:
                return usuarios_adoptantes[i]
            i=i+1
        return False