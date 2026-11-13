import math

Slices, Rings, Radius = map(float, input().split())
a_s, a_r, b_s, b_r = map(float, input().split())

segment_len = Radius / Rings

option1 = (a_r + b_r) * segment_len

small_radius = min(a_r, b_r) * segment_len

option2 = abs(a_r - b_r) * segment_len + (2 * math.pi * small_radius * abs(a_s - b_s) / (2 * Slices + 1))

print(min(option1, option2))