#!/bin/bash
xrandr --output HDMI-2 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 1921x0 --rotate normal
xbindkeys
nohup ./cava.sh 0<&- &>/dev/null &
pkill picom
picom -b --active-opacity 0.9 --inactive-opacity 0.5 --corner-radius 5 -r 0 -o 0
