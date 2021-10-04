operacion = input("ingrese operacion(suma-s; resta-r; multiplicacion-m; division-d)")
a = int(input("ingrese el primer numero: "))
c = int(input("ingrese el segundo numero: "))
if operacion == 's' :
    print("la suma es: ",a+c)
elif operacion== 'r' :
    print("la resta es: ",a-c)
elif operacion=='m' :
    print("la multiplicacion es: ",a*c)
elif operacion=='d' and c !=0 :
    print("la division es: ",a/c)
else:
    print("error")