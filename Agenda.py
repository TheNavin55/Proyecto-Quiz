class Agenda:
    def __init__(self):
        self.contactos = dict()
        self.id = 0
    
    def añadirContacto(self):
        contacto = dict()

        nombre = input("Nombre: ")
        contacto["nombre"]= nombre

        apellido = input("Apellido: ")
        contacto["apellido"]= apellido

        telefono = input("Telefono: ")
        contacto["telefono"]= telefono

        email = input("E-Mail: ")
        contacto["e-Mail"]= email

        self.id+=1
        self.contactos[self.id]= contacto

        return print("El contacto se añadio correctamente")


    def listadeContactos(self):
        return print(self.contactos)
        
    
    def buscarContacto(self):
        clave_busqueda = input("Ingrese el criterio de busqueda: ")
        valor_busqueda = input("ingrese el nombre a buscar: ")
        print(f'{"id":3s}{"nombre":15s}{"apellido":15s}{"telefono":11s}{"email":20s}')
        for clave, contacto in self.contactos.items():
            if valor_busqueda == contacto[clave_busqueda]:
                print(f'{clave:3s}{contacto["nombre"]:15s}{contacto["apellido"]:15s}{contacto["telefono"]:11s}{contacto["email"]:20s}')
        
    
    def editarContacto(self):
        clave_busqueda = input("Ingrese el criterio de busqueda: ")
        valor_busqueda = input("ingrese el nombre a buscar: ")
        cont_resultados = 0
        for clave, contacto in self.contactos.items():
            if valor_busqueda == contacto[clave_busqueda]:
                cont_resultados+=1
                print(contacto)
            if cont_resultados>1:
                modificar = int(input("Ingrese le id del contacto a modificar: "))
                clave_modificar = input("Ingrese el campo del contacto a modificar: ")
                nuevo_valor = input("ingrese el nuevo valor: ")
                self.contactos[modificar][clave_modificar] = nuevo_valor


    def menu(self):
        opcion = 0
        while opcion != 5:
            opcion = int(input("""Ingrese el numero de opcion que desea realizar: 
            1:Añadir Contactos 
            2:Lista de contactos 
            3:Buscar contacto 
            4:Editar contacto 
            5:Cerrar Agenda\n"""))

            if opcion==1:
                Agenda.añadirContacto(self)
            
            elif opcion==2:
                Agenda.listadeContactos(self)

            elif opcion==3:
                Agenda.buscarContacto(self)
            
            elif opcion==4:
                Agenda.editarContacto(self)
            
        return print("Agenda cerrada")
            

nueva_agenda = Agenda()
nueva_agenda.menu()