import RPi.GPIO as GPIO
import time

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)
    GPIO.setup(15, GPIO.OUT)

def loop():
    while True:
        potentiometer_value = GPIO.input(14)
        GPIO.output(15, potentiometer_value)
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        setup_gpio()
        loop()
    finally:
        GPIO.cleanup()