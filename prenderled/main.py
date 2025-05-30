#Librerias para trabajar
from machine import Pin
from utime import sleep 

#Creacion de variables
ledAzul= Pin(2,Pin.OUT)

#Cracion de ciclo para que prenda el led
while True:
  #El valor 1 es prendido y 0 apagado
  ledAzul.value(1)
  print ("predio")
  sleep(2)

  ledAzul.value(0)
  print ("apagado")
  sleep(2)

