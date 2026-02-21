import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

print("Available Ports:")

for port in ports:
    print(port.device)