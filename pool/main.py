pool_size = int(input())
trees = input()
positions = input().split()
r = int(positions[0])
c = int(positions[1])

distance_from_top = r - 1
distance_from_bottom = pool_size - r
distance_from_left = c - 1
distance_from_right = pool_size - c

bigger_y = 0
if distance_from_top > distance_from_bottom:
    bigger_y = distance_from_top
else:
    bigger_y = distance_from_bottom

bigger_x = 0
if distance_from_left > distance_from_right:
    bigger_x = distance_from_left
else:
    bigger_x = distance_from_right

bigger_total = 0
if bigger_x > bigger_y:
    bigger_total = bigger_x
else:
    bigger_total = bigger_y

print (bigger_total)
