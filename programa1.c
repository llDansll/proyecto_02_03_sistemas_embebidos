/*
    Blinky en C para puerto GPIO22

    Enciende y apaga el puerto GPIO22

    Autor: Daniel M. Barrera Leguizamón
*/

#include <wiringPi.h>           // Incluimos la libreria para configuración de puertos en la tarjeta

int main(void)
{
    wiringPiSetup();            // Inicializamos configuración de puertos
    pinMode(3,OUTPUT);          // Configuramos el puerto GPIO22 de la tarjeta o el puerto 3 de la librería WiringPI

    digitalWrite(3,1);          // Encendemos el puerto GPIO22
    delay(100);                 // Espera de 100ms
    digitalWrite(3,0);          // Apagamos el puerto GPIO22
    delay(100);                 // Espera de 100ms

    return 0;
}