''''import serial
import time
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value)'''

import serial  # import serial library
import time

i = 0

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)  # create serial object named arduino
while True:  # create loop
    #clockwise 90 degrees
    command = "89\n"  # query servo position
    arduino.write(command.encode())  # write position to serial port
    time.sleep(0.5)
    reachedPos = str(arduino.readline())  # read serial port for arduino echo
    command = "91\n"
    arduino.write(command.encode())  # write position to serial port
    print(reachedPos)
    i = i + 1

    if(i == 3):
        break

    #anti-clockwise 90 degrees
    command = "98\n"  # query servo position
    arduino.write(command.encode())  # write position to serial port
    time.sleep(0.48)
    reachedPos = str(arduino.readline())  # read serial port for arduino echo
    command = "90\n"
    arduino.write(command.encode())  # write position to serial port
    print(reachedPos)
    i = i + 1

    if (i == 3):
        break
