import RPi.GPIO as GPIO

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():    
    while True:
        if GPIO.input(15) == GPIO.HIGH:
            GPIO.output(14, GPIO.HIGH)
        else:
            GPIO.output(14, GPIO.LOW)
    
if __name__ == "__main__":
    try:
        setup_gpio()
        loop()
    finally:
        GPIO.cleanup()