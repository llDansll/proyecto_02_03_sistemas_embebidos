#!/bin/python3

"""
    Lectura de Acelerómetro ADXL345 y sensor de temperatura DS18B20 mediante servicio IoT

    Lee la aceleración de cada uno de los ejes del acelerómetro ADXL345 en metros sobre segundo y la temperatura
    del sensor DS18B20, se promedian sus valores durante aproximadamente un minuto mediante un crontable y se sube dicho promedio
    a la plataforma IoT de adafruit io.

    Autor: Daniel M. Barrera Leguizamón
"""

import time                                                     # Librería time para generar retardos
import board                                                    # Librería de lectura de puertos de Adafruit
import busio                                                    # Libreria para el manejo del protocolo I2C
import adafruit_adxl34x                                         # Librería o Driver para el manejo del Acelerómetro ADXL345
from w1thermsensor import W1ThermSensor                         # Librería o Driver para el manejo del sensor de temperatura
from Adafruit_IO import *                                       # Importar funcionabilidad del servicio IoT ofrecido por Adafruit
aio = Client('User','Key')     # Se realiza la sincronización del usuario y el key de la cuenta

i2c = busio.I2C(board.SCL, board.SDA)                   # Se inicializa el bus de comunicaciones I2C
accelerometer = adafruit_adxl34x.ADXL345(i2c)           # Se configura el dispositivo específico, para este caso el ADXL345
sensor = W1ThermSensor()                                # Se inicializa la configuración para el sensor de temperatura DS18B20

dato_x = 0.0                                            # Variables auxiliares para la lectura de aceleración
dato_y = 0.0
dato_z = 0.0

temp = 0.0                                              # Variable auxiliar para lectura de temperatura

samples = 86                                            # Numero de muestras a tomar por minuto
sampling = 0.25                                         # Tiempo de muestreo

for i in range(samples):                                # Bucle para realizar el muestreo de la lectura de los sensores durante
    dato_x += accelerometer.acceleration[0]             # un minuto
    dato_y += accelerometer.acceleration[1]
    dato_z += accelerometer.acceleration[2]
    time.sleep(sampling)
    temp += sensor.get_temperature()
    time.sleep(sampling)

prom_dato_x = dato_x/samples                            # Se promedian los datos obtenidos por los sensores durante un minuto
prom_dato_y = dato_y/samples
prom_dato_z = dato_z/samples
prom_temp = temp/samples

aio.send("accelerometer-x-axis",prom_dato_x)            # Se realiza el envío del promedio realizado para la aceleración de
aio.send("accelerometer-y-axis",prom_dato_y)            # los tres ejes a la plataforma IoT de Adafruit
aio.send("accelerometer-z-axis",prom_dato_z)

aio.send("temperature",prom_temp)                       # Se realiza el envío del promedio realizado para la temperatura
                                                        # a la plataforma IoT de Adafruit