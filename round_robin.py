#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

from queue import Queue
from format import format_rr

def round_r(arr):
   #time quantum is 10 milliseconds
   q = 10
   time = 0
   
   burst_times = []
   #make a burst times queue
   bt = Queue()
   # make a process name queue
   pq = Queue()

   #make a dictionary to store task names and their finish times
   d = {}
   for v in arr:
      task, p, bur = v.split(",")
      burst_times.append(int(bur))
      # adding the values to the queue
      bt.enqueue(int(bur))
      pq.enqueue(task)
      # initalizing each value in the dictionary with 0
      d[task] = 0

   while not bt.isEmpty():
      v = bt.dequeue()
      pnum = pq.dequeue()

      #if the value removed from the queue is bigger
      #than the quantam time
      if v > q:
         # decrease the value by the quantam time
         v -= q
         # increase the time
         time += q
         # add the remainder of the value to the queue to be executed
         bt.enqueue(v)
         pq.enqueue(pnum)

      elif v <= q:
         #if the value is less, then increase the time by how long it takes
         time += v
         d[pnum] = time

   t = ta_time_rr(d)
   w = wait_time_rr(d, burst_times)

   # avg turnaround time and the individual turnaround times
   ta, arrt = t[0], t[1]
   # avg wait time and the individual wait times
   wt, arrw = w[0], w[1]


   format_rr()
   i = 0
   #loop through and print out
   for v in arr:
      task, p, bur = v.split(",")
      print("{:<8} {:<10} {:<10} {:<10} {:<10}".format(task, p, bur, arrw[i], arrt[i]))
      i += 1

   return [wt, ta]


def ta_time_rr(d):
   # dictionaries in python 3.6 are insertion ordered
   total = 0
   in_ta = []
   i = 0
   # add the value to the array and total
   for key, value in d.items():
      in_ta.append(value)
      total += value
      i += 1

   return [total / i, in_ta]

def wait_time_rr(d, burst):
   tot = 0
   i = 0
   in_wt = []
   # for each key, value pair in the dictionary,
   # minus the burst time from the value and add it to the total
   for key, value in d.items():
      s = value - burst[i]
      in_wt.append(s)
      tot += s
      i += 1

   return [tot / i, in_wt]
