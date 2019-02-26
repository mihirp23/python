#!/usr/bin/python

## Mihir Patel
## Google Foobar Challenge
## File : when_it_rains_it_pours.py

################################################################################
def answer(heights):
################################################################################
# Computes the total area of standing water accumulated when water is poured
# from the top and allowed to run off the sides. List of heights is provided.

    # initialize variables.
    num_of_heights = len(heights)
    mx_height = max(heights)
    idx_of_mx = heights.index(mx_height)
    area = 0

    # accumulate area to the left of the maximum height.
    current_idx = idx_of_mx - 1
    while (current_idx > 0):
        current_height = heights[current_idx]
        max_height_to_left = max(heights[0:current_idx])
        if max_height_to_left > current_height:
            area += max_height_to_left - current_height
        current_idx = current_idx - 1

    # accumulate area to the right of the maximum height.
    current_idx = idx_of_mx + 1
    while (current_idx < num_of_heights - 1):
        current_height = heights[current_idx]
        max_height_to_right = max(heights[current_idx:num_of_heights])
        if max_height_to_right > current_height:
            area += max_height_to_right - current_height
        current_idx = current_idx + 1

    return area
        
    
            
            
       

print answer([1, 4, 2, 5, 1, 2, 3])
print answer([1, 2, 3, 2, 1])
