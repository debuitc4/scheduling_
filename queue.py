#!/usr/bin/env python3

# Caoimhe De Buitlear: 19378783
# I acknowledge the DCU Academic Integrity Policy: https://www.dcu.ie/sites/default/files/policy/1_-_integrity_and_plagiarism_policy_ovpaa-v4.pdf
# References: I took this code from a task we did in my data structures and algorithms module

class Queue:
    def __init__(self):
        self.items = []

    # check if the queue is empty
    def isEmpty(self):
        return self.items == []

    # add things to the end of the queue
    def enqueue(self, item):
        self.items.insert(0,item)

    # removing things from the front of the queue
    def dequeue(self):
        return self.items.pop()

    #returning the size of the queue
    def size(self):
        return len(self.items)
