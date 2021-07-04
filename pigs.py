import pigpio
import time

pi = pigpio.pi()
bright = 255

GREEN = 17
RED = 27
BLUE = 22
STEP = 1

def updateColor(color, step):
    color += step
    if color > 255:
        return 255
    if color < 0:
        return 0
    return color

def setLights(pin, brightness):
    realBrightness = int(int(brightness) * (float(bright)/255.0))
    pi.set_PWM_dutycycle(pin, realBrightness)

def fading():
    r = 255
    b = 0
    g = 0
    while True:
        print(str(r) + " " + str(g) + " " + str(b))
        if r == 255 and b == 0 and g < 255:
            g = updateColor(g,STEP)
            setLights(GREEN,g)
        elif g == 255 and b == 0 and r > 0:
            r = updateColor(r,-STEP)
            setLights(RED,r)
        elif r == 0 and g == 255 and b < 255:
            b = updateColor(b, STEP)
            setLights(BLUE,b)
        elif r == 0 and g > 0 and b == 255:
            g = updateColor(g, -STEP)
            setLights(GREEN,g)
        elif r < 255 and g == 0 and b == 255:
            r = updateColor(r,STEP)
            setLights(RED,r)
        elif r == 255 and g == 0 and b > 0:
            b = setLights(b,-STEP)
            setLights(BLUE,b)
    
    time.sleep(0.5)
