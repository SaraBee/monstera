import serial
import sys
import argparse
from statistics import mean
from twitter import Twitter
from thoughts import Thoughts

lower_bound = 250
threshold_reading = 425 # arbitrary
unearthed_reading = 550 # if the sensor is not in the soil

# Run this thing with --notweet to output the tweet to stdout
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--notweet', default=False, action='store_true')
    return parser.parse_args()

def get_reading(reading):
    try:
        return int(reading)
    except:
        return 0

args = get_args()

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
    if avg_reading > unearthed_reading:
        # The sensor reading is high enough that it's probably not in soil
        msg = Thoughts.get_unearthed_thought(avg_reading)
    elif avg_reading > threshold_reading:
        # The reading is above the arbitrary dryness threshold
        msg = Thoughts.get_thirsty_thought(avg_reading)
    else:
        # nicenice
        msg = Thoughts.get_happy_thought(avg_reading)

    if (args.notweet):
        print(msg)
    else:
        Twitter.tweet(msg)
else:
    print("no readings")
