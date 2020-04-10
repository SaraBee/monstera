import serial
import sys
from statistics import mean

lower_bound = 250
threshold_reading = 425 #arbitrary

def get_reading(reading):
    try:
        return int(reading)
    except:
        return 0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
sample = ser.read(100) # pull 100 bytes off serial

try:
    decoded_sample = sample.decode("utf-8")
except:
    print("we don't know why but there's something wrong")
    sys.exit()

# turn the decoded sample string into a list of samples
sample_list = decoded_sample.split('\r\n')

readings_list = []
for reading in sample_list:
    reading = get_reading(reading)
    # sometimes a reading gets truncated; any value above lower_bound is real
    if reading > lower_bound:
        readings_list.append(reading)

if len(readings_list):
    avg_reading = int(round(mean(readings_list)))
    print(avg_reading)
    if avg_reading > threshold_reading:
        print("This is when we would send a tweet I guess")
else:
    print("no readings")
