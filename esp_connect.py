import serial
import time

ser = serial.Serial('COM3', 115200)
time.sleep(2)

print("Connected to ESP32...\n")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Received:", data)

        value = int(data)

        if value > 2000:
            ser.write(b'1')
            print("LED ON\n")
        else:
            ser.write(b'0')
            print("LED OFF\n")