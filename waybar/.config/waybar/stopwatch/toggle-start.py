#!/usr/bin/python3
#------------------------------------
# Start/stop/pause polybar stopwatch.
#                     Author: 4g3nt47
#------------------------------------

import sys, os, time

if (len(sys.argv) < 2):
  print(f"[-] Usage: {sys.argv[0].split('/')[-1]} <tmpfile>")
  exit(1)

tmpfile = sys.argv[1]

# Starts the stopwatch by setting mode to 1 and saving the current time.
def start_stopwatch():
  wfo = open(tmpfile, "w")
  wfo.write(f"1 {int(time.time())} 0")
  wfo.close()
  return

# Pauses the stopwatch by setting mode to 2 and saving both the starting time and the current time. 
def pause_stopwatch(stime):
  wfo = open(tmpfile, "w")
  wfo.write(f"2 {stime} {int(time.time())}")
  wfo.close()
  return

# Resumes the stopwatch by setting mode to 2 and adjusting the start time to account for the pause duration.
def resume_stopwatch(stime, ptime):
  duration = int(time.time() - ptime)
  new_stime = stime + duration
  wfo = open(tmpfile, "w")
  wfo.write(f"1 {new_stime} 0")
  return

def main():
  if not os.path.isfile(tmpfile):
    return start_stopwatch()
  mode, stime, ptime = [int(x) for x in open(tmpfile).read().split(" ")]
  if (mode == 0): # Stopped.
    return start_stopwatch()
  if (mode == 1): # Started
    return pause_stopwatch(stime)
  if (mode == 2): # Paused.
    return resume_stopwatch(stime, ptime)

main()
