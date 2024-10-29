import csv
from datetime import datetime

def buscar_cheques(dni, tipo_cheque, estado, fecha_inicio, fecha_fin, archivo_csv):
    cheques_encontrados = []

    # Leer el archivo CSV
    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:

            # Convertir timestamps a objetos datetime
            fecha_pago = datetime.fromtimestamp(int(row['FechaPago']))
            fecha_origen = datetime.fromtimestamp(int(row['FechaOrigen']))

            if (row['DNI'].strip() == dni
                and row['TipoCheque'] == tipo_cheque 
                and row['Estado'] == estado 
                and ((fecha_inicio <= fecha_pago <= fecha_fin) or (fecha_inicio <= fecha_origen <= fecha_fin))
                ):
                    cheques_encontrados.append(row)
    
    return cheques_encontrados

def main():
    # Validar el nombre del archivo CSV
    while True:
        archivo_csv = input("Ingrese el nombre del archivo CSV que contiene la información de los cheques: ")
        if archivo_csv == "cheques.csv":
            break
        else:
            print("Nombre de archivo no válido.")

    # Pedir al usuario que ingrese el DNI del cliente
    while True:
        try:
            dni = input("Ingrese el DNI del cliente para buscar los cheques: ").strip()
            if int(dni) > 0:
                break
            else:
                print("El numero de DNI debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    # Pedir al usuario que ingrese el Tipo de Cheque
    while True:
        tipo_cheque = input("Ingrese el tipo de cheque (EMITIDO, DEPOSITADO): ").upper()
        if tipo_cheque in ['EMITIDO', 'DEPOSITADO']:
            break
        else:
            print("Tipo de cheque no válido. Debe ser 'EMITIDO' o 'DEPOSITADO'.")

    # Pedir al usuario que ingrese el Estado del Cheque
    while True:
        estado = input("Ingrese el estado del cheque (pendiente, aprobado, rechazado): ").lower()
        if estado in ['pendiente', 'aprobado', 'rechazado']:
            break
        else:
            print("Estado de cheque no válido. Debe ser 'pendiente', 'aprobado' o 'rechazado'.")

    # Preguntar al usuario si desea filtrar por rango de fechas
    filtrar_fechas = input("¿Desea filtrar por rango de fechas? (s/n): ").lower()
    if filtrar_fechas == 's':       
        fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (YYYY-MM-DD): "), '%Y-%m-%d')
        fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (YYYY-MM-DD): "), '%Y-%m-%d')
    else:
        fecha_inicio = datetime.min
        fecha_fin = datetime.max

    # Buscar los cheques que coincidan con los criterios ingresados
    cheques = buscar_cheques(dni, tipo_cheque, estado, fecha_inicio, fecha_fin, archivo_csv)

    if not cheques:
        print("No se encontraron cheques para los criterios ingresados.")
        return

    # Preguntar al usuario cómo quiere los resultados
    while True:
        try:
            opcion = int(input("Ingrese 1 para guardar los resultados en un nuevo archivo CSV o 2 para imprimir en pantalla: "))
            if opcion not in [1, 2]:
                raise ValueError("Opción no válida. Debe ser 1 o 2.")
            break
        except ValueError as e:
            print(e)

    # Procesar la opción elegida
    if opcion == 1:
        # Guardar los resultados en un nuevo archivo CSV
        with open('cheques_encontrados.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cheques[0].keys())
            writer.writeheader()
            writer.writerows(cheques)
        print("Los resultados se han guardado en 'cheques_encontrados.csv'.")
    elif opcion == 2:
        # Imprimir los resultados en pantalla
        for cheque in cheques:
            print(cheque)

if __name__ == "__main__":
    main()