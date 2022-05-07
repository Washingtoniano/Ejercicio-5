from PlanAhorro import planAhorro
import csv
class lista():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def leer(self):
        archivo=open("planes.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            Plan=planAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__indice.append(Plan)
        archivo.close()
    def opcion1(self):
        i=0
        for plan in self.__indice:
            print(plan)
        new=int(input("Ingrese el valor del vehiculo\t"))
        while i<(len(self.__indice)) and (plan()!=new):
            i=i+1
        if (i>=len(self.__indice)):
            print ("Error")
        else:
            nuevo=(float(input("Ingrese el nuevo valor del vehiculo")))
            plan.va=nuevo

    def opcion2(self,va):
        for plan in self.__indice:
            ca=plan.Calcular()
            if (ca<va):
                print (plan)

    def opcion3(self):
        for plan in (self.__indice):
            print (plan)
            print ("Licitar:{}".format(plan.licitar()))

    def opcion4(self,codigo):
        i=0
        while  i<len(self.__indice) and (self.__indice[i].cod)!= codigo:
            i=i+1
        if i>= len(self.__indice):
            print ("Codigo no encontrado\n")
        else:
            cuotas=int (input ("Ingrese la cantidad de cuotas"))
            self.__indice[i].ccuot(cuotas)
    def opcion5(self):
        for Plan in self.__indice:
            print (Plan)

