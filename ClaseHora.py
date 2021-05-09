class Hora:
    __hora=0
    __min=0
    __seg=0
    
    
    def __init__ (self,hora=0,min=0,seg=0):
        self.__hora=hora
        self.__min=min
        self.__seg=seg
        
        
    def getHora (self):
        return self.__hora
    
    def getMin (self):
        return self.__min
    
    def getSeg (self):
        return self.__seg
    
    def Mostrar (self):
        print("{}""h, ""{}""m, ""{}""s".format(self.__hora,self.__min,self.__seg))
    
    
