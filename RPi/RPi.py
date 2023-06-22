# Import Libraries
import RPi.GPIO as GPIO
import time
import pyrebase

# Firebase Configuration
# (*) Should be changed by your own data
config = {
    "apiKey": "AIzaSyB4OBIxh7X61OfSmhSfGy_zPP-njaKBxVM",
    "authDomain": "vigia-15de1.firebaseapp.com",
    "databaseURL": "https://vigia-15de1-default-rtdb.firebaseio.com",
    "storageBucket": "vigia-15de1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin numbers for each relay
pin_relay_1 = 17
pin_relay_2 = 18
pin_relay_3 = 19
pin_relay_4 = 20

# GPIO setup for each relay
GPIO.setup(pin_relay_1, GPIO.OUT)
GPIO.setup(pin_relay_2, GPIO.OUT)
GPIO.setup(pin_relay_3, GPIO.OUT)
GPIO.setup(pin_relay_4, GPIO.OUT)

# Firebase Database Initialization
db = firebase.database()

# While loop to run until the user kills the program
while True:
    switch = db.child("Switch").get()

    for user in switch.each():
        # Check the value of the child (which is 'state')
        if user.val() == "OFF":
            # If the value is off, turn off the corresponding relay
            GPIO.output(pin_relay_1, False)
            GPIO.output(pin_relay_2, False)
            GPIO.output(pin_relay_3, False)
            GPIO.output(pin_relay_4, False)
        else:
            # If the value is not off (implies it's on), turn on the corresponding relay
            GPIO.output(pin_relay_1, True)
            GPIO.output(pin_relay_2, True)
            GPIO.output(pin_relay_3, True)
            GPIO.output(pin_relay_4, True)

        # 0.1 Second Delay
        time.sleep(0.1)
