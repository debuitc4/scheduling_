#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

# formatting and printing out the values
def format(proc_num,p,burst_times,in_wt,in_ta):
   print("{:<8} {:<10} {:<10} {:<10} {:<10}".format("Task","Priority","Burst", "Wait time", "Turnaround time"))
   for i in range(0, len(p)):
      print("{:<8} {:<10} {:<10} {:<10} {:<10}".format(proc_num[i],p[i],burst_times[i], in_wt[i], in_ta[i]))

#for round robin printing the title and looping in the round robin function itself
def format_rr():
   print("{:<8} {:<10} {:<10} {:<10} {:<10}".format("Task","Priority","Burst", "Wait time", "Turnaround time"))
