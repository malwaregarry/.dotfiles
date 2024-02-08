#!/usr/bin/python3
#-----------------------------------------------------
# Displays the stopwatch status icon and elapsed time.
#                                      Author: 4g3nt47
#-----------------------------------------------------

import sys, os, time, datetime

if (len(sys.argv) < 2):
  print(f"[-] Usage: {sys.argv[0].split('/')[-1]} <tmpfile>")
  exit(1)

tmpfile = sys.argv[1]
stopped_icon = "󰔞"
started_icon = "󱫟"
paused_icon  = "󱫡"

# Get the elapsed time between two given epochs (in seconds).
# Format: "days:hours:minutes:secs"
def get_time_diff(start_time, curr_time):
  diff = curr_time - start_time
  secs = diff % 60
  mins = int(diff / 60) % 60
  hours = int(diff / (60 * 60)) % 24
  return "%02d:%02d:%02d" %(hours, mins, secs)

def main():
  try:
    if os.path.isfile(tmpfile):
      mode, stime, ptime = [int(x) for x in open(tmpfile).read().split(" ")]
    else:
      raise Exception()
  except Exception as e:
    return f"{stopped_icon} --:--:--:--"
  curr_time = int(time.time())
  if (mode == 0): # Stopwatch is not running.
    return f"{stopped_icon} 00:00:00:00"
  if (mode == 1): # Stopwatch is running.
    return f"{started_icon} {get_time_diff(stime, curr_time)}"
  if (mode == 2): # Stopwatch is paused.
    return f"{paused_icon} {get_time_diff(stime, ptime)}"
  return f"{stopped_icon} BAD CONFIG"

print(main())
