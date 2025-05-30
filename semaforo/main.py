from machine import Pin
from utime import sleep



ledverde = Pin(2, Pin.OUT)
ledamarillo = Pin(4, Pin.OUT)
ledrojo = Pin(15, Pin.OUT)

while True:
 
  #verde
  ledverde.on()
  print("prende led verde")
  sleep(3)
  ledverde.off()
  print("apaga led verde")
  sleep(2)


  #amarillo
  ledamarillo.on()
  print("prende led amarillo")
  sleep(3)
  ledamarillo.off()
  print("apaga led amarillo")
  sleep(2)

  #rojo  
  ledrojo.on()
  print("prende led rojo")
  sleep(3)
  ledrojo.off()
  print("apaga led red")
  sleep(2)
