#!/bin/bash
APP="hungarian-SyS"
APP_DIR="$HOME/.local/share/$APP"
AUTO_START_DIR="$HOME/.config/autostart/"


mkdir -p $APP_DIR $AUTO_START_DIR 2>/dev/null

cp $APP.py $APP.xkb $APP_DIR
cp $APP.desktop $AUTO_START_DIR


