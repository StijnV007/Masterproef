import RPi.GPIO as GPIO

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(15, GPIO.FALLING, callback=button_callback, bouncetime=200)

def loop():
    while True:
        pass

def button_callback(channel):
    GPIO.output(14, not GPIO.input(14))


if __name__ == "__main__":
    try:
        setup_gpio()
        loop()
    finally:
        GPIO.cleanup()