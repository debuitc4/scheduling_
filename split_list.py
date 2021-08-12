#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

def split_list(arr):
   burst_times = []
   proc_num = []
   p = []
   # splitting the values into their arrays
   for v in arr:
      proc, prior, bur = v.split(",")
      p.append(int(prior))
      proc_num.append(proc)
      burst_times.append(bur)
   
   #returning the split lists
   return [burst_times, proc_num, p]
   