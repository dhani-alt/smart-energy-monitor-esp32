import serial
import time

ser = serial.Serial("COM3", 115200)

while True:
    print("LED ON")
    ser.write(b'1')
    time.sleep(2)

    print("LED OFF")
    ser.write(b'0')
    time.sleep(2)