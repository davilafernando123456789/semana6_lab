t=int(input("ingrese la temperatura: "))
if t<10:
    print("el clima es frio")
elif 11<t<16:
    print("el clima es templado")
elif 17<t<24:
    print("el clima es calido")
elif t>24:
    print("tropical")
else:
    print("error")