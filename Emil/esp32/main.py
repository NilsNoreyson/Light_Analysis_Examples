import time
import machine
import neopixel


led = machine.Pin(25, machine.Pin.OUT)

np = neopixel.NeoPixel(machine.Pin(22), 22)


while True:
    for i in range(22):
        np.fill([0,0,0])
        np[i] = [255,0,0]
        np.write()
        time.sleep(0.1)


#upload this with
# ampy -p COM5 -b 115200 put main.py
# led.value(0)


# while True:
#     led.value(1)
#     time.sleep(0.5)
#     led.value(0)
#     time.sleep(0.5)

