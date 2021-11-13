#!/bin/python3

"""
    Lectura Aceleórmetro ADXL345

    Lee la aceleración de cada uno de los ejes del acelerómetro ADXL345 en metros sobre segundo, utiliza libreria de Adafruit

    Autor: Daniel M. Barrera Leguizamón
"""


import time                     # Librería time para generar retardos
import board                    # Librería de lectura de puertos de Adafruit
import busio                    # Libreria para el manejo del protocolo I2C
import adafruit_adxl34x         # Librería o Driver para el manejo del Acelerómetro ADXL345

i2c = busio.I2C(board.SCL, board.SDA)                   # Se inicializa el bus de comunicaciones I2C
accelerometer = adafruit_adxl34x.ADXL345(i2c)           # Se configura el dispositivo específico, para este caso el ADXL345

while True:
    print("%f %f %f"%accelerometer.acceleration)        # Se imprime en pantalla el valor de aceleración de los tres ejes x, y, z
    time.sleep(1)                                       # Se realiza un retardo de 1 segundo