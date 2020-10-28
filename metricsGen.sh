#!/bin/bash

# Consts
BLOCKS=35000000
RAND=$(shuf -i 1-10 -n 1)

# How many times it'll run
COUNTEDBLOCKS=$(( $BLOCKS ))
echo "Process count: " $COUNTEDBLOCKS

# Blast the CPU
dd if=/dev/zero of=/dev/null count=$COUNTEDBLOCKS;