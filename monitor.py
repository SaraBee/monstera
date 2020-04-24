import serial
import sys
import argparse
from statistics import mean
from twitter import Twitter
from thoughts import Thoughts

moisture_threshold = 415 # arbitrary
humidity_threshold = 28.0 # arbitrary
unearthed_reading = 550 # if the sensor is not in the soil

# Run this thing with --notweet to output the tweet to stdout
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--notweet', default=False, action='store_true')
    parser.add_argument('--topic', default="moisture", action="store")
    return parser.parse_args()

def parse_sample(sample_list):
    readings = {
        "temp": [],
        "humidity": [],
        "moisture": []
        }

    for reading in sample_list:
        if '\r' not in reading:
            break
        reading = reading.strip()
        reading = reading.split(':')

        if len(reading) == 2:
            key = reading[0]
            val = reading[1]
            if key == "moisture":
                try:
                    readings["moisture"].append(int(val))
                except:
                    print("we got a weird value or something")
            elif key in ["humidity", "temp"]:
                try:
                    readings[key].append(float(val))
                except:
                    print("we got a weird value or something")
    return readings

def output(args, msg):
    if (args.notweet):
        print(msg)
    else:
        Twitter.tweet(msg)

args = get_args()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
sample = ser.read(200) # pull 200 bytes off serial

try:
    decoded_sample = sample.decode("utf-8")
except:
    print("we don't know why but there's something wrong")
    sys.exit()

# turn the decoded sample string into a list of samples
sample_list = decoded_sample.split('\n')

readings_list = parse_sample(sample_list)

if args.topic == "moisture" and len(readings_list["moisture"]):
    avg_reading = int(round(mean(readings_list["moisture"])))
    if avg_reading > unearthed_reading:
        # The sensor reading is high enough that it's probably not in soil
        msg = Thoughts.get_unearthed_thought(avg_reading)
    elif avg_reading > moisture_threshold:
        # The reading is above the arbitrary dryness threshold
        msg = Thoughts.get_thirsty_thought(avg_reading)
    else:
        # nicenice
        msg = Thoughts.get_happy_thought(avg_reading)

    output(args, msg)

if args.topic == "humidity" and len(readings_list["humidity"]):
    avg_reading = round(mean(readings_list["humidity"]), 1)

    if avg_reading < humidity_threshold:
        msg = Thoughts.get_dry_thought(avg_reading)
        output(args, msg)
