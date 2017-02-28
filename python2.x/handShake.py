'''
.SYNOPSIS
    number of handshakes in a group of people
.DESCRIPTION
    problem: If there are n number of people in a place and
    they all have to handshake with each other, then calculate the 
    number of handshakes made in total (excluding the handshakes made more than once
    between any 2 people)
.NOTES
    File Name      : handShake.py
    Author         : gajendra d ambi
    Date           : September 2016
    Prerequisite   : python 2.7.x, 
    Copyright      - None
.LINK
    Script posted over: https://github.com/MrAmbiG/python
    explanation: https://www.youtube.com/watch?v=H67bLOpVJng
'''
people = input("Number of people?: ")
n = 0
while n < people:
    handshakes = 0
    for person in range(people):
        handshakes = handshakes+person
        n = n+1
    print handshakes
