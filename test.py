from serial import Serial
import requests
import json 
import time

ser = Serial(port='/dev/cu.usbmodem14201', baudrate=9600)

text = "ON"
#print(requests.get('https://kazar4.com:5672/lights/', verify="./newpem.cer").text)

while True:
    time.sleep(1)
    toSend = ""
    try:
        toSend = requests.get('https://kazar4.com:5672/lights/', verify=False).text
        toSend = toSend.upper()
    except:
        continue
    print("Trying To Send: " + str(toSend))
    ser.write(toSend.encode())
    #ser.write(input("Input 1 to turn on, or 0 to turn off the built-in LED: ").encode())
        #input("Input 1 to turn on, or 0 to turn off the built-in LED: ").encode())
    #value= ser.readline()
    #valueInString=str(value,'UTF-8')
    #print(valueInString) 