# Bteam
This repository will consist of all modified ARC 2022 code, meant to be used to fly our self-build drone.
All code produced, forked, and pulled is to be finalized and looked over by all teamates. Then cleared for use.
C:\Python31\python.exe fliename.py

for Brockton student computer this is the command to run python

C:\Python31\python.exe -m pip install numpy

How to calculate distances between waypoints
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
