#!/bin/python3

"""
    Ejercicio hilos en python

    Lee el valor de aceleración de cada uno de los ejes del acelerómetro ADXL345 en el primer hilo,
    en un segundo hilo se envía un dato por puerto serial desde el computador y en un tercer hilo se lee
    el valor del sensor y se utiliza el dato por el puerto serial para promediar las lecturas del sensor
    y enviar el dato por puerto serial para ser visualizado en una terminal

    Autor: Daniel M. Barrera Leguizamón
"""

import time                                         # Importación de librerías para el manejo de retardos, hilos,
import sys                                          # puerto serial y acelerómtero ADXL345
import board
import busio
import adafruit_adxl34x
import serial
import threading

i2c = busio.I2C(board.SCL, board.SDA)               # Se inicializa el bus de comunicaciones I2C
accelerometer = adafruit_adxl34x.ADXL345(i2c)       # Se configura el dispositivo específico, para este caso el ADXL345

# Configuracion puerto serial
ser = serial.Serial ("/dev/ttyS0", baudrate = 115200, parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3000)

# Se declaran variables globales del programa
accel_data_x = []
accel_data_y = []
accel_data_z = []
accel_x = 0.0
accel_y = 0.0
accel_z = 0.0
dataN = []

def acel():                                     # Hilo para lectura del acelerometro
    while 1:
        accel_x = accelerometer.acceleration[0] # Se realiza la lectura del eje x del acelerometro
        accel_y = accelerometer.acceleration[1] # Se realiza la lectura del eje y del acelerometro
        accel_z = accelerometer.acceleration[2] # Se realiza la lectura del eje z del acelerometro
        accel_data_x.append(accel_x)            # Se utiliza la función reentrante "append" para enviar el dato
        accel_data_y.append(accel_y)            # a otro hilo por cada uno de los ejes
        accel_data_z.append(accel_z)

def mean():
    N = 5                                       # Hilo para promediar lectura y mostrar en puerto serial
    mean_x = []
    mean_y = []
    mean_z = []
    while  1:
        if (len(accel_data_x) > 0) and (len(accel_data_y) > 0) and (len(accel_data_z) > 0):     # Se comprueba que la longitud
            mean_x.append(accel_data_x.pop(0))                                                  # del arreglo para cada eje sea
            mean_y.append(accel_data_y.pop(0))                                                  # mayor a cero
            mean_z.append(accel_data_z.pop(0))
        if (len(mean_x) == N and len(mean_y) == N and len(mean_z) == N):                # Cuando la longitud del arreglo es igual
            data_x = sum(mean_x)/len(mean_x)                                            # al numero de muestras N se realiza el
            data_y = sum(mean_y)/len(mean_y)                                            # promedio de las lecturas por cada eje
            data_z = sum(mean_z)/len(mean_z)
            mean_x.clear()                              # Se limpian los arreglos de las variables de promedio y lectura de sensor
            mean_y.clear()
            mean_z.clear()
            accel_data_x.clear()
            accel_data_y.clear()
            accel_data_z.clear()
            if (len(dataN) > 0):
                data_f = str(data_x) + "  " + str(data_y) + "  " + str(data_z) + "  -> PROMEDIO " + str(N)  + "\n\r"
                ser.write(data_f.encode())              # Se envía el dato por puerto serial
                N = dataN.pop(0)

def serial():                                           # Hilo para recibir el dato del puerto serial
    init = ""
    fin = ""
    number = 0

    while 1:
        data = ser.read(18)                             # Se lee una trama de 17 caractéres
        time.sleep(0.03)
        data_f = data[0:17].decode("utf-8")
        data_div = data_f.split("-")                    # Se divide el string de acuerdo a la separacion "-"

        for i in range(len(data_div)):                  # Se asignan variables independientes para cada trama ##PROMEDIO, NNN, ##
            if i == 0:
                init = data_div[0]
            if i == 1:
                try:
                    number = int(data_div[1])
                except ValueError:
                    number = 0
            if i == 2:
                fin = data_div[2]

        if init == "##PROMEDIO" and number > 0 and number <= 999 and fin == ("##"):     # Se compara el dato enviado por puerto serial
            dataN.append(number)                                                        # con el mensaje ##PROMEDIO-NNN-##
        else:
            print("Dato Inválido")                                                      # Si no es correcta la comparación no se
                                                                                        # valida el mensaje
# Configuración de hilos
tt1 = threading.Thread(target=acel)
tt2 = threading.Thread(target=mean)
tt3 = threading.Thread(target=serial)

# Se inicializan los hilos
tt1.start()
tt2.start()
tt3.start()