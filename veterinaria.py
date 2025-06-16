#from clases.persona import persona
from clases.usuario_adoptante import UsuarioAdoptante, usuarios_adoptantes
from clases.perro import Perro, perros_a_adoptar
#lógica de ejecución

perros_adoptados=[]
class SistemaAdopcion(object):
    def __init__(self, perro, persona, preferencias):
        self.perro=perro
        self.persona=persona
        self.preferencias=preferencias

    @staticmethod
    def cambiar_estado(self,perros_a_adoptar,perro_id):
        perro=Perro.buscar_perro(perros_a_adoptar,perro_id)
        if perro!=False:
            pregunta2=input("Desea cambiar a (disponible, reservado o adoptado)")
            if pregunta2.upper()=="DISPONIBLE":
                perro.estado=pregunta2
            elif pregunta2.upper()=="RESERVADO":
                perro.estado=pregunta2
            elif pregunta2.upper()=="ADOPTADO":
                perro.estado=pregunta2
            else:
                print("No se encontró un perro con ese id.")

        print("El estado fue modificado.")


    def mostrar_informacion(self,perros_a_adoptar, perro_id):
        perro=Perro.buscar_perro(perros_a_adoptar, perro_id)
        if perro!=False:
            print ("Los datos son: Nombre: "+perro.nombre+
                    "\nRaza: "+perro.raza+
                    "\nEdad: "+str(perro.edad)
                    +"\nTamaño: "+perro.tamaño+
                    "\nPeso: "+str(perro.peso)+
                    "\nEstado de salud: "+perro.estado_salud
                    +"\nVacunado: "+str(perro.vacunado)+
                    "\nEstado: "+perro.estado+
                    "\nTemperamento: "+perro.temperamento+
                    "\nid: "+str(perro.id)+".")
    @staticmethod
    def sugerir_perro_segun_preferencias(perros_a_adoptar, preferencia):
        i=0
        while i<len(perros_a_adoptar):
            if perros_a_adoptar[i].raza==preferencia:
                return perros_a_adoptar[i]
            if perros_a_adoptar[i].edad==preferencia:
                return perros_a_adoptar[i]
            if perros_a_adoptar[i].tamaño==preferencia:
                return perros_a_adoptar[i]
            if perros_a_adoptar[i].peso==preferencia:
                return perros_a_adoptar[i]
            if perros_a_adoptar[i].temperamento==preferencia:
                return perros_a_adoptar[i]
            if perros_a_adoptar[i].estado_salud==preferencia:
                return perros_a_adoptar[i]
            i=i+1

        print("No hay perros que coincidan con las preferencias.")
        return None

    @staticmethod
    def eliminar_perro_por_id(perros_a_adoptar, id_eliminado):
        perro=Perro.buscar_perro(perros_a_adoptar,id_eliminado)
        if perro!=False:
            perros_a_adoptar.remove(perro)
            print("Se eliminó el perro registrado")
        else:
            print("No sé encontró al perro")
            
    @staticmethod
    def  confirmar_adopcion(id_perro):
        perro=Perro.buscar_perro(perros_adoptados,id_perro)
        if perro!=False:
            SistemaAdopcion.eliminar_perro_por_id(perros_a_adoptar, id_perro)

    def buscar_perro_adopcion(perros_a_adoptar, id_perro):
        perro=Perro.buscar_perro(perros_a_adoptar, id_perro)
        if perro!=False:
            print("El perro esta disponible para adopción.")
            perros_adoptados.append(perro)
            SistemaAdopcion.cambiar_estado(perros_a_adoptar, id_perro)#cambiar estado
            SistemaAdopcion.confirmar_adopcion(id_perro)
        else:
            print("No se encontró el id.")
        

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
        

    def modificar_datos_por_dni(self,usuarios_adoptantes, dni_buscado,nuevo_nombre,nuevo_apellido,nuevo_email,nueva_preferencias):
        persona=UsuarioAdoptante.buscar_persona(usuarios_adoptantes, dni_buscado)
        if persona != False:
            persona.modificar_datos(nuevo_nombre, nuevo_apellido, nuevo_email, nueva_preferencias)
            print("Los datos fueron modificados correctamente")
        else:
            print("Dni no cioncide con un usuario registrado.")

#Iba a hacer otra lista con los nuevos elementos, pero chat-gpt me recomendó el remove para que tenga menos errores
    def eliminar_usuario_por_dni(usuarios_adoptantes,dni_eliminado):
            persona=UsuarioAdoptante.buscar_persona(usuarios_adoptantes, dni_eliminado)
            if persona!=False:
                usuarios_adoptantes.remove(persona)
                print ("Usuario eliminado")
            else: 
                print("No se encontró a ese usuario")

  
#usuarios_adoptantes=SistemaAdopcion.eliminar_datos_por_dni(usuarios_adoptantes,"12345678")         





    
