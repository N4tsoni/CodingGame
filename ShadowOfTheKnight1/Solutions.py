import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

xmax,ymax= w -1, h-1
xmin= ymin =0 

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if ("U") in bomb_dir :
       ymax= y0-1
    if ("D") in bomb_dir :
       ymin= y0+1
    if ("R") in bomb_dir :
       xmin= x0+1
    if ("L") in bomb_dir :
       xmax= x0-1
    x0 = xmin + math.ceil((xmax-xmin)/2)
    y0 = ymin + math.ceil((ymax-ymin)/2)
               
    # Write an action using print
    print(f"ymax={ymax} ymin={ymin} xmin={xmin}, xmax={xmax}", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print("{0} {1}".format(int(x0),int(y0)))
