import RPi.GPIO as GPIO
import time
import Adafruit_DHT

def loop():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
        time.sleep(1)

if __name__ == '__main__':
    try:
        loop()
    finally:
        GPIO.cleanup()