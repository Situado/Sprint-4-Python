# Este archivo se encarga de generar diccionarios de cheques con las correspondientes validaciones y guardarlos en un archivo "cheques.csv" para su posterior uso.

import datetime
import csv

def ingresar_campos():
    cheque = {}

    while True:
        try:
            cheque['NroCheque'] = int(input("Ingrese el número de cheque (único por cuenta): "))
            if cheque['NroCheque'] > 0:
                break
            else:
                print("El numero del cheque debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            cheque['CodigoBanco'] = int(input("Ingrese el código del banco (1-100): "))
            if 1 <= cheque['CodigoBanco'] <= 100:
                break
            else:
                print("El código del banco debe estar entre 1 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    while True:
        try:
            cheque['CodigoSucursal'] = int(input("Ingrese el código de la sucursal del banco (1-300): "))
            if 1 <= cheque['CodigoSucursal'] <= 300:
                break
            else:
                print("El código de la sucursal debe estar entre 1 y 300.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    while True:
        try:
            cheque['NumeroCuentaOrigen'] = int(input("Ingrese el número de cuenta de origen: "))
            if cheque['NumeroCuentaOrigen'] > 0:
                break
            else:
                print("El numero de la Cuenta Origen debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            cheque['NumeroCuentaDestino'] = int(input("Ingrese el número de cuenta de destino: "))
            if cheque['NumeroCuentaDestino'] > 0:
                break
            else:
                print("El numero de la Cuenta Destino debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            cheque['Valor'] = float(input("Ingrese el valor del cheque: "))
            if cheque['Valor'] > 0:
                break
            else:
                print("El valor del cheque debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            fecha_origen = input("Ingrese la fecha de emisión (dd/mm/yyyy): ")
            cheque['FechaOrigen'] = int(datetime.datetime.strptime(fecha_origen, "%d/%m/%Y").timestamp())
            break
        except ValueError:
            print("Formato de fecha inválido. Use dd/mm/yyyy.")

    while True:
        try:
            fecha_pago = input("Ingrese la fecha de pago (dd/mm/yyyy): ")
            cheque['FechaPago'] = int(datetime.datetime.strptime(fecha_pago, "%d/%m/%Y").timestamp())
            if cheque['FechaPago'] >= cheque['FechaOrigen']:
                break
            else:
                print("La fecha de pago no puede ser anterior a la fecha de emisión.")
        except ValueError:
            print("Formato de fecha inválido. Use dd/mm/yyyy.")

    while True:
        try:
            cheque['DNI'] = int(input("Ingrese el DNI del cliente: "))
            if cheque['DNI'] > 0:
                break
            else:
                print("El numero de DNI debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        cheque['Estado'] = input("Ingrese el estado del cheque (pendiente, aprobado, rechazado): ").lower()
        # lower() convierte el texto a minúsculas
        if cheque['Estado'] in ['pendiente', 'aprobado', 'rechazado']:
            break
        else:
            print("Estado no válido. Debe ser 'pendiente', 'aprobado' o 'rechazado'.")

    while True:
        cheque['TipoCheque'] = input("Ingrese el tipo de cheque (EMITIDO, DEPOSITADO): ").upper()
        # upper() convierte el texto a mayúsculas
        if cheque['TipoCheque'] in ['EMITIDO', 'DEPOSITADO']:
            break
        else:
            print("Tipo de cheque no válido. Debe ser 'EMITIDO' o 'DEPOSITADO'.")

    print("Cheque ingresado correctamente!")
    return cheque

def ingresar_cheques():
    cheques = []
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de cheques a ingresar: "))
            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    
    for _ in range(cantidad):
        cheques.append(ingresar_campos())
    
    return cheques

# Ejemplo de uso
cheques_info = ingresar_cheques()
# for cheque in cheques_info:
#     print(cheque)

# Función para guardar los cheques en un archivo CSV
def guardar_cheques_csv(cheques, filename):
    
    # Define las claves de las columnas
    keys = [
        'NroCheque', 'CodigoBanco', 'CodigoSucursal', 'NumeroCuentaOrigen', 'NumeroCuentaDestino',
        'Valor', 'FechaOrigen', 'FechaPago', 'DNI', 'Estado', 'TipoCheque'
    ]

    # Abre el archivo CSV en modo escritura
    with open(filename, 'w', newline='') as file: # newline='' evita que se agreguen líneas en blanco adicionales
        dict_writer = csv.DictWriter(file, fieldnames=keys) # Crea el escritor de archivos CSV
        dict_writer.writeheader() # Escribe las claves como encabezado
        dict_writer.writerows(cheques) # Escribe los cheques en el archivo


guardar_cheques_csv(cheques_info, 'cheques.csv') # Guarda los cheques en un archivo CSV