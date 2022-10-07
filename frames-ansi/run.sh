#!/bin/sh --

directory=$(dirname $0)

clear

while true; do
  for i in ${directory}/*.ansi; do
    tput home
    cat $i
    sleep 0.05
  done
done
