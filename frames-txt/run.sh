#!/bin/sh --

directory=$(dirname $0)

clear

color=1

while true; do
  for i in ${directory}/*.txt; do
    tput home
    tput setaf $((${color} + 1))
    cat $i
    color=$(((${color} + 1) % 5))
    sleep 0.05
  done
done
