A=int(input("ingrese el monto: "))
if A<100:
    print("no hay comision")
elif 100<A<300:
    print("la comision es: ",A*0.10)
elif A>300:
    print("la comision es: ",A*0.20)
else:
    print("error")