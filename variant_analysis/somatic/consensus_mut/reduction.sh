#!/bin/bash

# Ask user to introduce initial number of mutations and final number after quality filter
echo "Introduce the initial number of mutations:"
read initial
echo "Introduce the final number of mutations after quality filtering:"
read final

# Calculate the difference in the number of variants
reduction_abs=$((initial - final))

# Calculate reduction percent
percent_reduction=$(echo "scale=4; ($reduction_abs / $initial) * 100" | bc)

# Show the result
echo "This is the percent of reduction after quality filter: $percent_reduction%"
