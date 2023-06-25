// Ian Mu;oz Nu;ez

#include <Servo.h>

Servo servoMotor; // Servo
int angle=90 // Variable para enviar el angulo al servo
int in; // Variable para recibir datos desde Python

void setup()
{
    Serial.begin(9600); // Comunicacion serial con 9600 baudios
    Serial.setTimeout(10); // Espera de 10 milisegundos entre cada lectura

    servoMotor.attach(9); // Asignar pin 9 para el servo
    servoMotor.write(angle); // Se mueve el servo a 90 grados

    delay(100); // Espera de 100 milisegundos (0.1 segundos)
}

void loop()
{
    if(Serial.available() > 0)
    {
        in = Serial.read(); // Recibir el angulo para el servo
        servoMotor.write(angle); // Se envia el valor 'angle' al servo
    }
    angle = in; // El nuevo angulo es igual al valor recibido
}

