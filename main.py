import time
from datetime import datetime
import csv
import random

keys = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
numberOfKeys = len(keys)

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time is None:
            return 0
        elif self.end_time is None:
            return time.time() - self.start_time
        else:
            return self.end_time - self.start_time

def write_session_results(filename, date, time, bpm, elapsed_time):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if bpm != None:
            writer.writerow([date, time, bpm, elapsed_time])
        else:
            writer.writerow([date, time, elapsed_time])

def start():
    input("Press enter to begin...")
    stopwatch.start()

def cycle():
    for i in range(numberOfKeys):
        current_key = random.choice(keys)
        print()
        print("Current key:", current_key)
        print()
        keys.remove(current_key)
        input("Press enter to continue...")

def stop():
    stopwatch.stop()
    elapsed_seconds = round(stopwatch.elapsed_time())
    elapsed_minutes = elapsed_seconds // 60
    remaining_seconds = elapsed_seconds % 60
    return f"{elapsed_minutes}:{remaining_seconds:02}"

stopwatch = Stopwatch()

current_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%I:%M %p")

mode = 0
while mode not in ["1", "2"]:
    mode = input("Select mode (1 for scales, 2 for fretboard): ")

if mode == "1":
    bpm = input("Enter bpm: ")
    start()
    cycle()
    write_session_results("scale_log.csv", current_date, current_time, bpm, stop())

else:
    start()
    cycle()
    write_session_results("fretboard_log.csv", current_date, current_time, None, stop())

print("Time:", stop())
