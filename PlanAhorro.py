class planAhorro():
    __codigo=int
    __modelo=str
    __version=str
    __valor=float
    __canC=int
    __canCL=int
    def __init__(self,cod=int,mo=str,ver=str,va=float,canC=int,canCL=int):
        self.__codigo=cod
        self.__modelo=mo
        self.__version=ver
        self.__valor=va
        self.__canC=canC
        self.__canCL=canCL
    def modelo(self):
        return self.__modelo
    def cod(self):
        p=int(self.__codigo)
        return p
    def ver(self):
        return self.__version
    def modVa(self,nuevo):
        self.__valor=nuevo
    def Calcular (self):
        va=float(self.__valor)
        ca=int (self.__canC)
        return ((va/ca)+va *0.10)

    def licitar (self):
        ca=int (self.__canCL)
        return (self.Calcular()*ca)
    def ccuot(self,new):
        self.__canC=new
    def val(self):
        v=float(self.__valor)
        return v
    def cuot(self):
        return self.__canC
    def cant(self):
        return self.__canCL
    def __str__ (self):
        return("Codigo:{}-Modelo:{}-Version:{}-Valor:${}-Cant.De Cuotas:{}-Cuotas p.Licitar:{}-Valord/Cuota:{}\n".format (self.__codigo,self.__modelo, self.__version,self.__valor,self.__canC,self.__canCL,self.Calcular()))
