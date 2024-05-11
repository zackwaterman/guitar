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
        writer.writerow([date, time, bpm, elapsed_time])

stopwatch = Stopwatch()
bpm = input("Enter bpm: ")
input("Press enter to begin...")
stopwatch.start()

for i in range(numberOfKeys):
    currentKey = random.choice(keys)
    print()
    print("Current key:", currentKey)
    print()
    keys.remove(currentKey)
    input("Press enter to continue...")

stopwatch.stop()
elapsed_seconds = round(stopwatch.elapsed_time())
elapsed_minutes = elapsed_seconds // 60
remaining_seconds = elapsed_seconds % 60
elapsed_time_formatted = f"{elapsed_minutes}:{remaining_seconds:02}"

current_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%I:%M %p")
print("Time:", elapsed_time_formatted)
write_session_results("practice_log.csv", current_date, current_time, bpm, elapsed_time_formatted)
