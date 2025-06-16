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


    def modificar_datos(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento,id):
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


    @staticmethod
    def buscar_perro(perros_a_adoptar, ingresarId):
        i=0
        v=len(perros_a_adoptar)
        while v>i:
            if ingresarId ==perros_a_adoptar[i].id:
                return perros_a_adoptar[i]
            i=i+1 
        return False