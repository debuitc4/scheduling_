#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

import sys
from wait_time import wait_time
from turn_around_time import turn_around
from split_list import split_list
from format import format

def fcfs(arr):
   # sending array to split_list function
   a = split_list(arr)
   burst_times, proc_num, p = a[0], a[1], a[2]

   w = wait_time(burst_times)
   wt, in_wt = w[0], w[1]
   
   a = turn_around(burst_times)
   ta, in_ta = a[0], a[1]

   # printing order and values
   format(proc_num,p,burst_times,in_wt,in_ta)

   return [wt,ta]

