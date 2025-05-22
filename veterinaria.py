class Persona(object):
    def __init__(self,nombre, dni, email):
        self.nombre=nombre
        self.dni=dni
        self.email=email

usuarios_adoptantes=[]
class UsuarioAdoptante(Persona):
    def __init__(self,nombre, dni, email, preferencias):
        super().__init__(nombre,dni,email)
        self.preferencias=preferencias

    def registrar_Persona(self):
        usuarios_adoptantes.append(self)

    def modificar_datos(self):
        pregunta=input("¿Desea modificar dato?: (S/N)")
        if pregunta.lower()== "s":
            pregunta2=input("Elija que modificar entre nombre, dni, email o preferencias:")
            if pregunta2.lower()=="nombre":
                nuevoNombre=input("Escriba el nuevo nombre: ")
                self.nombre=nuevoNombre
            elif pregunta2.lower()=="dni":
                nuevoDNI=input("Ingrese nuevo DNI: ")
                self.dni=nuevoDNI
            elif pregunta2.lower()=="email":
                nuevoEMAIL=input("Ingrese un nuevo email: ")
                self.email=nuevoEMAIL
            elif pregunta2.lower()=="preferencias":
                nuevaPreferencia=input("Ingrese la nueva preferencia: ")
                self.preferencias=nuevaPreferencia
            else:
                print("Esa opción no es válida.")
        else:
            return 
    
    
    
    def ver_historial(self):
        pregunta=input("Ingrese el dni del usuario que desee ver: ")
        v=len(usuarios_adoptantes)
        i=0
        while v>i:
            if usuarios_adoptantes[i].dni==pregunta:
                print("Sus datos son: Nombre: "+ usuarios_adoptantes[i].nombre+", DNI: "+ usuarios_adoptantes[i].dni+", Email: "+usuarios_adoptantes[i].email+ 
                      " y preferencias: "+ usuarios_adoptantes[i].preferencias)
            i=i+1
        return 


class EliminarAdoptante:
    def eliminar_datos(self):
        pregunta=input("¿Desea eliminar a un usuario? (S/N)")
        if pregunta.lower()=="s":
            pregunta2=input("Ingrese el dni del usuario que desea eliminar: ")
            v=len(usuarios_adoptantes)
            i=0
            usuarios_adoptantes_nuevo=[] #Preguntar si lo dejo acá o lo saco fuera de la clase
            while v>i:
                if usuarios_adoptantes[i].dni!=pregunta2:
                    usuarios_adoptantes_nuevo=usuarios_adoptantes_nuevo+[usuarios_adoptantes[i]]
                i=i+1  
            print("El usuario fue eliminado.") 
            return usuarios_adoptantes_nuevo
            
            #ChatGPT me recomendó:
            #global usuarios_adoptantes
            #usuarios_adoptantes=usuarios_adoptantes_nuevo
        else:
            print("No se eliminó a nungún usuario.")

perros_adoptados=[]
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
        perros_adoptados.append(self)

    def cambiar_estado(self):
        pregunta=input("Ingrese id para cambiar el estado: ")
        i=0
        v=len(perros_adoptados)
        while i<v:
            if pregunta==perros_adoptados[i].id:
                pregunta2=input("Desea cambiar a (disponible, reservado o adoptado)")
                if pregunta2.lower()=="disponible":
                    perros_adoptados[i].estado=pregunta2
                elif pregunta2.lower()=="reservado":
                    perros_adoptados[i].estado=pregunta2
                elif pregunta2.lower()=="adoptado":
                    perros_adoptados[i].estado=pregunta2
            i=i+1
        print("El estado fue modificado.")
        return 


    
