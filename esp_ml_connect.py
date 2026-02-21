import serial
import numpy as np
import joblib

# Load trained model
model = joblib.load("energy_model.pkl")

# Replace COM port (check in Arduino IDE → Tools → Port)
ser = serial.Serial("COM3", 115200)

print("System Started...")

while True:
    try:
        line = ser.readline().decode().strip()
        print("Received:", line)

        values = line.split(',')
        power = float(values[0])   # Example sensor value

        data = np.array([[power]])
        prediction = model.predict(data)

        if prediction[0] == 1:
            ser.write(b"ON\n")
            print("Wastage Detected - LED ON")
        else:
            ser.write(b"OFF\n")
            print("Normal Usage - LED OFF")

    except:
        pass