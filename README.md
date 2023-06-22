# Vehicle Control Vigía Project

This project is intended to show you how to control connected relay switches with a Raspberry Pi using your iOS/android device or web browser, allowing you to control any hardware in the vehicle.

A relay switch (x4) on the Raspberry Pi pin connected to Firebase controlled by an app and a web client has been used in this project.


* **Fire Base**
  
     - Initializing Google Firebase.
       After creating the Firebase project in your console, you need to create an object called "Switch" that contains a "state" value between "ON/OFF"

* **Raspberry Pi - relay switch**
     - Connection of the relay switch with the Raspberry Pi.
      The circuit should be like this:
     ![RPi circuit image](https://github.com/gabotrix1/ControlVehicularVigia/blob/master/RPi/RPi_circuit.png)

   
     - Initialize python program on (Raspberry Pi) connected with Firebase API to get data.

       [**Code**](https://github.com/gabotrix1/ControlVehicularVigia/blob/master/RPi/RPi.py)


* **iOS APP**
     - Initialize the Xcode project and then connect the app with Firebase.
   
       [**Code**](https://github.com/gabotrix1/ControlVehicularVigia/tree/master/iOS)

* **Customer website**
     - Initialize the web client project and then connect it with Firebase.
    
    
       [**Code**](https://github.com/gabotrix/ControlVehicularVigia/tree/master/WEB%20client)

       ![Web page image](https://github.com/ZiyadAlSamhan/home-automation/blob/master/WEB%20client/WebP.png)
