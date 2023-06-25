// Ian Mu;oz Nu;ez

#include <Servo.h>

Servo servoX; // Servo para el eje 'x'
Servo servoY; // Servo para el eje 'y'
int inX, inY; // Variables para recibir datos desde Python
int angleX=90, angleY=90; // Variables para enviar angulos a los servos

void setup()
{
    Serial.begin(9600); // Comunicacion serial con 9600 baudios
    Serial.setTimeout(10); // Espera de 10 milisegundos entre cada lectura

    servoX.attach(9); // Asignar el pin 9 para el servo del eje 'x'
    servoX.attach(10); // Asignar el pin 10 para el servo del eje 'y'

    servoX.write(angleX); // Se mueve el servo del eje 'x' a 90 grados
    servoY.write(angleY); // Se mueve el servo del eje 'y' a 90 grados

    delay(100); // Espera de 100 milisegundos (0.1 segundos)

    while(!Serial){} // Esperar a que haya comunicacion serial
}

void loop()
{
    if(Serial.available() > 0) // Si la comunicacion serial esta en uso
    {
        inX = Serial.read(); // Recibir el angulo para el servo del eje 'x'
        delay(10); // Espera de 10 milisegundos (0.01 segundos)
        inY = Serial.read(); // Recibir el angulo para el servo del eje 'y'

        servoX.write(angleX); // Se envia el valor 'angleX' al servo del eje 'x'
        servoY.write(angleY); // Se envia el valor 'angleY' al servo del eje 'y'
    }
    angleX = inX; // El angulo en 'x' es igual al valor 'inX' recibido
    angleY = inY; // El angulo en 'y' es igual al valor 'inY' recibido
}

