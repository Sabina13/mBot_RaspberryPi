import serial
import RPi.GPIO as GPIO
import time
 
ser=serial.Serial("/dev/ttyUSB0",9600)  
ser.baudrate=9600
def blink(pin):
    
    
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)  
    return
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
while True:
    
    read_ser=ser.readline()    
    if(read_ser== b'Hello From Arduino!\r\n'):
        GPIO.output(18,GPIO.HIGH)
    else:
        GPIO.output(18,GPIO.LOW)


     

