from Lista import lista
class menu():
    __li=lista()
    def __init__(self):
        self.__li=lista()
    def iniciador(self):
        self.__li.leer()
    def operador(self,op):
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
        self.__li.opcion1()
    def opcion2(self):
        va=float(input ("Ingrese el valor que desea comparar"))
        self.__li.opcion2(va)
    def opcion3(self):
        print (self.__li.opcion3())
    def opcion4(self):
        self.__li.opcion4()
    def opcion5(self):
        self.__li.opcion5()

