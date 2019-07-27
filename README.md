# Coding-Tests
I tried to keep the execution of this executable fairly simplistic in nature
so that both Windows and Linux can run this program. 

All that is needed is to type: ```py CodeTest``` and it will start the program. 
The "py" part may be different on your computer, replace the "py" with 
whatever phrase you use to start up python in terminal. It will most likely be
"python" or whatever you are using as your path variable.

Or you can just double click the CodeTest1.py file. It should pull up terminal 
and allow you to play around with the program, but that is the boring way of doing things.
You will learn alot more with using terminal to find and start a python file then by
just double clicking the program in a file. 

## Installation
Really all you need to do is clone this into a repository. Nothing needs to be installed on your system except
for Python. Once Python has been installed to your path you can run this program.

## Runtime Prompt for the application. 
Enter P for Pangram Detector, A for Animation or E to exit: 
If you enter P it will send you to the 1st function within the code.
If you enter A it will send you to the 2nd function within the code. 
If you enter E it will exit the program for you. 

## What these applications do.
### Pangram Detector. 
The user will give a string for the program to check if it is a Pangram or not. A pangram is a sentence containing every letter in the English Alphabet. 
#### Example of this: 
"The quick brown fox jumps over the lazy dog” is a Pangram because it contains all the characters from ‘a’ to ‘z’
"The quick brown fox jumps over the dog" is not a Pangram because it doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing.

### Linear Chamber Animation
A collection of particles is contained in a linear chamber. They all have the same speed,
but some are headed toward the right and others are headed toward the left. These
particles can pass through each other without disturbing the motion of the particles, so
all the particles will leave the chamber relatively quickly. The user will give two inputs 
to run the program. The first is a integer value that says the speed at which you want the particle
to move. The second is a string value which is in essence the array of the linear chamber. L in the array
means the particle is moving in the left direction and R means the particle is moving in the right direction.
The particles can overlap. Once all particles have exited out of the chamber, the program will stop.
#### Examples of this:
##### Example 1:
```2, "..R...."```
Returns:
  { "..X....",
    "....X..",
    "......X",
    "......." }
The single particle starts at the 3rd position, moves to the 5th, then 7th, and then out of
the chamber.

##### Example 2:
```3,  "RR..LRL"```
Returns:
  { "XX..XXX",
    ".X.XX..",
    "X.....X",
    "......." }
Note that, at the first time step after init, there are actually 4 particles in the chamber,
but two are passing through each other at the 4th position

##### Example 3:
```2,  "LRLR.LRLR"```
Returns:
  { "XXXX.XXXX",
    "X..X.X..X",
    ".X.X.X.X.",
    ".X.....X.",
    "........." }
At time 0 (init) there are 8 particles. At time 1, there are still 6 particles, but only 4
positions are occupied since particles are passing through each other.

##### Example 4:
```10,  "RLRLRLRLRL"```
Returns:
  { "XXXXXXXXXX",
    ".........." }
These particles are moving so fast that they all exit the chamber by time 1.

##### Example 5:
```1,  "..."```
Returns:
  { "..." }

##### Example 6:
```1,  "LRRL.LR.LRR.R.LRRL."```
Returns:
  { "XXXX.XX.XXX.X.XXXX.",
    "..XXX..X..XX.X..XX.",
    ".X.XX.X.X..XX.XX.XX",
    "X.X.XX...X.XXXXX..X",
    ".X..XXX...X..XX.X..",
    "X..X..XX.X.XX.XX.X.",
    "..X....XX..XX..XX.X",
    ".X.....XXXX..X..XX.",
    "X.....X..XX...X..XX",
    ".....X..X.XX...X..X",
    "....X..X...XX...X..",
    "...X..X.....XX...X.",
    "..X..X.......XX...X",
    ".X..X.........XX...",
    "X..X...........XX..",
    "..X.............XX.",
    ".X...............XX",
    "X.................X",
   "..................." }
   
## MakeFile
The MakeFile is an unimportant documentation because this is a python implementation. 
It was only included to give the user experience on using MakeFile functionality. 
