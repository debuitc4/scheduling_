#!/usr/bin/env python3

def turn_around(arr):
   turn_time = 0
   accum = 0
   count = 0
   in_ta = []
   # calculate the turn around time
   for v in arr:
      turn_time = turn_time + int(v)
      in_ta.append(turn_time)
      accum += turn_time
      count += 1

   return [accum / count, in_ta]
