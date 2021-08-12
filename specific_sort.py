#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

from split_list import split_list

def sort_s(arr, i):
   # splitting list into list of lists
   a = [x.split(",") for x in arr]
   # sort on the priority
   if i == 1:
      ax = sorted(a, key=lambda x:int(x[i]), reverse=True)
   #sort on the burst times
   elif i == 2:
      ax = sorted(a, key=lambda x:int(x[i]))

   # join the sorted lists back
   li = [",".join(v) for v in ax]

   # #send to split_list function
   new = split_list(li)

   return new
