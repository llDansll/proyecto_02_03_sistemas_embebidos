#!/bin/bash

#       Lectura sensor de temperatura DS18B20 en Bash
#
#       Lee los valores del sensor y los almacena cada segundo mediante
#       systemd en un archivo llamado:
#       AAAAMMDD_TEMPERATURA.csv, la primera columna del archivo corresponde a la fecha y
#       hora actual en formato “AAAAMMDD HHMMSS“ y la segunda a la temperatura leída desde el sensor
#
#       Autor: Daniel M. Barrera Leguizamón

#Se obtiene la fecha de ejecución del script
fecha_01=`date "+%Y%m%d"`
#Se crea el archivo AAAAMMDD_TEMPERATURA.csv
touch "$fecha_01"_TEMPERATURA.csv
#Nos ubicamos en el directorio del sensor de temperatura para su lectura
cd /sys/devices/w1_bus_master1/28-3c01b5564680
#Creamos el nombre de cada columna sobre el archivo AAAAMMDD_TEMPERATURA.csv
echo "fecha y hora actual;temperatura" > /home/pi/proyecto_01/02_part/"$fecha_01"_TEMPERATURA.csv

    #Obtenemos la fecha actual del sistema
    fecha_02=`date "+%Y%m%d"`
    #Obtenemos la hora actual del sistema
    hora=`date "+%H%M%S"`
    #Se realiza la lectura de temperatura actual del sensor
    tmp_01=`cat temperature`
    tmp_02=`bc -l <<< "scale=3; $tmp_01/1000"`
    #Se almacena la fecha, hora y temperatura en la variable msg
    msg="$fecha_02 $hora;$tmp_02"

    #Se introducen los datos de fecha, hora y temperatura en el archivo AAAAMMDD_TEMPERATURA.csv
    echo $msg >> /home/pi/proyecto_02_03/02_part/"$fecha_01"_TEMPERATURA.csv

cd /home/pi/proyecto_02_03/02_part