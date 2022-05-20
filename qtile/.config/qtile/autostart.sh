#!/usr/bin/env bash

nitrogen --restore &
nm-applet &
blueberry-daemon &
lxsession &
picom --experimental-backends -b &
