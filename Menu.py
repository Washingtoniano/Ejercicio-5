from Lista import lista
class menu():
    __va=int
    __li=lista()
    def __init__(self):
        self.__va=None
        self.__li=lista()
    def operador(self,op):
        self.__li.leer()
        if  (str.lower(op)=='a'):
            self.opcion1()
        elif (op=='b'):
            self.opcion2()
        elif (op=='c'):
            self.opcion3()
        elif (op=='d'):
            self.opcion4()
        elif (op=='e'):
            self.opcion5()
        else:
            print ("Error")
    def opcion1(self):
        val=float (input("Ingrese el valor actual del vehiculo\n "))
        self.__li.opcion1(val)
    def opcion2(self):
        va=float(input ("Ingrese el valor que desea comparar"))
        self.__li.opcion2(va)
    def opcion3(self):
        self.__li.opcion3()
    def opcion4(self):
        codigo=int(input ("Ingrese el codigo del vehiculo"))
        self.__li.opcion4(codigo)
    def opcion5(self):
        self.__li.opcion5()

