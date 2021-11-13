"""
    Encendido y apagado del puerto GPIO20 mediante servicio IoT

    Enciende y apaga el puerto GPIO20 de la RaspberryPi 3 mediante un pulsador contenido en la plataforma
    IoT de Adafruit.

    Autor: Daniel M. Barrera Leguizamón
"""

import time                                                     # Librería time para generar retardos
import digitalio                                                # Librerias para cofniguración de puertos entrada salida
import board
from Adafruit_IO import Client, Feed, RequestError              # Importar funcionabilidad del servicio IoT ofrecido por Adafruit
aio = Client('User','Key')     # Se realiza la sincronización del usuario y el key de la cuenta

try:                                                            # Se relaciona el nombre del feed o etiqueta del interruptor
    digital = aio.feeds('digital')                              # de la plataforma IoT con la variable "digital"
except RequestError: # create a digital feed
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)

led = digitalio.DigitalInOut(board.D20)                         # Se configura el puerto GPIO20 como salida
led.direction = digitalio.Direction.OUTPUT

while True:
    data = aio.receive(digital.key)                             # Se lee el dato proveniente de la plataforma, 1 o 0
    led.value = int(data.value)                                 # Se coloca el valor de la posición dle switch en el puerto GPIO20