p =int(input("ingrese el monto: "))
if p>1000:
    descuento= p*0.20
    preciofinal=p-descuento
    print("el monto a pagar es: ",preciofinal)
else:
    print("el total a pagar es: ",p)