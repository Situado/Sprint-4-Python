# Este archivo se encarga de hacer la busqueda y filtrado de cheques en el archivo "cheques.csv" según los criterios ingresados por el usuario.

import csv
from datetime import datetime

def buscar_cheques(dni, tipo_cheque, estado, fecha_inicio, fecha_fin, archivo_csv):
    cheques_encontrados = [] # Lista que almacenará los cheques encontrados

    with open(archivo_csv, mode='r', newline='') as file: # Leer el archivo CSV
        reader = csv.DictReader(file) # Crear un objeto DictReader para leer el archivo
        for row in reader: # Iterar sobre las filas del archivo

            # Convertir timestamps a objetos datetime para comparar fechas
            fecha_pago = datetime.fromtimestamp(int(row['FechaPago']))
            fecha_origen = datetime.fromtimestamp(int(row['FechaOrigen']))

            # Comparar si los datos de cada cheque coinciden con los criterios de búsqueda
            if (row['DNI'].strip() == dni
                and row['TipoCheque'] == tipo_cheque  
                and ((fecha_inicio <= fecha_pago <= fecha_fin) or (fecha_inicio <= fecha_origen <= fecha_fin))
                ):
                    if (row['Estado'] == estado):
                        cheques_encontrados.append(row)
                    elif estado == '':
                        cheques_encontrados.append(row)

        
    numeros_cheque = [cheque['NroCheque'] for cheque in cheques_encontrados] # Lista con los nros de cheque encontrados

    if len(numeros_cheque) != len(set(numeros_cheque)): # Verificar si hay números de cheque repetidos

        # len(numeros_cheque) devuelve la cantidad de elementos en la lista
        # set(numeros_cheque) convierte la lista en un conjunto, eliminando los elementos duplicados
        # len(set(numeros_cheque)) devuelve la cantidad de elementos ÚNICOS en la lista

        print("Error: Se encontraron números de cheque repetidos para el DNI dado.")                    
    
    return cheques_encontrados

def main():

    # Ingresar y validar el nombre del archivo CSV
    while True:
        archivo_csv = input("Ingrese el nombre del archivo CSV que contiene la información de los cheques: ")
        if archivo_csv == "cheques.csv":
            break
        else:
            print("Nombre de archivo no válido.")

    # Pedir al usuario que ingrese el DNI del cliente a consultar
    while True:
        try:
            dni = input("Ingrese el DNI del cliente para buscar los cheques: ").strip()
            if int(dni) > 0:
                break
            else:
                print("El numero de DNI debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    # Preguntar al usuario cómo quiere los resultados (Pantalla o CSV)
    while True:
        try:
            opcion = int(input("Ingrese 1 para guardar los resultados en un nuevo archivo CSV o 2 para imprimir en pantalla: "))
            if opcion not in [1, 2]:
                raise ValueError("Opción no válida. Debe ser 1 o 2.")
            break
        except ValueError as e:
            print(e)


    # Pedir al usuario que ingrese el Tipo de Cheque
    while True:
        tipo_cheque = input("Ingrese el tipo de cheque (EMITIDO, DEPOSITADO): ").upper()
        if tipo_cheque in ['EMITIDO', 'DEPOSITADO']:
            break
        else:
            print("Tipo de cheque no válido. Debe ser 'EMITIDO' o 'DEPOSITADO'.")


    # Preguntar y pedir al usuario si desea ingresar el Estado del Cheque
    filtrar_estado = input("¿Desea filtrar por Estado del Cheque? (si/no): ").lower()
    if filtrar_estado == 'si': 
        while True:
            estado = input("Ingrese el estado del cheque (pendiente, aprobado, rechazado): ").lower()
            if estado in ['pendiente', 'aprobado', 'rechazado']:
                break
            else:
                print("Estado de cheque no válido. Debe ser 'pendiente', 'aprobado' o 'rechazado'.")
    else:
        estado = ''    

    # Preguntar al usuario si desea filtrar por rango de fechas
    filtrar_fechas = input("¿Desea filtrar por rango de fechas? (si/no): ").lower()
    if filtrar_fechas == 'si':       
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

    # Procesar la opción de Salida elegida
    if opcion == 1:  # Guardar los resultados en un nuevo archivo CSV

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_filename = f'{dni}_{timestamp}.csv'
        keys = [
                'NroCheque', 'CodigoBanco', 'CodigoSucursal', 'NumeroCuentaOrigen', 'NumeroCuentaDestino',
                'Valor', 'FechaOrigen', 'FechaPago', 'DNI', 'Estado', 'TipoCheque'
                ]# Define las claves de las columnas
        
        with open(output_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(cheques)

        print("Los resultados se han guardado en el archivo con el siguiente formato: '<DNI>_<TIMESTAMP_ACTUAL>.csv'.")

    elif opcion == 2: # Imprimir los resultados en pantalla
        for cheque in cheques:
            print(cheque)

if __name__ == "__main__": # Ejecutar el programa principal
    main()