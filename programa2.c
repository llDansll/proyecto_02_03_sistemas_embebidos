/*
    Blinky en C para puerto GPIO27

    Enciende y apaga el puerto GPIO27

    Autor: Daniel M. Barrera Leguizamón
*/

#include <wiringPi.h>                   // Incluimos la libreria para configuración de puertos en la tarjeta

int main(void)
{
    wiringPiSetup();            // Inicializamos configuración de puertos
    pinMode(2,OUTPUT);          // Configuramos el puerto GPIO27 de la tarjeta o el puerto 2 de la librería WiringPI

    digitalWrite(2,1);          // Encendemos el puerto GPIO27
    delay(100);                 // Espera de 100ms
    digitalWrite(2,0);          // Apagamos el puerto GPIO27
    delay(100);                 // Espera de 100ms

    return 0;
}