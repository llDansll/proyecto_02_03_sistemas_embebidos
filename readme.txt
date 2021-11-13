Codigo realizado con fines educativos para la asignatura Sistemas Embebidos de la Pontificia Universidad Javeriana Colombia

Autor: Daniel M. Barrera Leguizamón

En este directorio se encuentran 13 archivos:

programa1.c	   		-> 	Prende y apaga el puerto GPIO22 de la RaspberryPi mediante systemd
programa2.c	   		-> 	Prende y apaga el puerto GPIO27 de la RaspberryPi mediante systemd
blinky_daemon_01.service 	->	Servicio para prender y apagar el puerto GPIO22 de la RaspberryPi
blinky_daemon_01.timer 		->	Servicio de temporización para prender y apagar el puerto GPIO22 de la RaspberryPi
blinky_daemon_02.service 	->	Servicio para prender y apagar el puerto GPIO27 de la RaspberryPi
blinky_daemon_02.timer 		->	Servicio de temporización para prender y apagar el puerto GPIO27 de la RaspberryPi
acelerometro.py			-> 	Muestra la lectura de aceleración del acelerómetro ADXL345
temp_sen.sh			-> 	Lee los valores del sensor DS18B20 y los almacena cada 10 segundos en un archivo llamado:
			   		AAAAMMDD_TEMPERATURA.csv, la primera columna del archivo corresponde a la fecha y
       					hora actual en formato “AAAAMMDD HHMMSS“ y la segunda a la temperatura leída desde 
					el sensor mediante systemd
temp.service			-> 	Servicio para lectura y almacenamiento de temperatura
temp.timer			-> 	Servicio de temporización para lectura y almacenamiento de temperatura
threads.py			->	Ejercicio de aplicación de hilos que utiliza en su implementación el acelerómetro
					ADXL345 y puerto serial.
acel_temp.py			->	Almacenamiento de datos en la plaraforma de AdafruitIO del promedio de 
					aceleración y temperatura durante un minuto mediante el uso de crontab
led_iot.py			->	Encendido y apagado del puerto GPIO20 de la RaspberryPi 3 desde la plataforma 
					AdafruitIO
					

Link acceso: https://github.com/llDansll/proyecto_02_03_sistemas_embebidos