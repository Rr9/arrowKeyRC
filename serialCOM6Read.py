import serial
import time
ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)


while(1):
    print(ser.readline())
    time.sleep(1)


ser.close()
