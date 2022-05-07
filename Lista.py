from PlanAhorro import planAhorro
import csv
class lista():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def leer(self):
        archivo=open("planes.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            bandera=False
            if(bandera==False):
                Plan=planAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.__indice.append(Plan)
        archivo.close()
        return self.__indice
    def opcion1(self):
        i=0
        for j in range(len(self.__indice)):
            print("Codigo:{}--Modelo:{}--Versio:{}".format(self.__indice[j].cod(),self.__indice[j].modelo(),self.__indice[j].ver()))
        new=float(input("Ingrese el valor del vehiculo $"))
        while i<(len(self.__indice)) and (self.__indice[i].val()!=new):
            i=i+1
        if (i>=len(self.__indice)):
            print ("Error")
        else:
            nuevo=(float(input("Ingrese el nuevo valor del vehiculo")))
            self.__indice[i].modVa(nuevo)

    def opcion2(self,va):
        for plan in self.__indice:
            ca=plan.Calcular()
            if (ca<va):
                print (plan)

    def opcion3(self):
        for plan in (self.__indice):
            print (plan)
            print ("Licitar:${}\n".format(plan.licitar()))

    def opcion4(self):
        codigo=int(input("Ingrese el codigo del plan"))

        i=0
        while  i<len(self.__indice) and ((self.__indice[i].cod()))!= codigo:
            i=i+1
        if i== len(self.__indice):
            print ("Codigo no encontrado\n")
        else:
            cuotas=int (input ("Ingrese la cantidad de cuotas:\t"))
            self.__indice[i].ccuot(cuotas)
    def opcion5(self):
        for Plan in self.__indice:
            print (Plan)

