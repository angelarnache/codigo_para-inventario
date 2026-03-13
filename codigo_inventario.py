condicion="falso"
nombre=[]
cantidad=[]
costo=[]

while condicion == "falso":
    print("───registro de producto──")
    palabra=input(" ingrese nombre del producto: ")
    palabra_2=(input("ingrese cantidad: "))
    #el .isdigit es para que solo se puedan registrar numeros enteros
    if palabra_2.isdigit():
        palabra_2 =int(palabra_2)
    else:
        print("digito invalido por favor ingrese numeros enteros")
        continue
    #el try es para que si se pone un signo,letra,palabra o algo diferente a un numero pues este de error y regrese
    try:
        palabra_3=float(input("ingrese costo: "))
    except ValueError:
        print("digoto invalido por favor ingrese el numero de nuevo")
        continue
    #aqui es donde las listas guardan los datos
    nombre.append(palabra)
    cantidad.append(palabra_2)
    costo.append(palabra_3)
    resultado=input("deseas ver el resultado: si/no:").lower()
    if resultado == "si" or resultado == "s":
        print(f"el producto:──{nombre}──")
        print(f"cantidad:──{cantidad}──")
        print(f"precio unitario:──{costo}──")
        #esto me permite hacer la multiplicacion necesaria
        total=[ x * y for x, y in zip(cantidad,costo)]
        print(f"total general entre el la cantidad y el costo {total}")
        print("gracias por usar")
        break
    else:
        print("gracias por usar")
    break
#el codigo se hizo para que pueda registrar el producto, cantidad y el costo para que cuando el usuario lo desee
#ver la pequeña lista con los resultados de la multiplicacion y si dice que no entonces se muestra un gracias y sale 
