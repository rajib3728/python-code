import serial
import pyautogui
import time
ArduinoSerial = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get 
while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
 
    if 'hi' in incoming:
        pyautogui.typewrite(['space'], 0.2)
    incoming = "";      