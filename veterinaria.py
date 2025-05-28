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
        pregunta=int(input("Ingrese el dni del usuario que desee ver: "))
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
            pregunta2=int(input("Ingrese el dni del usuario que desea eliminar: "))
            v=len(usuarios_adoptantes)
            i=0
            usuarios_adoptantes_nuevo=[] #Preguntar si lo dejo acá o lo saco fuera de la clase. Tipo cómo hago para que actualice la de afuera. Me mezclé.
            while v>i:
                if usuarios_adoptantes[i].dni!=pregunta2:
                    usuarios_adoptantes_nuevo=usuarios_adoptantes_nuevo+[usuarios_adoptantes[i]]
                i=i+1  
            print("El usuario fue eliminado.") 
            return usuarios_adoptantes_nuevo
            
            #ChatGPT me recomendó hacer:
            #global usuarios_adoptantes
            #usuarios_adoptantes=usuarios_adoptantes_nuevo
        else:
            print("No se eliminó a nungún usuario.")

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

    def cambiar_estado(self):
        pregunta=int(input("Ingrese id para cambiar el estado: "))
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if pregunta==perros_a_adoptar[i].id:
                pregunta2=input("Desea cambiar a (disponible, reservado o adoptado)")
                if pregunta2.lower()=="disponible":
                    perros_a_adoptar[i].estado=pregunta2
                elif pregunta2.lower()=="reservado":
                    perros_a_adoptar[i].estado=pregunta2
                elif pregunta2.lower()=="adoptado":
                    perros_a_adoptar[i].estado=pregunta2
                else:
                    print("No se encontró un perro con ese id.")
            i=i+1
        print("El estado fue modificado.")
        return 

    def mostrar_informacion(self):
        pregunta=int(input("Ingrese el id del perro del que desea ver información: "))
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if pregunta==perros_a_adoptar[i].id:
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
        return None
    #ChatGPT me recomendó hacer un @staticmethod dentro de cada clase correspondiente, pero no sabía si estaba bien así que lo dejo acá afuera x ahora
def buscar_perro(ingresarId):
    i=0
    v=len(perros_a_adoptar)
    while v>i:
        if ingresarId ==perros_a_adoptar[i].id:
            return perros_a_adoptar[i].id
        else:
            print("No se encontró el perro.")
        i=i+1 



perros_adoptados=[]
class SistemaAdopcion(object):
    def __init__(self, perro, persona, preferencias):
        self.persona=persona
        self.perro=perro
        self.persona=persona
        self.preferencias=preferencias

    

    def buscar_perro_adopcion(self):
        pregunta=int(input("Ingrese el id del perro a adoptar: "))
        i=0
        v=len(perros_a_adoptar)
        while i<v:
            if pregunta==perros_a_adoptar[i].id:
                print("El perro esta disponible para adopción.")
                perros_adoptados=perros_adoptados+[perros_a_adoptar[i]]
            else:
                print("No se encontró el id.")
            i=i+1

    ##
                





    
