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
    def opcion1(self,va):
        i =0
        while self.__indice[i].val !=va and i<=len(self.__indice):
            i=i+1
        if i>(len(self.__indice)):
            print ("No se encontro el  valor")
        else:
            print ("Codigo:{}-Modelo:{}-Version:{}\n".format (self.__indice[i].cod,self.__indice[i].modelo, self.__indice[i].ver))
            nuevo= float(input("Ingrese el nuevo valor para el vehiculo\n"))
            self.__indice[i].modVa(nuevo)
    def opcion2(self,va):
        i=0
        for plan in self.__indice:
            ca=self.__indice[i].Calcular()
            i=i+1
            if (ca<va):
                print (plan)

    def opcion3(self):
        i=0
        for plan in (self.__indice):
            print (plan)
            print ("Licitar:{}".format(self.__indice[i].licitar))
            i=i+1


    def opcion4(self,codigo):
        i=0
        while self.__indice[i].cod != codigo and i<=len(self.__indice):
            i=i+1
        if i>  len(self.__indice):
            print ("Codigo no encontrado\n")
        else:
            cuotas=int (input ("Ingrese la cantidad de cuotas"))
            self.__indice[i].ccuot(cuotas)
    def opcion5(self):
        for Plan in self.__indice:
            print (Plan)

