class planAhorro():
    __codigo=None
    __modelo=''
    __version=''
    __valor=0.0
    __canC=0
    __canCL=0
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
        return self.__codigo
    def ver(self):
        return self.__version
    def modVa(self,nuevo):
        self.__valor=nuevo
    def Calcular (self):

        resultado =((self.__valor/self.__canC)+self.__valor *0.10)
        return resultado
    def licitar (self):
        return (self.__canCL*self.Calcular())
    def ccuot(self,new):
        self.__canC=new
    def val(self):
        return self.__valor
    def cuot(self):
        return self.__canC
    def cant(self):
        return self.__canCL
    def __str__ (self):
        return("Codigo:{}-Modelo:{}-Version:{}-Valor:${}-Cant.De Cuotas:{}-Cuotas p. Licitar:{}-Monto para licitar:${}\n".format (self.__codigo,self.__modelo, self.__version,self.__valor,self.__canC,self.__canCL,self.__licitar))
