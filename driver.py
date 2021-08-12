#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf

import sys
from sjf import sort_sjf
from fcfs import fcfs
from priority_s import priority
from round_robin import round_r
from print import print_averages

# checking if the command line supplies the scheduling.txt file
try:
   args = sys.argv[1]
except IndexError:
   print("No filename supplied or too many arguments on command line\n")

def main():
   #opening file for reading
   try:
      file1 = open(args, 'r')
      #adding each line as an array element
      lines = [line.strip("\n") for line in file1]

      print("Shortest job first")
      ans1 = sort_sjf(lines)
      print_averages(ans1)

      print("\n")
      
      print("First come first served")
      ans2 = fcfs(lines)
      print_averages(ans2)

      print("\n")

      print("Priority scheduling")
      ans3 = priority(lines)
      print_averages(ans3)

      print("\n")
      print("Round robin scheduling")
      ans4 = round_r(lines)
      print_averages(ans4)
      
   except (IOError, NameError):
      print("Could not open file.")

   
if __name__ == "__main__":
   main()
