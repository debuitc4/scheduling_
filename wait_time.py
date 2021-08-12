#!/usr/bin/env python3

def wait_time(arr):
   # calculating the wait time
   wait_time = 0
   accum = 0
   in_wt = []
   i = 0
   while i < len(arr) - 1:
      in_wt.append(wait_time)
      wait_time += int(arr[i])
      accum += wait_time
      i += 1
   
   in_wt.append(wait_time)
   _sum = accum / (i + 1)
   return [_sum, in_wt]
