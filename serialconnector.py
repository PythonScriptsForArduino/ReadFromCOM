# run this command in the console to get serial function !pip install pyserial

import serial
import csv
import datetime
import serial.tools.list_ports

#List all com devices
list = serial.tools.list_ports.comports()
connected = []
for element in list:
    connected.append(element.description)
print("\n\n\nConnected COM ports:\n")
print("\n".join(connected))

#enter com port number to listen to that port
print ("\n\nIf you get the error: \"SerialException: could not open port 'COMXX': WindowsError(5, 'Access is denied.')\" \n")
print("Reset device or plug it out and back in and restart script")
portNo = input("Which port to connect to?\t")
portString = "COM" + str(portNo)

#start listening to that port
ser = serial.Serial(
    port=portString,\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print ("\n")     
print("connected to: " , ser.portstr)

#add headers to the csv file
header = ["Time", "Data"]
with open(r'output.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                
seq = []
count = 1
row = []     
print ("\n")           
print ("Data is writing to csv (Ctrl + C to finish capturing)...")

while True:
    
    for c in ser.read():
        seq.append(c)
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array
        if c == '\n':
            
            #print incomind data and write csv
            #print("Line " + str(count) + ': ' + joined_seq)
            with open(r'output.csv', 'a') as f:
                writer = csv.writer(f)
                row.append(datetime.datetime.now().strftime("%H:%M:%S"))
                row.append(joined_seq.strip())
                #print row
                writer.writerow(row)
        
            seq = []
            count += 1
            row = []
            break


ser.close()