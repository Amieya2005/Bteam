# Bteam

This is all of our notes for coding!!!!

This repository will consist of all modified ARC 2022 code, meant to be used to fly our self-build drone.
All code produced, forked, and pulled is to be finalized and looked over by all teammates. Then cleared for use.
C:\Python31\python.exe fliename.py

for Brockton student computer this is the command to run python

C:\Python31\python.exe -m pip install numpy

Ctrl-Z = to end the process in the terminal
Ctrl-Shift-V = to paste a code in python
**********Ctrl-S = Save *************
PLEASE USE THIS FOR WHEN EVER YOU MAKE AN EDIT INTO YOUR CODE SO IT CAN BE SAVED AND THEN YOU CAN STAGE IT
pwd = print working directory
cd ../ to go back a file - moves back a level
ls = list the files in the file_folder
$Env:Path

when running a program you have to launch.
Python is an interpretive language = is the interpreter

string = key
'7' = string = key
  #'7' this is the example to show that the string and key mean the same thing
 '7' = 'a'
 'a' = string

 Dictionaries are used to store values in keys
len() can be used to show how many items are in the Dictionaries

SPACES ARE DIFFERENT FROM TABS, CHOOSE ONE OF THEM AND STICK WITH IT!!

****How to calculate distances between waypoints****
open powershell, an you should be prompted by
PS C:\Users\user>
first, you need to run python by typing the command "py.exe"
it should look like,
PS C:\Users\user> py.exe
A sequence should run and now you should see
>>>
type out "import numpy"
your screen should display
>>> import numpy
(MAKE SURE YOU PRESS SPACE BEFORE YOU TYPE OUT THE COMMAND)
Press enter you and should see,
 >>>
type out the following, and press enter after each one
a= numpy.array((0,0,3))
a is the first point
b= numphy.array((0,0,6))
b is the second point
o= numphy.array((0,0,0))
o is the origin
dist = numpy.linalg.norm(o-a)
(this bit of code calculates the first distance)
dist2 = numpy.linalg.norm(o-b)
(this calculates the second difference)
at this time, your screen should display
>>> a= numpy.array((0,0,3))
>>> b= numpy.array((0,0,6))
>>> o= numpy.array((0,0,0))
>>> dist = numpy.linalg.norm(o-a)
>>> dist = numpy.linalg.norm(o-b)
Everything that you've just typed out is the information needed for the computer to calculate the distance between your waypoints. Now we're going to use that, to get the distances.
after you type out >>> dist = numpy.linalg.norm(o-b), press enter so that you see
>>>
(here, you're going to enter the distance you want to find. Previously we made two code equation that had dist and dist2. These are the two distances you're trying to find.)
type out dist
your screen should look like this
>>> dist
when you press enter, it should display
3.00
(this means 3 is the first distance between your waypoints)
next, hit enter and type out dist2
your screen should display
>>> dist 2
when you press enter it should display 6.0
(this means 6 is your second distance)
Lesson:complete!
2/19/22-Interactive Python
---------------------------------------------------------------------
