import math

Slices, Rings, Radius = map(float, input().split())
ax, ay, bx, by = map(float, input().split())

distance = Radius / Rings

option1 = distance * ax + distance * bx

winkel = Slices * 2 / abs(ay - by)



option2 = 2 * math.pi * winkel


print(min(option1, option2))