##Tal vez quiera crear empleados en el futuro
class Persona(object):
    def __init__(self,nombre, apellido, dni, email):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.email=email

usuarios_adoptantes=[]
class UsuarioAdoptante(Persona):
    def __init__(self,nombre, dni, email, preferencias):
        super().__init__(nombre,dni,email)
        self.preferencias=preferencias ##FIJARSE (raza,edad,tamaño)

    def registrar_Persona(self):
        usuarios_adoptantes.append(self)

    def modificar_datos(self, nombre, apellido, dni, email, preferencias):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
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


    

perros_a_adoptar=[]
class Perro(object):
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento,id):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.tamaño=tamaño
        self.peso=peso
        self.estado_salud=estado_salud
        self.vacunado=vacunado 
        self.estado=estado 
        self.temperamento=temperamento 
        self.id=id 

    def registrar_Mascota(self):
        perros_a_adoptar.append(self)

        ###############################################################
    @staticmethod
    def buscar_perro(perros_a_adoptar, ingresarId):
        i=0
        v=len(perros_a_adoptar)
        while v>i:
            if ingresarId ==perros_a_adoptar[i].id:
                return perros_a_adoptar[i].id
            i=i+1 
        return False



perros_adoptados=[]
class SistemaAdopcion(object):
    def __init__(self, perro, persona, preferencias):
        self.persona=persona
        self.perro=perro
        self.persona=persona
        self.preferencias=preferencias

    def cambiar_estado(self,perros_a_adoptar,perro_id):
        perro=Perro.buscar_perro(perro_id)
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if perro_id==perros_a_adoptar[i].id:
                pregunta2=input("Desea cambiar a (disponible, reservado o adoptado)")
                if pregunta2.upper()=="DISPONIBLE":
                    perros_a_adoptar[i].estado=pregunta2
                elif pregunta2.upper()=="RESERVADO":
                    perros_a_adoptar[i].estado=pregunta2
                elif pregunta2.upper()=="ADOPTADO":
                    perros_a_adoptar[i].estado=pregunta2
                else:
                    print("No se encontró un perro con ese id.")
            i=i+1
        print("El estado fue modificado.")

######
    def mostrar_informacion(self,perros_a_adoptar, perro_id):
        perro=Perro.buscar_perro(perros_a_adoptar, perro_id)
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if perro==perros_a_adoptar[i].id:
                print ("Los datos son: Nombre: "+perros_a_adoptar[i].nombre+
                       "\nRaza: "+perros_a_adoptar[i].raza+
                       "\nEdad: "+str(perros_a_adoptar[i].edad)
                       +"\nTamaño: "+perros_a_adoptar[i].tamaño+
                       "\nPeso: "+str(perros_a_adoptar[i].peso)+
                       "\nEstado de salud: "+perros_a_adoptar[i].estado_salud
                       +"\nVacunado: "+perros_a_adoptar[i].vacunado+
                       "\nEstado: "+perros_a_adoptar[i].estado+
                        "\nTemperamento: "+perros_a_adoptar[i].temperamento+
                       "\nid: "+str(perros_a_adoptar[i].id)+".")
            i=i+1

        ##fijarse bien, me hace ruido este. Agregar buscar perro
    def buscar_perro_adopcion(self,perros_a_adopar, id_perro):
        perro=Perro.buscar_perro(perros_a_adoptar, id_perro)
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if perro==perros_a_adoptar[i].id:
                print("El perro esta disponible para adopción.")
                perros_adoptados=perros_adoptados+[perros_a_adoptar[i]]
            else:
                print("No se encontró el id.")
            i=i+1
##########

    def ver_historial_por_dni(self,usuarios_adoptantes, dni_buscado):
        persona=UsuarioAdoptante.buscar_persona(usuarios_adoptantes, dni_buscado)
        if persona!=False:
            print("Los datos son: Nombre: "+persona.nombre+
                "\nApellido: "+persona.apellido+
                "\nDNI: "+persona.dni+
                "\nEmail: "+persona.email+
                "\nPreferencias: "+persona.preferencias)
        else: 
            print("Dni no coincide con un usuario registrado.")
        

    def modificar_datos_por_dni(self,usuarios_adoptantes, dni_buscado):
        persona=UsuarioAdoptante.buscar_persona(usuarios_adoptantes, dni_buscado)
        if persona != False:
            nombre=input("Ingrese nombre: ")
            apellido=input("Ingrese apellido: ")
            email=input("Ingrese email: ")
            preferencias=input("Ingrese preferencias: ")
            persona.modificar_datos(nombre, apellido, email, preferencias)
        else:
            print("Dni no cioncide con un usuario registrado.")


    def eliminar_datos_por_dni(usuarios_adoptantes,dni_eliminado):
            persona=UsuarioAdoptante.buscar_persona(usuarios_adoptantes, dni_eliminado)
            usuarios_adoptantes_nuevo=[]
            i=0
            v=len(usuarios_adoptantes)
            while i<v:
                if persona.dni != usuarios_adoptantes[i].dni:
                    usuarios_adoptantes_nuevo.append(usuarios_adoptantes[i]) 
                i=i+1
            print("El usuario fue eliminado.")
            return usuarios_adoptantes_nuevo
            
#usuarios_adoptantes=SistemaAdopcion.eliminar_datos_por_dni(usuarios_adoptantes,"12345678")         





    
