#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

def print_averages(ans):
   w = "Average wait time: {:.2f} ms"
   t = "Average turnaround Time: {:.2f} ms"
   
   print(w.format(ans[0]))
   print(t.format(ans[1]))
