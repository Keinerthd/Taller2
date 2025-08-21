
archivo_clientes = "clientes.txt"

def crear_archivo():
    with open(archivo_clientes, "w") as file:
        file.write("12345,Jose,50.43\n")
        file.write("54321,Dario,43.12\n")
        file.write("67890,Maria,75.80\n")
        file.write("98765,Laura,49.99\n")
    print("Archivo creado con éxito.\n")

def buscar_saldo(nombre):
    with open(archivo_clientes, "r") as file:
        for linea in file:
            cedula, nom, saldo = linea.strip().split(",")
            if nom.lower() == nombre.lower():
                return float(saldo)
    return None



def contar_mayores_50():
    contador = 0
    with open(archivo_clientes, "r") as file:
        for linea in file:
            _, _, saldo = linea.strip().split(",")
            if float(saldo) > 50:
                contador += 1
    return contador

def listar_ordenados():
    clientes = []
    file = open(archivo_clientes, "r")
    for linea in file:
        partes = linea.strip().split(",")
        cedula = partes[0]
        nom = partes[1]
        saldo = float(partes[2])
        clientes.append([nom, saldo])
    file.close()


    for i in range(len(clientes)):
        for j in range(i + 1, len(clientes)):
            if clientes[i][1] > clientes[j][1]:
                clientes[i], clientes[j] = clientes[j], clientes[i]

    return clientes


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Crear archivo de clientes")
        print("2. Buscar saldo por nombre")
        print("3. Contar clientes con saldo mayor a 50")
        print("4. Listar clientes ordenados por saldo")
        print("5. salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            nombre = input("ingrese el nombre del cliente: ")
            saldo = buscar_saldo(nombre)
            if saldo is not None:
                print(f"El saldo de {nombre} es: {saldo}")
            else:
                print("cliente no encontrado.")
        elif opcion == "3":
            print(f"Clientes con saldo mayor a 50: {contar_mayores_50()}")
        elif opcion == "4":
            print("Clientes ordenados por saldo:")
            for nombre, saldo in listar_ordenados():
                print(f"{nombre}: {saldo}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")


menu()