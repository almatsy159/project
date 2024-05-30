#!/bin/bash

# ^([A-Z]|[0-9]:)(.|$)$
x=$1

y=$(grep -E $1)
z=$(grep -v $1)
