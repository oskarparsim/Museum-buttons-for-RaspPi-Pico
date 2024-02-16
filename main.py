from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

nupp1 = Pin(14, Pin.IN, Pin.PULL_UP)
nupp2 = Pin(15, Pin.IN, Pin.PULL_UP)

led.value(1)
while True:
    if nupp1.value() == 0:
        print("play1")
        while nupp1.value() == 1:
            pass
        sleep(0.2)
        
    elif nupp2.value() == 0:
        print("play2")
        while nupp2.value() == 1:
            pass
        sleep(0.2)

led.value(0)

