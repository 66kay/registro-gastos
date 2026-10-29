# Registro de gastos con archivo CSV
import csv

ARCHIVO = "gastos.csv"


def agregar_gasto():
    descripcion = input("Descripción: ")
    try:
        monto = int(input("Monto: "))
    except ValueError:
        print("El monto debe ser un número")
        return
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([descripcion, monto])
    print("Gasto guardado")


def ver_gastos():
    total = 0
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            for fila in csv.reader(f):
                print(fila[0], "-", "$" + fila[1])
                total += int(fila[1])
    except FileNotFoundError:
        print("Aún no hay gastos")
        return
    print("Total: $" + str(total))


while True:
    print("\n1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        ver_gastos()
    elif opcion == "3":
        break
    else:
        print("Opción no válida")
