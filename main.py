import time
from datetime import datetime
import csv
import random

strings = ["E", "A", "D", "G", "B", "e"]
number_of_strings = len(strings)

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

def write_session_results(filename, date, time, misc, elapsed_time):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, misc, elapsed_time])

def start():
    input("Press enter to begin...")
    stopwatch.start()

def cycle():
    keys = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    number_of_keys = len(keys)

    for i in range(number_of_keys):
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
    focus = None

    while focus not in range(1, 7):
        focus = int(input("Enter the string you want to focus on: "))

    start()

    cycle()

    write_session_results("fretboard_log.csv", current_date, current_time, focus, stop())

print("Time:", stop())
