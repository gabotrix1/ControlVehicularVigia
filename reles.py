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
relay_pins = {
    1: 17,
    2: 18,
    3: 19,
    4: 20
}

# GPIO setup for each relay
for pin in relay_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Firebase Database Initialization
db = firebase.database()

# Initialize Firebase data
db.child("S1").set(0)
db.child("S2").set(0)
db.child("S3").set(0)
db.child("S4").set(0)

# While loop to run until the user kills the program
while True:
    try:
        # Read values from Firebase and control relays
        for relay_number, pin in relay_pins.items():
            relay_ref = db.child("S{}".format(relay_number))
            relay_state = relay_ref.get().val()

            if relay_state == 1:
                GPIO.output(pin, GPIO.LOW)
                print("Relay {} ON".format(relay_number))
            else:
                GPIO.output(pin, GPIO.HIGH)
                print("Relay {} OFF".format(relay_number))

        time.sleep(0.1)

    except KeyboardInterrupt:
        break

# Clean up GPIO
GPIO.cleanup()

