from fechaHorasiete import FechaHora
from ClaseHora import Hora
def bisiesto (año):
    if (año%4==0 and año%100!=0 or año%100==0):
        return True
    else:
        return False
def validarHora (hora,min,seg):

    if (hora in range(24)):
        if min in range(60):
            if seg in range(60):
                return True
            else:
                print("los datos ingresados son incorrectos,seg")
                return False
        else:
            print("los datos ingresados son incorrectos,min")
            return False
    else:
        print("los datos ingresados son incorrectos,hora")
        return False

def validar (dia,mes, año,hora,min,seg):
    if (año in range(2022)):
        if (mes in range(13)):
            if (mes==4 or mes==6 or mes==9 or mes==11):
                if dia in range(31):
                    if (validarHora(hora,min,seg)):
                        return True
                    else:
                        print("los datos ingresados son incorrectos, hora")
                        return False
                else:
                    print("los datos ingresados son incorrectos, se ingreso un dia incorrecto")
                    return False
            else:
                if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                    if dia in range(32):
                        if (validarHora(hora,min,seg)==True):
                            return True
                        else:
                            print("los datos ingresados son incorrectos")
                            return False
                    else:
                        print("los datos ingresados son incorrectos")
                        return False
                else:
                    if mes==2:
                        if bisiesto(año):
                            if dia in range(30):
                                if (validarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False
                        else:
                            if dia in range(29):
                                if (validarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False 
    else:
        return False
if __name__ == '__main__':

   d = int(input("Ingrese Dia: "))

   mes = int(input("Ingrese Mes: "))

   a = int(input("Ingrese Año: "))

   h = int(input("Ingrese Hora: "))

   m = int(input("Ingrese Minutos: "))

   s = int(input("Ingrese Segundos: "))

   if (validar(d, mes, a, h, m, s)):
       f = FechaHora(d,mes,a,h, m, s)

       f.Mostrar()

       input()

       h1 = int(input("Ingrese Hora: "))

       m1 = int(input("Ingrese Minutos: "))

       s1 = int(input("Ingrese Segundos: "))
       
       if (validarHora(h1, m1, s1)):
           r = Hora(h, m, s)

           r.Mostrar()

           #input()

           f2 = f +r
           f2.verificarsuma()
           f2.Mostrar()

           input()

           f3 = r + f
           f3.verificarsuma()
           f3.Mostrar()

           input()

           f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de
   
                   # días indicada por el número entero
           f4.verificarResta()
           f4.Mostrar()
   

           f4 = 1 + f2# suma un día a un objeto FechaHora

           f4.Mostrar() 
           input()       

 

