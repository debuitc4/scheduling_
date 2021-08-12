#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

from wait_time import wait_time
from turn_around_time import turn_around
from specific_sort import sort_s
from format import format

def sort_sjf(arr):
   # sending array to sort_s function (sorting on shortest job)
   new = sort_s(arr, 2)
   burst_times, proc_num, p = new[0], new[1], new[2]
   
   
   w = wait_time(burst_times)
   wt, in_wt = w[0], w[1]
   
   a = turn_around(burst_times)
   ta, in_ta = a[0], a[1]

   # printing order and values
   format(proc_num,p,burst_times,in_wt,in_ta)
   return [wt,ta]



