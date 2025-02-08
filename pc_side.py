import serial
import time

# Replace 'COM3' with your Pico's COM port
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Give the connection a moment to establish

# Send a command to the Pico
ser.write(b'attack\n')

# Read the response from the Pico
#response = ser.readline()
#print(response.decode())

# Close the serial connection
ser.close()
